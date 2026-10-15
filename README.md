# 📊 Streamlit Sales Dashboard

An interactive sales dashboard I built at Future Connect Training & Recruitment. Upload an Excel workbook and it cleans the data, calculates profit, and shows KPIs and Plotly charts for trends, categories, products, countries, and sales reps.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat-square&logo=plotly&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white)

<!-- Add a screenshot: ![Dashboard](screenshots/dashboard.png) -->

## ✨ Features
- 📤 Excel upload (`.xlsx`) straight from the browser
- 🧹 Cleaning: parses dates, drops incomplete rows, adds Month-Year and Profit columns
- 🔢 KPI cards: total sales, cost, profit (in £ millions), and units sold
- 📈 Sales, cost, and profit trend by month
- 📊 Top categories, top 10 subcategories, top 10 products, sales by country, and top 10 sales reps

## 🗂️ Expected data
The workbook needs a sheet named **Data** with these columns:

`Date`, `Sales`, `Cost`, `Units sold`, `Category`, `Subcategory`, `Product`, `Country`, `Salesrep`

The original company dataset isn't included.

## 🚀 Run locally

```bash
git clone https://github.com/ziauldin/streamlit-sales-dashboard.git
cd streamlit-sales-dashboard
pip install -r requirements.txt
streamlit run app.py
```

Open http://localhost:8501 and upload your workbook.

## 🛠️ Tech stack
Python · Streamlit · pandas · Plotly Express · openpyxl
