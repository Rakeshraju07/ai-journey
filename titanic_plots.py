import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")
df["Age"] = df["Age"].fillna(df["Age"].median())

# Chart 1: survival rate by sex
plt.figure()
df.groupby("Sex")["Survived"].mean().plot(kind="bar")
plt.title("Survival rate by sex")
plt.xlabel("Sex")
plt.ylabel("Survival rate")
plt.savefig("survival_by_sex.png")
plt.show()

# Chart 2: survival rate by class
plt.figure()
df.groupby("Pclass")["Survived"].mean().plot(kind="bar")
plt.title("Survival rate by class")
plt.xlabel("Passenger class (1 = first)")
plt.ylabel("Survival rate")
plt.savefig("survival_by_class.png")
plt.show()

# Chart 3: age distribution
plt.figure()
df["Age"].plot(kind="hist", bins=20)
plt.title("Age distribution of passengers")
plt.xlabel("Age")
plt.ylabel("Number of passengers")
plt.savefig("age_histogram.png")
plt.show()