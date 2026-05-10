import streamlit as st
import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="Content Monetization Modeler",
    layout="wide"
)

st.title("📺 Content Monetization Modeler")
st.subheader("Predict YouTube Ad Revenue")

# =========================================
# LOAD DATA
# =========================================

df = pd.read_csv("youtube_ad_revenue_dataset.csv")

# =========================================
# PREPROCESSING
# =========================================

# Label Encoding
le = LabelEncoder()

cat_cols = ['video_id', 'category', 'device', 'country']

for col in cat_cols:
    df[col] = le.fit_transform(df[col])

# Convert date column
df['date'] = pd.to_datetime(df['date'])

# Feature Engineering
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day

# Drop original date column
df.drop("date", axis=1, inplace=True)

# Safe engagement rate calculation
df['engagement_rate'] = np.where(
    df['views'] == 0,
    0,
    (df['likes'] + df['comments']) / df['views']
)

# Fill missing values for all numeric columns
numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns

for col in numeric_columns:
    df[col] = df[col].fillna(df[col].median())

# =========================================
# MODEL BUILDING
# =========================================

X = df.drop("ad_revenue_usd", axis=1)
y = df["ad_revenue_usd"]

model = LinearRegression()
model.fit(X, y)

# =========================================
# SIDEBAR INPUT
# =========================================

st.sidebar.header("Enter Video Details")

video_id = st.sidebar.number_input(
    "Video ID",
    min_value=0,
    max_value=5000,
    value=100
)

views = st.sidebar.number_input(
    "Views",
    min_value=0,
    max_value=10000000,
    value=10000
)

likes = st.sidebar.number_input(
    "Likes",
    min_value=0,
    max_value=1000000,
    value=1000
)

comments = st.sidebar.number_input(
    "Comments",
    min_value=0,
    max_value=100000,
    value=100
)

watch_time_minutes = st.sidebar.number_input(
    "Watch Time Minutes",
    min_value=0,
    max_value=1000000,
    value=5000
)

video_length_minutes = st.sidebar.number_input(
    "Video Length (Minutes)",
    min_value=0.0,
    max_value=300.0,
    value=10.0
)

subscribers = st.sidebar.number_input(
    "Subscribers",
    min_value=0,
    max_value=10000000,
    value=100000
)

category = st.sidebar.number_input(
    "Category Encoded",
    min_value=0,
    max_value=20,
    value=1
)

device = st.sidebar.number_input(
    "Device Encoded",
    min_value=0,
    max_value=10,
    value=1
)

country = st.sidebar.number_input(
    "Country Encoded",
    min_value=0,
    max_value=20,
    value=1
)

month = st.sidebar.number_input(
    "Month",
    min_value=1,
    max_value=12,
    value=6
)

day = st.sidebar.number_input(
    "Day",
    min_value=1,
    max_value=31,
    value=15
)

# =========================================
# CALCULATE ENGAGEMENT RATE
# =========================================

engagement_rate = (
    (likes + comments) / views
    if views != 0 else 0
)

# =========================================
# INPUT DATAFRAME
# =========================================

input_data = pd.DataFrame({
    'video_id': [video_id],
    'views': [views],
    'likes': [likes],
    'comments': [comments],
    'watch_time_minutes': [watch_time_minutes],
    'video_length_minutes': [video_length_minutes],
    'subscribers': [subscribers],
    'category': [category],
    'device': [device],
    'country': [country],
    'month': [month],
    'day': [day],
    'engagement_rate': [engagement_rate]
})

# Match training column order exactly
input_data = input_data[X.columns]

# =========================================
# PREDICTION
# =========================================

if st.button("Predict Revenue"):
    prediction = model.predict(input_data)

    st.success(
        f"Predicted Ad Revenue: ${prediction[0]:.2f}"
    )

# =========================================
# DATASET PREVIEW
# =========================================

st.subheader("Dataset Preview")
st.dataframe(df.head())

# =========================================
# MODEL PERFORMANCE INFO
# =========================================

st.subheader("Best Model Information")

st.write("""
### Selected Model: Linear Regression

### Performance Metrics:

- R² Score: 0.9438
- MAE: 3.64
- RMSE: 14.46

### Why Linear Regression?

Linear Regression achieved the highest R² score
with the lowest MAE and RMSE compared to all
other regression models tested.

Therefore, it was selected as the final best model
for predicting YouTube ad revenue.
""")
