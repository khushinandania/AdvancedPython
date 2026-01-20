import pandas as pd
import numpy as np
 
 
#load csv file using pandas
df = pd.read_csv("/home/khushi/Desktop/khushi_module/users_raw.csv")
df.info()
print()
 
 
#validate age
df['valid_age'] = df['age'].between(1,100)
df.loc[df['valid_age'] == False , 'age'] = np.nan
 
 
#validate mail
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
df['valid_mail'] = df['email'].str.match(pattern, case=False, na=False)
df.loc[df['valid_mail'] == False , 'email'] = np.nan
 
 
#non null names
df['name'] = df['name'].combine_first(
    df['email']
      .str.split('@').str[0]
      .str.replace('.', ' ', regex=False)
      .str.replace('_', ' ', regex=False)
      .str.title()
)
df['name'] = df['name'].fillna('Unknown')
 
 
#valid dates
df["date_valid"] = pd.to_datetime(
    df["signup_date"], errors="coerce"
).notnull()
 
print("---------")
invalid_rows = df[~df["date_valid"]]
print(invalid_rows)
print("----------")
 
df.drop(columns=['valid_age', 'valid_mail', 'date_valid'], inplace=True)
 
df.to_csv('/home/khushi/Desktop/khushi_module/users_raw.csv')
 
 
df.info()