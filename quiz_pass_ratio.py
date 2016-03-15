# Dahv Reinhart - V00735279
# SEng265 - Assignment 3
# 'Quiz Pass-Ratio' - Computes the overall pass ratio for all students on each question in a given quiz
# Due Nov 28th, 2015

import libxml2
import sys
import quiz_library

'''
purpose
	Accept 1 or more log file names on the command line.

	Accumulate across all the log files the pass ratio for each question.

	A question result is considered a pass if it is not 0 or None
	and fail otherwise.

	The pass ratio for a question is the number of passes
	divided by the number of passes + fails.
preconditions
	Each command-line argument is the name of a
	readable and legal quiz log file.

	All the log_files have the same number of questions.
'''

# check number of command line arguments
if len(sys.argv) < 2:
	print 'Syntax:', sys.argv[0], 'quiz_log_file ...' #must have legal arguments supplied on the command line
	sys.exit()

initQ = quiz_library.load_quiz_log(sys.argv[1]) #since it is guarenteed that each log_file will have the same number
q = quiz_library.compute_question_count(initQ)  #of questions, initialize the question counter to the fist file.


for y in range(0, q): #goes through each question in the log files
	temp = 0.0
	counter = 0.0
	for x in range(1, len(sys.argv)): #for each question, goes through all the log_files
		log_list = quiz_library.load_quiz_log(sys.argv[x])
		mark_list = quiz_library.compute_mark_list(log_list)
		counter += 1 #the number of occurances of any given question
		temp += mark_list[y] #the cumulative marks obtained for a given question accross all log_files
	
	pass_ratio = (temp / counter) #compute the pass ratio ((passes) / (fails + passes))

	separate = ','
	if y == (q-1):
		separate = '' #fence-post printing

	sys.stdout.write((str(pass_ratio) + separate))

print ''


