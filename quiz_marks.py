# Dahv Reinhart - V00735279
# SEng265 - Assignment 3
# 'Quiz Marks' - Computes the total mark obtained by a given student for a given quiz
# Due Nov 28th, 2015

import libxml2
import sys
import quiz_library

'''
purpose
	Accept 1 or more log file names on the command line.
	For each log file
		write to standard output the course mark for the log file,
		in CSV format
preconditions
	Each command-line argument is the name of a legal, readable quiz log file.

	All of the log files have the same number of questions.
'''

# handle command line arguments
if len(sys.argv) < 2:
	print 'Syntax:', sys.argv[0], 'quiz_log_file ...' #must have legal arguments supplied on the command line
	sys.exit()

for x in range(1, len(sys.argv)): #go through each one of the log_files supplied 
	log_list = quiz_library.load_quiz_log(sys.argv[x])
	mark_list = quiz_library.compute_mark_list(log_list)
	course_mark = reduce(lambda y,z: y+z, mark_list) #add up all the marks obtained in a log_file
	print (sys.argv[x] + ',' + str(course_mark))     #this will equal the total mark for the student on that quiz
