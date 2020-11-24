import pandas as pd
pd.set_option('display.max_colwidth', -1)

jeopardy = pd.read_csv('jeopardy.csv')

print(jeopardy.head())


King_England = jeopardy[(jeopardy[' Question'].str.contains("King")) & (jeopardy[' Question'].str.contains("England"))]

print(King_England[' Question'].head(20))
