import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
file=pd.read_spss(r"C:\Users\USER\Videos\PYTHON ZERO TO HERO\project\Dat.sav")
df = pd.DataFrame(file)
print(df.columns)
print(df)

#1.Is there a favorite teacher of a particular ethnic?
#Group the data by 'Ethnic' and 'Teacher' and calculate the count of student for each combination
favourite_teacher = df.groupby(['Ethnic','Teacher'])['Student'].count().reset_index()
#Find the teacher with the highest count for each ethnic
favourite_teacher_by_ethnic = favourite_teacher.loc[favourite_teacher.groupby('Ethnic')['Student'].idxmax()]
print('1.favorite teacher of a particular ethnic')
print(favourite_teacher_by_ethnic)
#Visulization
plt.figure(figsize=(10,6))
sns.barplot(x='Teacher', y='Student',hue='Ethnic' ,data=favourite_teacher_by_ethnic)
plt.title('Favourite for Each Ethnic Group')
plt.xlabel('Favourite Teacher')
plt.ylabel('Number of Students')
plt.legend(title='Ethnic Group', loc='upper left')
plt.show()
print()

#2.Do students who get free lunch get higher grades than others?
#calculate the average score for each lunch program
average_score_paid_lunch = df[df['Freeredu']=='Paid lunch']['Score'].mean().round(2)
average_score_free_lunch = df[df['Freeredu']=='Free lunch']['Score'].mean().round(2)
average_scores_by_lunch = [average_score_paid_lunch, average_score_free_lunch]
print('2.Do students who get free lunch get higher grades than others?')
print(f'paid lunch={average_score_paid_lunch}', f'free lunch={average_score_free_lunch}')
#Visualization using matplotlib
#Data for the pie chart
average_scores_by_lunch = [average_score_paid_lunch, average_score_free_lunch]
lunch_programs = ['Paid lunch','Free lunch']
# Create pie chart
plt.figure(figsize=(8,6))
plt.pie(average_scores_by_lunch, labels=lunch_programs, autopct='%1.1f%%' ,startangle=90)
plt.title('Average Academic Score by Lunch Program')
plt.axis('equal') # Equal ratio ensures that the pie chart is circular.
plt.show()
print()

#3.Does one ethnic have more score than the other?
#Group the data by 'Ethnic' and 'Score' and calculate the average score for each ethnic group
average_score_by_ethnic = df.groupby('Ethnic')['Score'].mean().round(2)
print('3.Does one ethnic have more score than the other?')
print(average_score_by_ethnic)
#Visualization using seaborn
plt.figure(figsize=(10,6))
sns.boxplot(x='Ethnic', y='Score', data=df)
plt.xlabel('Ethnicity')
plt.ylabel('Academic Score')
plt.title('Ethnic Comparison of Academic Score')
plt.show()
print()

#4.Does any gender have a higher score than the other?
#Group the data by 'Gender' and 'Score' and calculate the average score each gender
average_score_by_gender = df.groupby('Gender')['Score'].mean().round(2)
print('4.Does any gender have a higher score than the other?')
print(average_score_by_gender)
#Visualization using seaborn
plt.figure(figsize=(8,6))
sns.boxplot(x='Gender', y='Score', data=df)
plt.xlabel('Gender')
plt.ylabel('Academic Score')
plt.title('Gender Comparison of Academic Score')
plt.show()
print()

#5.What is the average score for students in general?
#calulate the average score for student in general and group the data by 'Student' and 'Score'
overall_average_score = df['Score'].mean().round(2)
print('5.What is the average score for students in general?')
print(overall_average_score)


#6.How many students of each ethnic are in the dataset?
#count the number of student in each ethnic group
Ethnic_count = df['Ethnic'].value_counts()
print('6.How many students of each ethnic are in the dataset?')
print(Ethnic_count)
#Visualization
sns.countplot(x='Ethnic',data=df)
plt.xlabel('Ethnic Group')
plt.ylabel('Number of Students')
plt.title('Number of Student in each Ethnic Group')
plt.tight_layout()
plt.show()
print()

#7.What is the number of male and female students?
#count the number of male and female student in the dataset
Gender_count = df['Gender'].value_counts()
print('7.What is the number of male and female students?')
print(Gender_count)
#Visualization using seaborn
plt.figure(figsize=(6,6))
sns.countplot(x='Gender',data=df)
plt.xlabel('Gender')
plt.ylabel('Number of Students')
plt.title('Number of male and Female Students')
plt.tight_layout()
plt.show()
print()

#8.What is the average score for male and female?
#calculate the average score for male and female students
average_score_by_gender = df.groupby('Gender')['Score'].mean().round(2)
print('8.What is the average score for male and female?')
print(average_score_by_gender)
#Visualization using visualization
plt.figure(figsize=(8,6))
plt.pie(average_score_by_gender, labels=average_score_by_gender.index, autopct='%1.1f%%',startangle=90)
plt.title('Does any gender have a higher score than the other?\n\nAverage Score by Gender')
plt.axis('equal')
plt.show()
print()

#9.Who gives the best results with all students?
#calculate the average score for each teacher
average_score_by_teacher = df.groupby('Teacher')['Score'].mean().round(2)
print('9.Who gives the best results with all students?')
print(average_score_by_teacher)
best_teacher =average_score_by_teacher.idxmax()
#Visualization using Matplolib
#Data for the pie chart
average_score = average_score_by_teacher.values
teachers = average_score_by_teacher.index
#find the index of the best teacher in the teacher list
best_teacher_index = teachers.tolist().index(best_teacher)
#create the pie chart
plt.figure(figsize=(8,8))
colors=['skyblue' if i != best_teacher_index else 'limegreen' for i in range(len(average_score))]
explode = [0.1 if i==best_teacher_index else 0 for i in range(len(average_score))]
plt.pie(average_score, labels=teachers, colors=colors, explode=explode ,autopct='%1.1f%%', startangle=90)
plt.title('Teacher with Best Results')
plt.axis('equal') # equal ensure the pie chart is circular
plt.show()