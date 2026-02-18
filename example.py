from minidf import read_csv
from minidf.stats import mean

# Load CSV
df = read_csv("data.csv")

print("First 5 rows:")
print(df.head())

# Select column
ages = df.select("age")

print("Average Age:", mean(ages))

# Filter
filtered = df.filter("city", "Mumbai")
print("Filtered Data:")
print(filtered)
