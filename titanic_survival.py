import pandas as pd
df = pd.read_csv('titanic.csv')
df['Age']=df['Age'].fillna(df['Age'].median())
df['Embarked']=df['Embarked'].fillna(df['Embarked'].mode()[0])
print(df.isnull().sum())  # count of missing values in each column after filling
print(df['Survived'].mean()*100)  # average survival rate as a percentage 38% on an average survived
#Did women survived more thanmen?
print(df.groupby("Sex")['Survived'].mean()) #About 74% of women survived while only 19% of men survived
#Survival rate by passenger class
print(df.groupby("Pclass")['Survived'].mean()) #About 63% of first class passengers survived, 47% of second class passengers survived and only 24% of third class passengers survived
#Average age of survivours and non-survivours
print(df.groupby("Survived")['Age'].mean()) #Average age of survivors is about 28 years while the average age of non-survivors is about 30 years
#Average fare in each class
print(df.groupby("Pclass")['Fare'].mean()) #Average fare for first class passengers is about 84, for second class passengers is about 20 and for third class passengers is about 13