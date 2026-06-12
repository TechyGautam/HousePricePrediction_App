
import pandas as pd 
from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
import streamlit as st
import joblib


pd.set_option('display.max_rows', None)

data = pd.read_csv("C:\\Users\\admin\\Desktop\\journey\\ml\\projects\\house_price_prediction\\data\\train.csv")
df = pd.DataFrame(data)

# model = LinearRegression()
model2 = RandomForestRegressor(n_estimators=100, max_depth=6,random_state=42)
scaler = StandardScaler()
# print(data.head())
# print("data shape: ", data.shape)
# print("data columns: ", data.columns)
# print("data description: ", data.describe())
# print("data info: ", data.info())
# print("Percentage of missing values: ",df.isnull().mean()*100)
# print("Percentage of missing values: ",df.isnull().mean()*100)
# print(df["MasVnrType"].value_counts(dropna=False))
# corr = df.corr(
#     numeric_only=True
# )

# print(
#     corr["SalePrice"]
#     .sort_values(
#         ascending=False
#     )
# )   
df.drop(
    columns=[
        "PoolQC",
        "MiscFeature",
        "Alley",
        "Fence",
        "MasVnrType",
        "BsmtFinSF2",      
        "BsmtHalfBath",   
        "MiscVal",         
        "Id",              
        "LowQualFinSF",    
        "YrSold",          
        "OverallCond",     
        "MSSubClass",      
        "EnclosedPorch",   
        "KitchenAbvGr" 
    ],
    inplace=True
)

X = df[
[
"OverallQual",
"GrLivArea",
"GarageCars",
"GarageArea",
"TotalBsmtSF",
"1stFlrSF",
"FullBath",
"TotRmsAbvGrd",
"YearBuilt",
"YearRemodAdd"
]
]

y = df["SalePrice"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# model.fit(X_train_scaled, y_train)
# score = model.score(X_test_scaled, y_test)
# print("R^2 Score: ", score)

model2.fit(X_train_scaled, y_train)
score1 = model2.score(X_train_scaled, y_train)
print("R^2 Score (Train): ", score1)
score2 = model2.score(X_test_scaled, y_test)
print("R^2 Score (Random Forest)(test): ", score2)


# Saving the model and scaler
joblib.dump(model2, "house_price_model_rf.pkl")
joblib.dump(scaler, "house_price_scaler.pkl")

