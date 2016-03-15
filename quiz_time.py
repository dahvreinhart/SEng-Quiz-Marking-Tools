# Dahv Reinhart - V00735279
# SEng265 - Assignment 3
# 'Quiz Time' - Computes the average time taken on each question in a quiz accross all students. (measure of difficulty)
# Due Nov 28th, 2015

import libxml2
import sys
import quiz_library

'''
purpose
	Accept 1 or more log file names on the command line.

	For each log file, compute the total time taken for each question. 

	Write to standard output, the average time spent for each question.
preconditions
	Each command-line argument is the name of a readable and
	legal quiz log file.

	All the log_files have the same number of questions.
'''

# handle command line arguments
if len(sys.argv) < 2:
	print 'Syntax:', sys.argv[0], 'quiz_log_file ...' #must have legal arguments supplied on the command line
	sys.exit()

initQ = quiz_library.load_quiz_log(sys.argv[1]) #since it is guarenteed that each log_file will have the same number
q = quiz_library.compute_question_count(initQ)  #of questions, initialize the question counter to the fist file.


for y in range(0, q): #goes through each question in the log files
	time = []
	for x in range(1, len(sys.argv)): #for each question, goes through all the log_files
		difference = [0, 0]
		log_list = quiz_library.load_quiz_log(sys.argv[x])
		for z in log_list:
			if int(z.index) == y and isinstance(z, quiz_library.Display): #the first 'Display' object
				if difference[0] == 0:                                #of a given question
					difference[0] = z.time #time 1

			elif int(z.index) == (y+1) and isinstance(z, quiz_library.Display): #the 'Display' objct of
				if difference[1] == 0:                                      #the next question
					difference[1] = z.time #time 2
				break #dont want to keep going if we already have time 1 and 2

			elif log_list[len(log_list) -1] == z: #if we are at the end of the log_list (the last question),
				difference[1] = z.time        #then set time 2 equal to the final answer element since
							      #there is no upcoming 'Display' object coming
		if difference[0] == 0 and y != 0: #if the question was never encounterd, do not include it in 
			difference[1] = 0         #the time calculation.

		questionTime = (int(difference[1]) - int(difference[0])) #time taken on a question in 1 log_file
		time.append(questionTime) #make a list of times for a question accross all log_files

	totalTime = float(reduce(lambda x,y: x+y , time)) #add the times for a given question
	averageTime = (totalTime / (len(sys.argv) - 1)) #divide the total time by the number of log_files
							#i.e. the number of occurances of each question
	separate = ','
	if y == (q-1):
		separate = '' #fence-post printing

	sys.stdout.write((str(averageTime) + separate))
	
print ''








