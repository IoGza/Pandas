import pandas as pd

grades = pd.Series([87, 100, 94])

print(grades)

grades = pd.Series(98.6, range(3))

print(grades)

a = grades[0]

# Calling series method describe produces all these stats
print(grades.describe())

grades = pd.Series([87, 100, 84], index=["Wally", "Eva", "Sam"])

print(grades)

grades = pd.Series({"Wally": 87, "Eva": 100, "Sam": 94})

print(grades["Eva"])


print(grades.Wally)

# Returns underlying array's element type
grades.dtype

# Returns values of array
grades.values