#
# H9-1:
#
#   student.py
#

class Student():
	'''
	Represents a single student, with attribes:
		name, list of quiz scores, # to drop,
		average score for all quizzes after
		dropping specified # of lowest cores
	'''

	def __init__(self, name):
		'''
		Initialize new Student with given name
			and empty list _scores
		'''
		pass

	def addScore(self,score):
		'''
		Add score to internal attribute (field) _scores
		'''
		pass

	def getNumberQuizzes(self):
		'''
		Return number of scores in attribute (field) _scores
		'''
		pass

	def calcQuizStats(self,dropNumber):
		'''
		Set _dropNumber, then set _average to mean (avg)
		calculated after dropping dropNumber lowest scores
		'''
		pass

	def getAverage(self):
		'''
		Return value of _average
		'''
		pass

	def __str__(self):
		'''
		Return string, formatted as shown in handout
		'''
		pass

def main():
	'''
	Create two Students, add quiz scores to each, then
		calculated quiz stats (choose # of lowest to drop)
		and print the stringified Student.
	One of your Students should have same output as in handout;
		you can choose your own data for the second
	'''
	pass

main()




