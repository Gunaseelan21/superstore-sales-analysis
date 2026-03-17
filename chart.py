import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../dataset/Sample - Superstore.csv", encoding="latin1")

# Chart 1: Sales by Category
df.groupby("Category")["Sales"].sum().plot(kind="bar")
plt.title("Sales by Category")
plt.show()