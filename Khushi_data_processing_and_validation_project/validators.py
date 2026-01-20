import pandas as pd
 
#load csv file using pandas
df = pd.read_csv("/home/khushi/Desktop/khushi_module/users_raw.csv")
 
#replace invalid age with median
df['age'] = df['age'].fillna(df['age'].median())
 
#replace missing income values with mean
df['monthly_income'] = df['monthly_income'].fillna(df['monthly_income'].mean())
 
#replace missing city with mode
df['city'] = df['city'].fillna(df['city'].mode()[0])
 
#drop invalid email
df = df.dropna(subset=['email'])
 
df.to_csv('/home/khushi/Desktop/khushi_module/users_raw.csv')
 
 
df.info()
 