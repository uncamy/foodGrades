import pandas as pd

grades = pd.read_csv('LargeDatasets/WebExtract.txt')

#boro codes (from dataset) 1- Manhattan 2- Bronx 3- BRK 4-Queens 4- SI
manhattan = grades[grades['BORO']== 1]

# keep only zipcode, cuisine, violation, score, grade, grade date
df = manhattan[['ZIPCODE', 'CUISINECODE', 'VIOLCODE',\
                'SCORE', 'CURRENTGRADE', 'GRADEDATE']]
#save to file
df.to_csv('manhattan_grades.csv')

#creating a new dataset for scores
scores = grades[['ZIPCODE', 'SCORE']]
missing = scores[scores.ZIPCODE > 1]

mean_score= scores.groupby('ZIPCODE').mean()

missing1  = mean_score.dropna(how='any')
final_means  = missing1[missing1.index != 'N/A']

final_means.to_json('NYC_mean_scores.json')
