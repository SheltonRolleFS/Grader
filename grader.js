const readline = require("readline")
const rl = readline.createInterface({
	input : process.stdin,
	output : process.stdout
})

class Grader{
	constructor(){
	
	}
	
	getGrade(){
	
		rl.question("What is your name? ", (name) => {
		
			rl.question("What is the name of your assignment? ", (assignmentName) => {
			
				rl.question("What is your grade in " + assignmentName + "? ", (grade) => {
				
					let letterGrade
					
					if(grade < 60){
						letterGrade = 'F'
					}else if(grade < 70){
						letterGrade = 'D'
					}else if(grade < 80){
						letterGrade = 'C'
					}else if(grade < 90){
						letterGrade = 'B'
					}else{
						letterGrade = 'A'
					}
					
					console.log(letterGrade)
				
				})
			})
		})
	}
}

const myGrade = new Grader()
myGrade.getGrade()