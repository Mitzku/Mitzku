import pandas as pd
pd.set_option('display.max_colwidth', -1)

jeopardy = pd.read_csv('jeopardy.csv')

#The taks: /
Write a function that filters the dataset for questions that contains all of the words in a list of words. /
For example, when the list ["King", "England"] was passed to our function, the function returned a DataFrame of 152 rows. /
Every row had the strings "King" and "England" somewhere in its " Question".#

#boolean indexing works. Here I filter the jeopardy for only those entries where the column ' Question' contains 'King' and 'England'#

King_England = jeopardy[(jeopardy[' Question'].str.contains("King")) & (jeopardy[' Question'].str.contains("England"))]



#How can I write this as a function though?# 

#idea 1#

df = create_df()

def create_df(word1, word2):
    data = jeopardy[(jeopardy[' Question'].str.contains(word1) & (jeopardy[' Question'].str.contains(word2))]
    df = pd.DataFrame(data)
    return df

#idea 2 - I get stuck here and don't know how to return a dataframe / don't know how to print out the results using other words than King or England#
def filter_words(word1, word2):
    if row[' Question'] == word1 and row[' Question'] == word2:
        return False
    return row

King_England = jeopardy.apply(filter_words, axis=1, broadcast=True)

print(df("King", "England"))
