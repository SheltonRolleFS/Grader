import sys

# Defining the Grader class
class Grader:
	# Creating the constructor
	def __init__(self):
		# Getting the user data from the command line in the constructor
		self.name = raw_input("What is your name? ")
		self.assignment_name = raw_input("What is the name of your assignment? ")
		self.grade = float(raw_input("What was your grade in " + self.assignment_name + "? "))
	
	# Determine the users letter grade based on the grade they entered
	def getGrade(self):
		letter_grade = ''
		
		if self.grade < 60:
			letter_grade = 'F'
		elif self.grade < 70:
			letter_grade = 'D'
		elif self.grade < 80:
			letter_grade = 'C'
		elif self.grade < 90:
			letter_grade = 'B'
		else:
			letter_grade = 'A'
		
		return letter_grade

# Instantiate the Grader class
myGrade = Grader()
# Display the letter grade for the user
print("Your letter grade in " + myGrade.assignment_name + " was a(n) " + myGrade.getGrade())
		