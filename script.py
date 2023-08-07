last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Current Semester Classes

subjects = ["physics", "calculus", "poetry", "history"]

grades = [98, 97, 85, 88]

gradebook = [["physics", 98],["calculus", 97], ["poetry", 85], ["history", 88]]

#print(gradebook)

#Your grade for your computer science class just came in! You got a perfect score, 100!
gradebook.append(["computer science", 100])

#print(gradebook)

# Your grade for "visual arts" just came in! You got a 93!
gradebook.append(["visual arts", 93])

# Our instructor just told us they made a mistake grading and are rewarding an extra 5 points for our visual arts class.
gradebook[-1] = ["visual arts", 98]

# You decided to switch from a numerical grade value to a Pass/Fail option for your poetry class.
gradebook.remove(["poetry", 85])

gradebook.append(["poetry", "Pass"])

# Create a new variable full_gradebook that combines both last_semester_gradebook and gradebook using + to have one complete grade book.

full_gradebook  = last_semester_gradebook + gradebook


print(full_gradebook )
