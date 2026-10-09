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