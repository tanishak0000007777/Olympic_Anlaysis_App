import streamlit as st
import pandas as pd
import preprocessor
import helper
from helper import medal_tally
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.figure_factory as ff

# --- Page Setup ---
st.set_page_config(page_title='Olympics Analysis Dashboard 🏅', layout='wide')

# --- Load Data ---
df = preprocessor.preprocessor()

# --- Sidebar Setup ---
with st.sidebar:
    st.image('https://upload.wikimedia.org/wikipedia/commons/5/5c/Olympic_rings_without_rims.svg', width=150)
    st.title('🏟️ Olympics Analysis')
    user_menu = st.radio(
        'Select an option',
        ('Medal Tally', 'OverAll Analysis', 'Country-wise Analysis', 'Athlete-wise Analysis')
    )
    st.markdown("---")

# --- Medal Tally ---
if user_menu == 'Medal Tally':
    st.sidebar.header('🏅 Medal Tally Filters')
    years, country = helper.country_year_list(df)
    selected_year = st.sidebar.selectbox("Select Year", years)
    selected_country = st.sidebar.selectbox("Select Country", country)

    medal_tally = helper.fetch_medal_tally(df, selected_year, selected_country)

    # Title
    if selected_year == 'Overall' and selected_country == 'Overall':
        st.subheader('🥇 Overall Medal Tally')
    elif selected_year != 'Overall' and selected_country == 'Overall':
        st.subheader(f'🏅 Medal Tally in {selected_year} Olympics')
    elif selected_year == 'Overall' and selected_country != 'Overall':
        st.subheader(f'📊 {selected_country} Overall Performance')
    else:
        st.subheader(f'🎖️ {selected_country} Performance in {selected_year} Olympics')

    st.dataframe(medal_tally.style.highlight_max(axis=0, color='lightgreen'), use_container_width=True)

# --- Overall Analysis ---
if user_menu == 'OverAll Analysis':
    st.title('📊 Top-Level Statistics')

    editions = df['Year'].nunique() - 1
    cities = df['City'].nunique()
    sports = df['Sport'].nunique()
    events = df['Event'].nunique()
    athletes = df['Name'].nunique()
    nationss = df['region'].nunique()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric('Editions', editions)
    with col2:
        st.metric('Hosts', cities)
    with col3:
        st.metric('Sports', sports)

    col4, col5, col6 = st.columns(3)
    with col4:
        st.metric('Events', events)
    with col5:
        st.metric('Athletes', athletes)
    with col6:
        st.metric('Nations', nationss)

    st.markdown("---")
    st.subheader("📈 Participation Trends Over Time")

    nation_over_time = helper.data_over_time(df, 'region')
    fig = px.line(nation_over_time, x='Edition', y='region', title="Participating Nations")
    st.plotly_chart(fig, use_container_width=True)

    event_over_time = helper.data_over_time(df, 'Event')
    fig1 = px.line(event_over_time, x='Edition', y='Event', title="Events Over Time")
    st.plotly_chart(fig1, use_container_width=True)

    athletes_over_time = helper.data_over_time(df, 'Name')
    fig2 = px.line(athletes_over_time, x='Edition', y='Name', title="Athletes Over Time")
    st.plotly_chart(fig2, use_container_width=True)

    st.subheader('🗺️ Events by Sport Over the Years')
    x = df.drop_duplicates(['Year', 'Event', 'Sport'])
    figg, ax = plt.subplots(figsize=(18, 14))
    sns.heatmap(
        x.pivot_table(index='Sport', columns='Year', values='Event', aggfunc='count').fillna(0).astype(int),
        annot=True,
        cmap='YlGnBu',
        linewidths=0.3,
        ax=ax
    )
    st.pyplot(figg)

    st.subheader("🏆 Most Successful Athletes")
    sport_list = df['Sport'].dropna().unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')
    sel_sport = st.selectbox('Select Sport', sport_list)
    top_athletes = helper.most_sucessful(df, sel_sport)
    st.table(top_athletes)

# --- Country-wise Analysis ---
if user_menu == 'Country-wise Analysis':
    st.sidebar.header("🌍 Select Country")
    country_list = df['region'].dropna().unique().tolist()
    country_list.sort()
    selected_country = st.sidebar.selectbox('Select Country', country_list)

    st.subheader(f"🎯 {selected_country} Medal Tally Over the Years")
    final_df = helper.yearwise_medal_tally(df, selected_country)
    fig = px.line(final_df, x='Year', y='Medal')
    st.plotly_chart(fig, use_container_width=True)

    st.subheader(f"🔥 {selected_country} Sport-wise Performance")
    pt = helper.country_event_heatmap(df, selected_country)
    figg, ax = plt.subplots(figsize=(18, 14))
    sns.heatmap(pt, annot=True, cmap='Blues', linewidths=0.3, ax=ax)
    st.pyplot(figg)

    st.subheader(f"🏅 Top Athletes from {selected_country}")
    top10_df = helper.most_successful_by_region(df, selected_country)
    st.table(top10_df)

# --- Athlete-wise Analysis ---
if user_menu == 'Athlete-wise Analysis':
    st.subheader('📊 Age Distribution of Athletes')
    athlete_df = df.drop_duplicates(subset=['Name', 'region'])

    x1 = athlete_df['Age'].dropna()
    x2 = athlete_df[athlete_df['Medal'] == 'Gold']['Age'].dropna()
    x3 = athlete_df[athlete_df['Medal'] == 'Silver']['Age'].dropna()
    x4 = athlete_df[athlete_df['Medal'] == 'Bronze']['Age'].dropna()

    fig = ff.create_distplot(
        [x1, x2, x3, x4],
        ['Overall Age', 'Gold', 'Silver', 'Bronze'],
        show_hist=False,
        show_rug=False
    )
    fig.update_layout(autosize=False, width=1000, height=600)
    st.plotly_chart(fig)

    st.subheader('🥇 Gold Medalist Age Distribution by Sport')
    fam_sports = df['Sport'].dropna().unique().tolist()
    x, name = [], []
    for sport in fam_sports:
        temp_df = athlete_df[athlete_df['Sport'] == sport]
        age_data = temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna()
        if len(age_data) > 1 and age_data.nunique() > 1:
            x.append(age_data)
            name.append(sport)
    if x:
        fig = ff.create_distplot(x, name, show_hist=False, show_rug=False)
        fig.update_layout(autosize=False, width=1000, height=600)
        st.plotly_chart(fig)
    else:
        st.warning("Not enough data to plot KDE distribution.")

    st.subheader('⚖️ Height vs Weight')
    sport_list = df['Sport'].dropna().unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')
    sel_sport = st.selectbox('Select Sport', sport_list)
    temp_df = helper.wt_vs_ht(df, sel_sport)

    fig, ax = plt.subplots()
    sns.scatterplot(
        data=temp_df,
        x='Weight', y='Height',
        hue='Medal', style='Sex', s=80, ax=ax
    )
    ax.set_title(f"{sel_sport} - Height vs Weight", fontsize=14)
    st.pyplot(fig)

    st.subheader('👥 Gender Participation Over the Years')
    final_df = helper.men_vs_women(df)
    fig = px.line(final_df, x='Year', y=['Male', 'Female'])
    fig.update_layout(autosize=False, width=1000, height=600)
    st.plotly_chart(fig)
