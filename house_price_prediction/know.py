import pandas as pd

data = pd.read_csv("C:\\Users\\admin\\Desktop\\journey\\datasets\\train.csv")
df = pd.DataFrame(data)
pd.set_option("display.max_columns", None)

print(df[["OverallQual", "GrLivArea", "GarageCars", "GarageArea", "TotalBsmtSF", "1stFlrSF", "FullBath", "TotRmsAbvGrd", "YearBuilt", "YearRemodAdd"]].describe())

"""
----------------------------------------------
# information --
Data columns (total 10 columns):
 #   Column        Non-Null Count  Dtype
---  ------        --------------  -----
 0   OverallQual   1460 non-null   int64
 1   GrLivArea     1460 non-null   int64
 2   GarageCars    1460 non-null   int64
 3   GarageArea    1460 non-null   int64
 4   TotalBsmtSF   1460 non-null   int64
 5   1stFlrSF      1460 non-null   int64
 6   FullBath      1460 non-null   int64
 7   TotRmsAbvGrd  1460 non-null   int64
 8   YearBuilt     1460 non-null   int64
 9   YearRemodAdd  1460 non-null   int64
dtypes: int64(10)
------------------------------------------------
#Description --
       OverallQual    GrLivArea   GarageCars   GarageArea  TotalBsmtSF  
count  1460.000000  1460.000000  1460.000000  1460.000000  1460.000000   
mean      6.099315  1515.463699     1.767123   472.980137  1057.429452   
std       1.382997   525.480383     0.747315   213.804841   438.705324   
min       1.000000   334.000000     0.000000     0.000000     0.000000   
25%       5.000000  1129.500000     1.000000   334.500000   795.750000   
50%       6.000000  1464.000000     2.000000   480.000000   991.500000   
75%       7.000000  1776.750000     2.000000   576.000000  1298.250000   
max      10.000000  5642.000000     4.000000  1418.000000  6110.000000   

          1stFlrSF     FullBath  TotRmsAbvGrd    YearBuilt  YearRemodAdd  
count  1460.000000  1460.000000   1460.000000  1460.000000   1460.000000  
mean   1162.626712     1.565068      6.517808  1971.267808   1984.865753  
std     386.587738     0.550916      1.625393    30.202904     20.645407  
min     334.000000     0.000000      2.000000  1872.000000   1950.000000  
25%     882.000000     1.000000      5.000000  1954.000000   1967.000000  
50%    1087.000000     2.000000      6.000000  1973.000000   1994.000000  
75%    1391.250000     2.000000      7.000000  2000.000000   2004.000000  
max    4692.000000     3.000000     14.000000  2010.000000   2010.000000  
"""