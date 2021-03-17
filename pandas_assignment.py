import pandas as pd
import random

# Create a Series from the list [7, 11, 13, 17].
new_list = [7, 11, 13, 17]

pandas_list = pd.Series(new_list)
print(pandas_list)


# Create a Series with five elements that are all 100.0.
print()
hundred_series = pd.Series(100.0, range(5))

print(hundred_series)


# Create a Series with 20 elements that are all random numbers in the range 0 to 100.
# Use method describe to produce the Series’ basic descriptive statistics.
print()
random_series = pd.Series(random.randint(0, 99), range(20))

print(random_series.describe())

# Create a Series called temperatures of the floating-point values 98.6, 98.9, 100.2 and 97.9.
# Using the index keyword argument, specify the custom indices 'Julie', 'Charlie', 'Sam' and 'Andrea'.

print()
temperatures = pd.Series([98.6, 98.9, 100.2, 97.9])
temperatures.index = ["Julie", "Charlie", "Sam", "Andrea"]

print(temperatures)

# Form a dictionary from the names and values in Part (4), then use it to initialize a Series.
series_dict = {}

series_dict = 