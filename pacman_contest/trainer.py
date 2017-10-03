import sys
import os
import random
from subprocess import Popen, PIPE

def kill_bad_individual(population,child):	#kill worst child in population
	min_score, min_index = 99999,-1
	for i in population:
		if i[-1] < min_score:
			min_score = i[-1]
			min_index = i
	if child
	del population[i]	#kill the worst!
	return 

def crossover(population):
	i = 0, j = 0
	while i == j:
		i = random.choice(range(50))
		j = random.choice(range(50))
	child1 = population[i], child2 = population[j]

	return 

def mutation(individual):
	i = random.choice(range(17))

	return 

def evaluation(individual):
	for j in range(20):	#loop thru all contest map
		try:
			map_name = 'contest%0dCapture' % j
			(stdout, stderr) = Popen(["python","capture.py","-b","ShuaiTeam","-q","-l",map_name], stdout=PIPE).communicate()
			print stdout
		except:
			print "Fail on map Contest%ddefaultCapture" % j
	return

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print "Please at least provide an option!"
		sys.exit()
	for i in range(1,len(sys.argv)):
		if sys.argv[i]=='-h':
			print '''
			-n [loop_time]
			-t test on, will not really execute
			'''
			sys.exit()

		elif sys.argv[i] == 'n':
			loop_count = int(sys.argv[i+1])
			i += 1
		elif sys.argv[i] == '-t':
			TestOn = False
			file_name 
			i += 1
		else:
			print "Invalid option!!"
			sys.exit()

	if not TestOn:
		fr = open("data","r")
		population = fr.read().split("\n")
		for i in range(loop_count):	#train loop_count generation
			child = crossover(population)
			child = mutation(child)
			kill_bad_individual(population)
	else:
		print "Test Over\n"
