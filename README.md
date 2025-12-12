# 🎬 Movie Analytics Python Project

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![pandas](https://img.shields.io/badge/pandas-latest-green.svg)
![matplotlib](https://img.shields.io/badge/matplotlib-latest-orange.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 📊 Project Overview

A comprehensive movie data analysis project using Python to explore trends in the film industry. This project analyzes movie production patterns, box office revenues, ratings, budget-revenue relationships, genre profitability, and director performance using advanced data analysis and visualization techniques.

## 🎯 Key Features

- **Data Cleaning & Preparation**: Robust handling of missing values, data type conversions, and data quality checks
- **Exploratory Data Analysis**: Statistical summaries and data quality assessments
- **Trend Analysis**: Time series analysis of movie production, box office revenue, and ratings over time
- **Financial Analysis**: Budget vs. revenue correlation and ROI (Return on Investment) calculations
- **Genre Analysis**: Performance metrics and profitability analysis across different genres
- **Director Performance**: Evaluation of directors based on ratings, box office success, and consistency
- **Interactive Visualizations**: Dynamic charts using Plotly, Matplotlib, and Seaborn

## 🛠️ Technologies Used

- **Python 3.8+**
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computations
- **matplotlib**: Static visualizations
- **seaborn**: Statistical data visualization
- **plotly**: Interactive visualizations

## 📁 Project Structure

```
movie-analytics-python-project/
│
├── movie_analytics_analysis.py    # Main analysis script
├── README.md                       # Project documentation
├── LICENSE                         # MIT License
└── .gitignore                      # Git ignore file
```

## 🚀 Getting Started

### Prerequisites

```bash
python >= 3.8
pandas
numpy
matplotlib
seaborn
plotly
```

### Installation

1. Clone the repository:
```bash
git clone https://github.com/NAING-LINNOO/movie-analytics-python-project.git
cd movie-analytics-python-project
```

2. Install required packages:
```bash
pip install pandas numpy matplotlib seaborn plotly
```

3. Run the analysis:
```bash
python movie_analytics_analysis.py
```

## 📈 Analysis Sections

### 1. Data Inspection & Cleaning
- Initial data exploration using `.info()`, `.describe()`, `.head()`
- Missing value analysis and imputation strategies
- Data type conversions and validation
- Duplicate removal

### 2. Feature Engineering
- **Profit Calculation**: `GlobalBoxOfficeUSD - BudgetUSD`
- **ROI Calculation**: `(Profit / BudgetUSD) * 100`
- Date parsing and temporal feature extraction

### 3. Trend Analysis
- Movie production trends over years
- Box office revenue patterns
- Average rating evolution
- Interactive time series visualizations

### 4. Budget-Revenue Relationship
- Correlation analysis between budget and revenue
- Scatter plots with trend lines
- Profitability assessment by budget range

### 5. Genre Performance
- Top-grossing genres by total profit
- Genre-wise ROI comparison
- Movies produced per genre
- Interactive bar charts and heatmaps

### 6. Director Analysis
- Best directors by average IMDb rating
- Most commercially successful directors
- Director consistency analysis (minimum 3 films)
- Performance metrics visualization

## 📊 Sample Visualizations

The project generates multiple visualizations including:
- Time series line plots for production trends
- Bar charts for genre comparison
- Scatter plots for budget-revenue relationships
- Interactive Plotly charts for deeper exploration

## 💡 Key Insights

This analysis helps answer questions such as:
- How has movie production evolved over time?
- What is the relationship between budget and box office success?
- Which genres are most profitable?
- Who are the most successful directors by different metrics?
- How do ratings correlate with commercial success?

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/NAING-LINNOO/movie-analytics-python-project/issues).

## 📝 License

This project is [MIT](LICENSE) licensed.

## 👤 Author

**Naing Linn Oo**
- GitHub: [@NAING-LINNOO](https://github.com/NAING-LINNOO)

## ⭐ Show your support

Give a ⭐️ if this project helped you!

---

*This project demonstrates data analysis skills using Python for portfolio purposes. The analysis techniques and visualizations can be adapted for various data analysis projects.*
