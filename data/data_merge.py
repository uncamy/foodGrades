import pandas as pd

geocodes = pd.read_csv('./geocoded_zips.csv')
manhattan = pd.read_csv('./manhattan_grades.csv')

geocodes.rename(columns = {'JURISDICTION NAME': 'ZIPCODE'}, inplace = True)

df = pd.merge(manhattan, geocodes, on = 'ZIPCODE')
df2 = df[(df['ZIPCODE'] < 10011)]


df2.to_csv('reduced_man_geocoded_zip.csv')
df.to_csv('all_man_geocoded.csv')
