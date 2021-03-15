import pandas as pd

grades_dict = {
    "Wally": [87, 96, 70],
    "Eva": [100, 87, 90],
    "Sam": [94, 77, 90],
    "Katie": [100, 81, 82],
    "Bob": [83, 65, 85],
}

grades = pd.DataFrame(grades_dict)

# Gives row indeices names
grades.index = ["Test1", "Test2", "Test3"]
# print(grades)

# print(grades['Eva'])
# print()
# # prints an individual column using dot notation
# print(grades.Sam)
# print()

# using the loc and iloc methods
# loc method used the name of the row to index
# colon method works for consecutive columns
# print(grades.loc[:'Test2'])
print()

# iloc is zero based integer indexing, so 1 would represent the second row
# print(grades.iloc[0:2])

# for non-consecutive rowsprint(grades.loc[:'Test2'])
# print(grades.loc[["Test1", "Test3"]])

# print(grades.iloc[[0, 2]])

# View only Eva's and Katies grades for Test1 and Test2
print(grades.loc[:"Test2", ["Eva", "Katie"]])

# View only sam and katie's grades for test1 and test3
print(grades.loc[["Test1", "Test3"], "Sam":"Katie"])

grade_90 = grades[grades >= 90]
print(grade_90)

# create a dataframe for everyone with a B grade
b_grade = grades[(grades >= 80) & (grades < 90)]
print(b_grade)

# create a dataframe for everyone with A or B grade
grades_a_or_b = grades[(grades >= 90) | (grades >= 80)]
print(grades_a_or_b)

print()

pd.set_option("precision", 2)

# By student
print(grades.describe())

# By test
print(grades.T.describe())