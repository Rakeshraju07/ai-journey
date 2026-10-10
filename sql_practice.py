import sqlite3
import pandas as pd

df = pd.read_csv("titanic.csv")
conn = sqlite3.connect("titanic.db")
df.to_sql("passengers", conn, if_exists="replace", index=False)

def run(query):
    return pd.read_sql_query(query, conn)

print(run("SELECT Name, Age FROM passengers WHERE Age > 60"))
print(run("SELECT Name, Age FROM passengers ORDER BY Age DESC LIMIT 5"))
print(run("SELECT COUNT(*) FROM passengers"))
print(run("SELECT AVG(Age), MAX(Fare) FROM passengers"))
print(run("SELECT Name, Age FROM passengers WHERE Sex = 'female' AND Pclass = 1"))
print(run("SELECT COUNT(*) FROM passengers WHERE Survived = 1"))