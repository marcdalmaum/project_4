# Import pandas
import pandas as pd

# Import CSV
df = pd.read_csv ('The-Office-Lines.csv')

# Clean CSV
df.drop('Unnamed: 6', axis = 1, inplace = True) 
df["speaker"]=df["speaker"].str.lower().str.replace(':','').str.strip().str.title()

# Save new CSV
df.to_csv('the_office_clean.csv', index=False)