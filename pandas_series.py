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


# Series of strings
hardware = pd.Series(["Hammer", "Saw", "Wrench"])
print(hardware)

# Calling string methods apply to each element
# checks if letter a exists in string element
print(hardware.str.contains("a"))

hardware_upper = hardware.str.upper()

print(hardware_upper)
