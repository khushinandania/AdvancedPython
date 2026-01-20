import pandas as pd
import numpy as np
 
 
##load csv file using pandas
df = pd.read_csv("/home/khushi/Desktop/khushi_module/users_raw.csv")
 
# Age group
age_bins = [0, 25, 35, 50, np.inf]
age_labels = ['18-25', '26-35', '36-50', '50+']
df['age_group'] = pd.cut(df['age'], bins=age_bins, labels=age_labels)
 
#income category
income_bins = [df['monthly_income'].min()-1,
               df['monthly_income'].quantile(0.33),
               df['monthly_income'].quantile(0.66),
               df['monthly_income'].max()+1]
income_labels = ['Low', 'Medium', 'High']
df['income_category'] = pd.cut(df['monthly_income'], bins=income_bins, labels=income_labels)
 
df = df.drop(columns=['Unnamed: 0'])
 
 
df.to_csv('/home/khushi/Desktop/khushi_module/clean_users.csv',index=False)
 