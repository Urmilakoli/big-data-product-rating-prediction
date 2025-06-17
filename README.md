# Big Data Product Rating Prediction

## Student: Urmila Koli  
**University**: Berlin School of Business & Innovation  
**Programme**: MSc Data Analytics

### 📌 Project Summary
This project builds an end-to-end Big Data pipeline using Hadoop, Spark, Hive, and MLlib to predict product ratings from the Amazon Product Reviews 2023 dataset (>5GB). The goal is to improve product recommendation systems using machine learning.

### 🛠️ Technologies Used
- Hadoop (HDFS)
- Apache Spark (PySpark)
- Hive (HiveQL)
- MLlib (Random Forest)
- Docker

### 📂 Project Structure
```
big-data-product-rating-prediction/
├── README.md
├── docker-setup/
│   └── docker-compose.yml
├── data/
│   └── amazon_reviews_2023.csv (not included)
├── notebooks/
│   └── spark_cleaning_analysis.ipynb
├── hive/
│   └── create_tables.hql
├── ml/
│   └── random_forest_model.py
├── requirements.txt
└── LICENSE
```

### 📈 Outcome
The trained Random Forest model predicts ratings based on review features, offering data-driven insights for e-commerce product recommendations.
