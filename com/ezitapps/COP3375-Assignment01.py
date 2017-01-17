'''
Created on Jan 16, 2017

@author: juanramirez
'''
import string
from random import randint
from builtins import int

### This code outline only processes for one student. To process for more we need to put this code in a loop.
###     To generate a report for the entire class, we need to do the following:
###        In the main body of the driver, set up a loop to process each student
###            - Determine the final grade, and capture the student name & ID, as well as the final grade
###               (i.e. pretty much pull in all the code given below).
###            - To print the table at the end, we need to capture student information as we process it.
###              The easiest way to do this is to keep appending it in individual lists 
###                   for student name, ID and final grade
###             - alternatively, we can also do this by storing this information in a list of tuples,
###                   with one tuple per student,e.g.[(st1, id1, grade1), (st2, id2, grade2),....
###                   Note: the latter will require additional formatting.
###
###  When all the students have been processed, we exit the processing loop.
###  Now we will need to set up another simple loop to print the table.
###  We should print an appropriate header (outside of this loop) and then retrieve each line item from the lists (or list of tuples)




def add_grades(assignment):
    print("Calculates the total points for all 5 assignments")
    # capture grades for all 5 assignments and compute total
    # add other print sttements as needed to capture tests and other scores
    # at end, return total score
    
    assignmentGrades = 0
    
    
    for assignmentValue in assignment:
        assignmentGrades = assignmentGrades + assignmentValue
        
        
    return assignmentGrades
    
    
    
def letterGrade(total_score):
    # calcualte and print total percetage
    # calculate the correponding letter grade (recall we did an example of this in class)
    finalGrade = round((total_score / 310)*100)
    
    print(str(finalGrade) + "%")
    
    if finalGrade >= 90 and finalGrade <= 100:
        return("A")

    elif finalGrade >= 80 and finalGrade < 90:
        return("B")

    elif finalGrade >= 70 and finalGrade < 80:
        return("C")

    elif finalGrade >= 60 and finalGrade < 70:
        return("D")

    else:
        return("F")
    


    
  
# To facilitate input of grade
# Created a function that automatically inputs a grade.  
def automateGrade(lowRange, highRange, amount):
    
    assignmentValue = []
    
    for interval in range(amount):
        assignmentValue.append(randint(lowRange,highRange)) 
        
    return assignmentValue




def main(): 
    print("Welcome to calculate your grade program")
    
    addStudent = "Y"
    studentNumber = 0
    studentList = []
    
    ### Start of While Loop!!!
    while addStudent == "Y":
        print("Add a Student")
        
        
        
        # Input Student ID and Student Name
        # Not Automated!!!
        studentID = input("Enter Student ID: ")
        studentName = input("Enter Student Name: ")
        # Create object of Student Class.
        studentList.append(Student(studentID, studentName))
        print(studentList[studentNumber].studentName + " has been added")
        
        
        
        # Automate the addition of random grades. 
        
        # Automate the assignment grades
        studentList[studentNumber].assignment = automateGrade(15, 20, 5)
        print("Five Assignment Grades are:" , studentList[studentNumber].assignment)
        
        # Automate grade assignment for Midterm, Final and Participation
        # Print the result to make sure it's ok.  
        studentList[studentNumber].midterm = randint(80,101)
        print("Midterm Exam Grade is:",studentList[studentNumber].midterm)
        studentList[studentNumber].final = randint(80,101)
        print("Final Exam Grade is:",studentList[studentNumber].final)
        studentList[studentNumber].participation = randint(8,11)
        print("Participation Grade is:",studentList[studentNumber].participation)
        
        # Add all Assignments and save it to the student object.
        internalAssignmentSum = add_grades(studentList[studentNumber].assignment)
        studentList[studentNumber].assignmentSum = internalAssignmentSum
        #print(studentList[studentNumber].assignmentSum, internalAssignmentSum)
        studentList[studentNumber].totalGradeSum()
        
        # Assign a letter grade to the object. 
        studentList[studentNumber].letterGrade = letterGrade(studentList[studentNumber].totalGrade)
        
        
        # Increment student amount
        studentNumber = studentNumber + 1
        
        # Request to see if you want to add another student. 
        print("You have " + str(studentNumber) + " students in the list.")
        addStudent = input("Do you want to add another student? Y or N: ").upper() 
        
    #### END OF WHILE LOOP!!!
    
    #print(studentList.__len__())
    print("\n\nPrint Grade Results for Students:")
    
    students = len(studentList)
    
    # Header for printed results
    formatTemplate = "{0:15}{1:15}{2:15}{3:15}{4:15}{5:15}{6:15}{7:15}"
    print(formatTemplate.format("ID", "Name" , "Assign.", "Midterm" , "Final", "Part.", 
          "Total", "Grade"))
    
    # Loop through all students and print the results. 
    # Print the grades in a correct format.
    for student in range(students):
        studentList[student].printstudent()
    
    
    
    

    

# Student Class where we have the values for an individual student.
# Information to store for each student.   
class Student:
    
    # Student Object Variables
    studentID = ""
    studentName = ""
    letterGrade = ""
    
    assignment = []
    assignmentSum = 0
    
    midterm = 0
    final = 0
    participation = 0
    
    totalGrade = 0
    
    # Format for output.
    formatTemplate = "{0:15}{1:15}{2:5d}{3:15d}{4:14d}{5:14d}{6:16d}{7:>14}"
    
    # Constructor
    def __init__(self, studentId, studentName):
        self.studentID = studentId
        self.studentName = studentName
        
    # Print the student information. Output
    def printstudent(self):
        #self.assignmentSum
        print (self.formatTemplate.format(self.studentID, self.studentName,self.assignmentSum,self.midterm,self.final, 
              self.participation, self.totalGrade, self.letterGrade))
     
    # Add all scores.   
    def totalGradeSum (self):
        self.totalGrade = self.assignmentSum + self.midterm + self.final + self.participation
            
            

# Start Main.
if __name__ == '__main__':
    main()