# Analysis of E-Commerce

## Project Overview
This project focuses on analyzing customer data from an E-commerce platform to understand churn patterns and customer behavior. Using machine learning algorithms like Decision Tree, Random Forest, and Extreme Boosting, we predict customer churn and provide insights into the factors influencing customer retention.

## Dataset
The dataset contains the following columns:
- **CustomerID**: Unique identifier for each customer
- **Churn**: Target variable indicating whether a customer has churned (1) or not (0)
- **Tenure**: Number of months the customer has been with the company
- **PreferredLoginDevice**: Device used by the customer to log in (e.g., mobile, desktop)
- **CityTier**: Tier of the city where the customer resides (e.g., 1, 2, 3)
- **WarehouseToHome**: Distance from the warehouse to the customer’s home (in miles)
- **PreferredPaymentMode**: Customer's preferred payment method (e.g., credit card, PayPal)
- **Gender**: Gender of the customer
- **HourSpendOnApp**: Average hours spent on the app per day
- **NumberOfDeviceRegistered**: Number of devices registered by the customer
- **PreferedOrderCat**: Preferred order category (e.g., electronics, clothing)
- **SatisfactionScore**: Customer satisfaction score (1-10)
- **MaritalStatus**: Marital status of the customer
- **NumberOfAddress**: Number of addresses registered by the customer
- **Complain**: Number of complaints registered by the customer
- **OrderAmountHikeFromlastYear**: Increase in order amount from the previous year
- **CouponUsed**: Number of coupons used by the customer
- **OrderCount**: Total number of orders placed by the customer
- **DaySinceLastOrder**: Days since the last order
- **CashbackAmount**: Total cashback amount received by the customer

## Project Structure
- **data/**: Contains the dataset used for analysis.
- **notebooks/**: Jupyter notebooks detailing the exploratory data analysis (EDA) and model training.
- **models/**: Saved models (Decision Tree, Random Forest, and Extreme Boosting).
- **templates/**: HTML templates for the Flask web interface.
- **static/**: CSS and JS files for styling and functionality.
- **app.py**: Flask application for deploying the model.
- **README.md**: Project overview and setup instructions.

## Model Training
Three machine learning models were implemented to predict customer churn:
1. **Decision Tree**: A tree-based model that makes decisions based on feature values, leading to a prediction for churn.
2. **Random Forest**: An ensemble model using multiple decision trees to improve prediction accuracy and reduce overfitting.
3. **Extreme Boosting (XGBoost)**: A boosting algorithm that combines weak learners to form a stronger predictive model, optimizing performance with accuracy and speed.

## Conclusion
The analysis of E-commerce customer data has revealed several important insights into customer churn behavior. Key factors influencing churn include **SatisfactionScore**, **OrderCount**, and **DaySinceLastOrder**. By leveraging machine learning models, particularly Extreme Boosting, we were able to predict customer churn with high accuracy. These insights can help E-commerce businesses develop targeted strategies to improve customer retention, such as enhancing satisfaction through personalized offers or re-engaging customers who haven't ordered recently. Overall, this project demonstrates the powerful role of data-driven decision-making in reducing churn and optimizing customer lifetime value.

