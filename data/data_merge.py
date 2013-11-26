import pandas as pd

geocodes = pd.read_csv('./geocoded_zips.csv')
manhattan = pd.read_csv('./manhattan_grades.csv')

geocodes.rename(columns = {'JURISDICTION NAME': 'ZIPCODE'}, inplace = True)

test= pd.merge(manhattan, geocodes, on = 'ZIPCODE')
