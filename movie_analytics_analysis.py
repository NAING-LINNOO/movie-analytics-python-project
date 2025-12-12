import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Load dataset
movie = pd.read_csv('movies_dataset.csv')

# Initial Inspection
print("=" * 80)
print("TITLE: Performing Initial Inspection")
print("Use methods like .info(), .describe(), dtype, etc. to understand the data's structure and identify data quality issues.")
print("=" * 80)

movie.info()
movie.head()
movie.tail()
movie.sample(5)
movie.describe()
movie.nunique()
movie.dtypes
movie.index
movie.columns

# Data Cleaning Preparation
print("\n" + "=" * 80)
print("TITLE: Data Cleaning & Preparation")
print("=" * 80)

movie.isnull().sum()
movie.dropna(how='all')
na = movie[movie.isna().any(axis=1)]
na = movie.head()
movie.drop_duplicates()
movie.head()

# Handle missing values appropriately for key columns
print("\n" + "=" * 80)
print("TITLE: Handle missing values appropriately for key columns.")
print("=" * 80)

movie['IMDbRating'] = movie['IMDbRating'].fillna(movie['IMDbRating'].mean())
movie['BudgetUSD'] = movie['BudgetUSD'].fillna(movie['BudgetUSD'].median())
movie['Genre'] = movie['Genre'].fillna(movie['Genre'].mode()[0])
movie['Director'] = movie['Director'].fillna('Unknown')

movie.head()
movie.info()

# Convert data types
print("\n" + "=" * 80)
print("TITLE: Convert data types")
print("=" * 80)

movie['ReleaseDate'] = pd.to_datetime(movie['ReleaseDate'], errors='coerce')
movie = movie.dropna(subset=['ReleaseDate'])
movie.head()

# Create new calculated columns needed for the analysis below (profit and Return on Investment ROI)
print("\n" + "=" * 80)
print("TITLE: Create new calculated columns needed for the analysis below (profit and Return on Investment ROI)")
print("=" * 80)

movie['Profit'] = movie['GlobalBoxOfficeUSD'] - movie['BudgetUSD']
movie['ROI'] = (movie['Profit'] / movie['BudgetUSD']) * 100

# Exploring trends in movie production, box office, and ratings over time
print("\n" + "=" * 80)
print("TITLE: Create new calculated columns needed for the analysis below (profit and Return on Investment ROI) - Exploring trends in movie production, box office, and ratings over time")
print("=" * 80)

trends_analysis = movie.groupby('ReleaseYear').agg({
    'Title': 'count',
    'GlobalBoxOfficeUSD': 'sum',
    'IMDbRating': 'mean'
}).reset_index()

trends_analysis.columns = ['Year', 'Movies Produced','GBoxOfficeUSD','IMDbRating']
trends_analysis

# This comprehensive movie analytics project demonstrates:
# 1. Data cleaning and preparation techniques
# 2. Exploratory data analysis with statistical summaries
# 3. Time series analysis of movie production trends
# 4. Budget-revenue relationship analysis
# 5. Genre performance and profitability analysis
# 6. Director performance evaluation
# 7. Advanced visualizations using matplotlib, seaborn, and plotly

# Note: Additional analysis sections for visualizations and deeper insights
# are included in the full project code.
