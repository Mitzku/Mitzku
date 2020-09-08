import codecademylib3_seaborn
import pandas as pd
import glob

student_files = glob.glob("exams*.csv")

df_list = []
for filename in student_files:
  data = pd.read_csv(filename)
  df_list.append(data)

students = pd.concat(df_list)

print(students)
print(len(students))



students = pd.melt(frame=students, id_vars=['full_name','gender_age','grade'], value_vars=['fractions', 'probability'], value_name='score', var_name='exam')

print(students.exam.value_counts())


print(students)
duplicates = students.duplicated()
print(duplicates.value_counts())

students = students.drop_duplicates()
duplicates = students.duplicated()
print(duplicates.value_counts())


print(students.gender_age.head())

students['gender'] = students['gender_age'].str[:1]
students['age'] = students['gender_age'].str[1:]

print(students.head())



print(students.gender_age.head())

students['gender'] = students['gender_age'].str[:1]
students['age'] = students['gender_age'].str[1:]

students = students.drop(columns='gender_age')
print(students.head())


# String Parsing

name_split = students['full_name'].str.split(' ')

print(name_split.head())

students['first_name'] = name_split.str.get(0)
students['last_name'] = name_split.str.get(1)

print(students.head())


print(students.dtypes)

students.score = students.score.replace('[\%]', '', regex=True)
students.score = pd.to_numeric(students.score)
print(students.head())




print(students.grade.head(5))

split = students.grade.str.split('(\d+)', expand=True)
students.grade = pd.to_numeric(split[1])

print(students.dtypes)

avg_grade = students.grade.mean()

print(avg_grade)


# Missing Values


score_mean = students.score.mean()
print(score_mean)

students.score = students.score.fillna(value=0)

score_mean_2 = students.score.mean()

print(score_mean_2)

