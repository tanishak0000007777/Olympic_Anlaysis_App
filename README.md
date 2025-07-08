🏅 Olympics Analysis Dashboard
An interactive data visualization web application built with Streamlit that provides deep insights into historical Olympic Games data — including medal tallies, participation trends, country-wise performance, and athlete-level analysis.


📁 Project Structure
bash
Copy
Edit
├── app.py                # Main Streamlit app
├── helper.py            # Utility functions for analysis
├── preprocessor.py      # Data cleaning and merging
├── athlete_events.csv   # Athlete historical Olympic data
├── noc_regions.csv      # Country/NOC mappings
└── README.md            # Project overview and instructions
🚀 Features
📊 Overall Analysis
Editions, hosts, sports, events, athletes, and nations count

Time-series plots for participation trends

Heatmap of events per sport

Most successful athletes by sport

🏅 Medal Tally
Medal table by country and year

Filterable by specific year or country

Highlights top performers

🌍 Country-wise Analysis
Year-wise medal trends for each country

Heatmap of sport-wise performance

Top athletes from selected country

🧍 Athlete-wise Analysis
Age distribution of medalists

Gold medalist age distribution by sport

Gender participation trends

Height vs Weight analysis by sport and gender

🛠️ Technologies Used
Python

Pandas

Streamlit

Plotly

Seaborn

Matplotlib

📦 Datasets Used
athlete_events.csv

noc_regions.csv

▶️ How to Run Locally
Clone the repository

bash
Copy
Edit
git clone https://github.com/your-username/olympics-analysis.git
cd olympics-analysis
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the app

bash
Copy
Edit
streamlit run app.py
Make sure the CSV files are in the same directory as app.py.

📝 To Do
Add Winter Olympics support

Improve mobile responsiveness

Deploy using Streamlit Cloud / Render

📸 Preview

📬 Contact
Have questions, suggestions or want to collaborate?

📧 [your-email@example.com]
🔗 LinkedIn
🐙 GitHub

