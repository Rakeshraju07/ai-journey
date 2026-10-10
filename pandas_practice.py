import pandas as pd
df =pd.read_csv('titanic.csv')
print(df.head())     # first 5 rows
print(df.shape)      # (rows, columns)
print(df.columns)    # column names
print(df.info())      # data types and non-null counts
print(df.describe())  # summary statistics for numerical columns
print(df['Age'].head())  # first 5 values of the 'Age' column
print(df[["Name","Age"]].head()) #double brackets to select multiple columns
print(df[df['Age']>60].head())  # filter rows where Age is greater than 60 we use two df inner df returns a boolean used to filter the outer df returns the columns
print(df[df["Sex"] == "female"].shape)   # how many women? we use shape to get the number of rows and columns
# combining conditions: use & and wrap each in parentheses
print(df[(df["Sex"] == "female") & (df["Pclass"] == 1)].shape) # how many women in first class?
print(df[df['Survived']==1].shape)  # how many survived?
print(df[(df["Sex"]== "male") & (df["Age"]<18)].shape)  # how many males under 18?
print(df[(df["Sex"] == "female") & (df["Survived"] == 1)]["Age"].mean()) # average age of women who survived 
print(df.groupby("Sex")['Survived'].count())
print(df.groupby("Sex")['Survived'].mean())  # average survival rate by sex
print(df.groupby("Sex")['Survived'].max())  # maximum survival rate by sex
print(df.groupby("Sex")['Survived'].sum())  # total number of survivors by sex
print(df.groupby("Pclass")['Survived'].mean())  # average survival rate by passenger class
print(df.groupby("Pclass")['Fare'].mean())  # average fare by passenger class
print(df.info())  # data types and non-null counts
print(df.isnull().sum())  # count of missing values in each column
df['Age'] = df['Age'].fillna(df['Age'].median())  # fill missing Age values with the median age
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])  # fill missing Embarked values with the most common value
print(df.isnull().sum())  # count of missing values in each column after filling