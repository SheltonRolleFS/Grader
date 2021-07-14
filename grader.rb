class Grader
	def initialize()
		puts "What is your name?"
		@name = gets
		puts "What is the name of your assignment?"
		@assignmentName = gets
		puts "What is the grade you got in " + @assignmentName + "?"
		@grade = gets.to_f
	end
	
	def getLetterGrade
		letter_grade = ''
		if @grade < 60
			letter_grade = 'F'
		elsif @grade < 70
			letter_grade = 'D'
		elsif @grade < 80
			letter_grade = 'C'
		elsif @grade < 90
			letter_grade = 'B'
		else
			letter_grade = 'A'
		end
		
		return letter_grade
	end

end

myGrade = Grader.new
print(myGrade.getLetterGrade())
			