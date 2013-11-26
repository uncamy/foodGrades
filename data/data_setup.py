import pandas as pd

grades = pd.read_csv('./original_data/WebExtract.txt')

#boro codes (from dataset) 1- Manhattan 2- Bronx 3- BRK 4-Queens 4- SI
manhattan = grades[grades['BORO']== 1]

# keep only zipcode, cuisine, violation, score, grade, grade date
df = manhattan[['ZIPCODE', 'CUISINECODE', 'VIOLCODE',\
                'SCORE', 'CURRENTGRADE', 'GRADEDATE']]
#save to file
df.to_csv('manhattan_grades.csv')
