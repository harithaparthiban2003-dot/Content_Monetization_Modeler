# Content_Monetization_Modeler
Social Media Analytics 
📂 Dataset Information
Name: YouTube Monetization Modeler Dataset
Format: CSV
Rows: ~122,000
Type: Synthetic Dataset
📊 Features:
video_id
date
views, likes, comments
watch_time_minutes
video_length_minutes
subscribers
category, device, country
ad_revenue_usd (Target Variable)

🔍 Project Workflow
1. Data Preprocessing
Handled missing values (~5%)
Removed duplicates (~2%)
Encoded categorical variables
Converted date features (month, day)

2. Feature Engineering
Created engagement_rate:
engagement_rate = (likes + comments) / views

3. Exploratory Data Analysis
Correlation heatmap
Revenue distribution
Views vs Revenue relationship
Category-wise analysis

4. Model Building
Tested 5 regression models:
Linear Regression ✅
Decision Tree
Random Forest
Gradient Boosting
Support Vector Regressor
📈 Model Performance
Model	R² Score	MAE	RMSE
Linear Regression	0.9438	3.64	14.46
Gradient Boosting	0.9408	4.61	14.85
Random Forest	0.9394	4.51	15.01
Decision Tree	0.8823	6.97	20.93
SVR	0.1407	48.80	56.56
🏆 Best Model

Linear Regression was selected as the best model because it achieved:

Highest R² Score
Lowest RMSE
Lowest MAE
💡 Key Insights
Views and watch time strongly influence revenue
Engagement rate improves prediction accuracy
Subscriber count impacts revenue indirectly
Certain content categories perform better
🌐 Streamlit Application
Features:
User input for video metrics
Real-time revenue prediction
Dataset preview
Model performance display
▶️ How to Run the Project
1. Install Dependencies
pip install pandas numpy scikit-learn streamlit
2. Run the App
streamlit run app.py
📁 Project Structure
Content_Monetization_Modeler/
│── app.py
│── youtube_ad_revenue_dataset.csv
│── README.md
│── notebook.ipynb
📌 Business Use Cases
Content strategy optimization
Revenue forecasting
Creator analytics tools
Ad campaign planning
🚀 Future Improvements
Add deep learning models
Deploy app online (Streamlit Cloud)
Improve feature selection
Add real-time YouTube API integration
