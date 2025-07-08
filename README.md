# 🏅 Olympics Analysis Dashboard

An interactive data visualization web application built with **Streamlit** that provides deep insights into historical **Olympic Games** data — including medal tallies, participation trends, country-wise performance, and athlete-level analysis.

![App Screenshot](./853b09cb-f065-418c-9677-804b9605c782.png)

## 📁 Project Structure

```
├── app.py                # Main Streamlit app
├── helper.py            # Utility functions for analysis
├── preprocessor.py      # Data cleaning and merging
├── athlete_events.csv   # Athlete historical Olympic data
├── noc_regions.csv      # Country/NOC mappings
└── README.md            # Project overview and instructions
```

## 🚀 Features

### 📊 Overall Analysis
- Editions, hosts, sports, events, athletes, and nations count
- Time-series plots for participation trends
- Heatmap of events per sport
- Most successful athletes by sport

### 🏅 Medal Tally
- Medal table by country and year
- Filterable by specific year or country
- Highlights top performers

### 🌍 Country-wise Analysis
- Year-wise medal trends for each country
- Heatmap of sport-wise performance
- Top athletes from selected country

### 🧍 Athlete-wise Analysis
- Age distribution of medalists
- Gold medalist age distribution by sport
- Gender participation trends
- Height vs Weight analysis by sport and gender

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **Streamlit**
- **Plotly**
- **Seaborn**
- **Matplotlib**

## 📦 Datasets Used

- [`athlete_events.csv`](https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results)
- [`noc_regions.csv`](https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results)

## ▶️ How to Run Locally

1. **Clone the repository**

```bash
git clone https://github.com/your-username/olympics-analysis.git
cd olympics-analysis
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the app**

```bash
streamlit run app.py
```

> Make sure the CSV files are in the same directory as `app.py`.

## 📝 To Do

- Add Winter Olympics support
- Improve mobile responsiveness
- Deploy using Streamlit Cloud / Render

## 📬 Contact

Have questions, suggestions or want to collaborate?

📧 tanishakbansal07@gmail.com  
🔗 [LinkedIn](www.linkedin.com/in/tanishak-bansal007)  
🐙 [GitHub](https://github.com/tanishak0000007777)
