import numpy as np

def fetch_medal_tally(df, year, country):
    medal_df = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    flag = 0
    temp_df = medal_df.copy()

    # Filtering based on the selected year and country
    if year == 'Overall' and country == 'Overall':
        pass  # no filtering

    elif year == 'Overall' and country != 'Overall':
        flag = 1
        temp_df = temp_df[temp_df['region'] == country]

    elif year != 'Overall' and country == 'Overall':
        temp_df = temp_df[temp_df['Year'] == int(year)]

    else:
        temp_df = temp_df[(temp_df['region'] == country) & (temp_df['Year'] == int(year))]

    # Grouping
    if flag == 1:
        x = temp_df.groupby('Year')[['Gold', 'Silver', 'Bronze']].sum().sort_values('Year').reset_index()
    else:
        x = temp_df.groupby('region')[['Gold', 'Silver', 'Bronze']].sum().sort_values('Gold', ascending=False).reset_index()

    # Total medals
    x['Total'] = x['Gold'] + x['Silver'] + x['Bronze']

    return x




def medal_tally(df):
    # Remove duplicate medals per team/event combination
    df = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])

    # Group by region and sum the medal counts
    medal_tally_df = df.groupby('region')[['Gold', 'Silver', 'Bronze']].sum().sort_values('Gold', ascending=False).reset_index()

    # Fill NaN with 0 (in case there were missing medals)
    medal_tally_df[['Gold', 'Silver', 'Bronze']] = medal_tally_df[['Gold', 'Silver', 'Bronze']].fillna(0).astype(int)

    # Calculate total medals
    medal_tally_df['Total'] = medal_tally_df['Gold'] + medal_tally_df['Silver'] + medal_tally_df['Bronze']

    return medal_tally_df


def country_year_list(df):
    years = df['Year'].dropna().unique().tolist()
    years = sorted([int(year) for year in years])
    years.insert(0, 'Overall')  # fix typo from 'OverAll'

    countries = np.unique(df['region'].dropna().values).tolist()
    countries.sort()
    countries.insert(0, 'Overall')  # fix typo from 'OverAll'

    return years, countries

def data_over_time(df,col):
    data_over_time = df.drop_duplicates(['Year', col])['Year'].value_counts().reset_index().sort_values('Year')
    data_over_time.rename(columns={'Year': 'Edition', 'count': col}, inplace=True)
    return data_over_time


def most_sucessful(df, sport):
    temp_df = df.dropna(subset=['Medal'])

    if sport != 'Overall':
        temp_df = temp_df[temp_df['Sport'] == sport]

    # Count medals per athlete
    medal_count = temp_df['Name'].value_counts().reset_index()
    medal_count.columns = ['Name', 'Medals']

    # Merge to get Sport and Region
    x = medal_count.merge(df[['Name', 'Sport', 'region']], on='Name', how='left') \
                   .drop_duplicates('Name')

    return x


def yearwise_medal_tally(df,country):
    temp_df = df.dropna(subset=['Medal'])
    temp_df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'], inplace=True)
    new_df = temp_df[temp_df['region'] == country]
    final_df = new_df.groupby('Year').count()['Medal'].reset_index()

    return final_df

def country_event_heatmap(df,country):
    temp_df = df.dropna(subset=['Medal'])
    temp_df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'], inplace=True)
    new_df = temp_df[temp_df['region'] == country]
    pt=new_df.pivot_table(index='Sport', columns='Year', values='Medal', aggfunc='count').fillna(0).astype('int')
    return pt

def most_successful_by_region(df, region):
    # Filter for medal winners only
    temp_df = df.dropna(subset=['Medal'])

    # Filter for selected region
    temp_df = temp_df[temp_df['region'] == region]

    # Count medals per athlete
    medal_count = temp_df['Name'].value_counts().reset_index()
    medal_count.columns = ['Name', 'Medals']

    # Merge to get Sport and Region, then remove duplicates
    x = medal_count.merge(df[['Name', 'Sport', 'region']], on='Name', how='left') \
                   .drop_duplicates('Name') \
                   .head(10)

    return x

def wt_vs_ht(df,sport):
    athlete_df = df.drop_duplicates(subset=['Name', 'region'])
    athlete_df['Medal'].fillna('No Medal', inplace=True)
    if sport != 'Overall':
        temp_df = athlete_df[athlete_df['Sport'] == sport]
        return temp_df
    else:
        return athlete_df

def men_vs_women(df):
    athlete_df = df.drop_duplicates(subset=['Name', 'region'])
    men=athlete_df[athlete_df['Sex']=='M'].groupby(['Year']).count()['Name'].reset_index()
    women = athlete_df[athlete_df['Sex'] == 'F'].groupby(['Year']).count()['Name'].reset_index()

    final=men.merge(women,on='Year',how='left')
    final.rename(columns={'Name_x':'Male','Name_y':'Female'}, inplace=True)

    final.fillna(0,inplace=True)
    return final