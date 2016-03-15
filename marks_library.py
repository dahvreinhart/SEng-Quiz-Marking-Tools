import libxml2
import sys

'''
Dahv Reinhart
V00735279
SEng 265 Assignment 2: marks_library.py
The function of this program is to accept XML files containg information about students and their school marks as input and to provide a corresponding overall course mark coupled with student ID information as output. 

'''

'''
purpose
	return the course mark for student s
preconditions
	student is a list of the form:
		[last_name, first_name, student_id, marks]
		where
		marks is a list of the form: [ [assignment_id,score], ... ]
	assignments is a dictionary of the form:
		{mark_id:[points, percentage], ... }
'''
def compute_mark(student, assignments):
	totalMark = x = 0
	for i in assignments:
		mark = (float(student[3][x][1]) / float(assignments[student[3][x][0]][0])) * (float(assignments[student[3][x][0]][1]))
		totalMark += mark    # add up each individual assignment mark and factor in weighting of the assignment
		x += 1
	return totalMark
'''
purpose
	extract the information from a and return it as a list:
		[mark_id, points, percentage]
preconditions
	s is an assignment element from a legal students XML file
'''
def extract_assignment(a):
	while a is not None:
		if a.name == "mark_id":
			b = a.content
		elif a.name == "points":
			c = int(a.content)
		elif a.name == "percentage":
			d = float(a.content)
		a = a.next
	aList = [b , c , d]    #loops through an assignments file and adds each assignment found to a list
	return aList
''':

purpose
	extract the information from s and return it as a list:
		[last_name, first_name, student_id, marks]
		where
		marks is a list of the form: [ [assignment_id,score], ... ]
preconditions
	s is a student element from a legal students XML file
'''
def extract_student(s):
	studentInfo = range(4)      #has 4 associated elements which need to be added
	assignmentInfo = range(2)   #each assignment has a name and a score; 2 elements in total
	markInfo = []  #markInfo is the running list of assignments needed to compute a total mark for the student. In 				order to handle courses which have more associated assignments, the length is undefined. Rather, 				it is simply added to when more assignments are found to exist.
	while s is not None:
		if s.name == "last_name":
			studentInfo[0] = s.content
		elif s.name == "first_name":
			studentInfo[1] = s.content
		elif s.name == "student_id":
			studentInfo[2] = s.content
		elif s.name == "marks": #'marks' is the parent of sub-children, each of which must be read
			s2 = s.children
			while s2 is not None:
				if s2.name == "mark": #'mark' is also the parent of sub-children
					s3 = s2.children
					while s3 is not None:
						if s3.name == "mark_id":
							assignmentInfo[0] = s3.content #assignment name
						elif s3.name == "score":
							assignmentInfo[1] = int(s3.content) #score on assignment
						s3 = s3.next
					markInfo.append(list(assignmentInfo)) #build the list of marks obtained
				s2 = s2.next
		s = s.next
	studentInfo[3] = markInfo #add the students marks attained on all assignments to their overall record
	return studentInfo






















