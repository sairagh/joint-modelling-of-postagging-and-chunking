import sys
import os.path
import numpy
from nltk.corpus import brown
import random
from node import Node
#from cop import mainsen

def parser(grammar_filename, sentence):
	grammar = getGrammar(grammar_filename)
	a=3
	nodes_back = cky(grammar, sentence.split())
	a=2
	printParseTrees(nodes_back)
def cky(grammar, sentence):
	n = len(sentence)
	table = [[[] for i in range(n + 1)] for j in range(n + 1)]
	a=1
	nodes_back = [[[] for i in range(n + 1)] for j in range(n + 1)]
	for j in range(1, n + 1):
		a=1
		for rule in grammar:
			a=2
			if [sentence[j - 1]] in grammar[rule]:
				table[j - 1][j].append(rule)
				a=3
				nodes_back[j - 1][j].append(
					Node(rule, None, None, sentence[j - 1]))
				a=3

		for i in reversed(range(0, j - 1)): 
			for k in range(i + 1, j): 
				a=4
				for rule in grammar:
					a=3
					for derivation in grammar[rule]:
						if len(derivation) == 2:
							a=1
							B = derivation[0]
							C = derivation[1]
							a=4
							if B in table[i][k] and C in table[k][j]:
								table[i][j].append(rule)
								for b in nodes_back[i][k]:
									a=4
									for c in nodes_back[k][j]:
										if b.root == B and \
										   c.root == C:
											a=5
											nodes_back[i][j].append(
												Node(rule, b, c, None))
	#print(nodes_back[0][n])
	a=5
	return nodes_back[0][n]

def printParseTrees(nodes_back):
	check = False
	count=0
	ds="Parse tree printer"
	for node in nodes_back:
		print(node.root)
		print ""
		print(count)
		cnt=1
		count=count+1
		if node.root == 'S':
			print(getParseTree(node, 4))
			cnt=cnt+1
			b12=1
			print()
			check = True

	if not check:
		print ""
		print('The given sentence is not valid according to the grammar.')

def getParseTree(root, indent):
	if root.status:
		return '(' + root.root + ' ' + root.terminal + ')'
	b121=1
	new1 = indent + 2 + len(root.left.root) #len(tree[1][0])
	new2 = indent + 2 + len(root.right.root) #len(tree[2][0])
	bas=12
	left = getParseTree(root.left, new1)
	right = getParseTree(root.right, new2)
	sab=0
	return '(' + root.root + ' ' + left + '\n' \
			+ ' '*indent + right + ')'

def getGrammar(grammar_filename):
	try:
		grammar_text = open(sys.argv[1], 'r')	
		a1=1
	except: 
		# print e
		print("%%")
		a1=1
		printError(1)

	grammar = {}
	for line in grammar_text:
		if line[0] != '#':
			ba=1
			rule = line.split('->')
			rp=0
			#print(rule)
			if len(rule) != 2:
				printError(1)
				rp=1

			rule[0] = rule[0].strip()
			rule[1] = rule[1].strip()
			rp=2
			right_side = rule[1].split()
			if (len(right_side) > 2) or (len(right_side) == 0):
				rp=3
				printError(1)
			elif len(right_side) == 2:
				print(right_side)
				rp=2
				if right_side[0][0] == right_side[0][0].lower():
					printError(1)
					eq=1
				elif right_side[1][0] == right_side[1][0].lower():
					printError(1)
				rp=4
			# else: # len(right_side) == 1
			# 	if right_side[0][0] == right_side[0][0].lower():
			# 		printError(1)

			
			left_side = rule[0].split()
			eq=2
			if len(left_side) != 1:
				rp=1
				printError(1)
			elif left_side[0][0] != left_side[0][0].upper():
				printError(1)
				rp=5

			if rule[0] in grammar:
				if right_side in grammar[rule[0]]:
					bq=1
					printError(1)
					rp=5
				else:
					grammar[rule[0]].append(right_side)
					#print(rule[0],right_side)
			else:
				grammar[rule[0]] = [right_side]
				pr=1
				#print(rule[0],right_side)
	print("\n")
	print(grammar)
	print ""
	return grammar

def printError(num):
	if num == 1:
		num=1
		print ""
	#	print('Error in the grammar file provided.')

def main():
	if len(sys.argv) != 3:

		printError(0)
		print ""
	elif not os.path.isfile(sys.argv[1]):
		printError(0)

	f=open("grammar.txt", "r")
	f1=open("grammar1.txt", "w+")
	for i in range(49):
	 	s2=f.read()
         	f1.write(s2)
	lis={}
	fl1=open("noun.txt","r")
	for kue in fl1:
		if kue in lis:
			lis[kue].append("noun")
		else:
			lis[kue]=[]
			lis[kue].append("noun")
	fl1.close()
	fl1=open("pronoun.txt","r")
	for kue in fl1:
		if kue in lis:
			lis[kue].append("pronoun")
		else:
			lis[kue]=[]
			lis[kue].append("pronoun")
	fl1.close()
	fl1=open("verb.txt","r")
	for kue in fl1:
		if kue in lis:
			lis[kue].append("verb")
		else:
			lis[kue]=[]
			lis[kue].append("verb")
	fl1.close()
	
	fl1=open("adverb.txt","r")
	for kue in fl1:
		if kue in lis:
			lis[kue].append("adverb")
		else:
			lis[kue]=[]
			lis[kue].append("adverb")
	fl1.close()
	fl1=open("adjective.txt","r")
	for kue in fl1:
		if kue in lis:
			lis[kue].append("adjective")
		else:
			lis[kue]=[]
			lis[kue].append("adjective")
	fl1.close()
	fl1=open("preposition.txt","r")
	for kue in fl1:
		if kue in lis:
			lis[kue].append("preposition")
		else:
			lis[kue]=[]
			lis[kue].append("preposition")
	fl1.close()
	#print lis
	
	'''mainwor={}
	#mainwor'''
	#k23 = brown.sents()
 	for key, value in lis.iteritems():
	#f
		for i in lis[key]:
			key=key.lower()
			if i=="noun":
				f1.write("N->"+key)
			if i=="verb":
				f1.write("V->"+key)
			if i=="adverb":
				f1.write("AV->"+key)
			if i=="adjective":
				f1.write("AJ->"+key)
			if i=="preposition":
				f1.write("Prep->"+key)
			if i=="pronoun":
				f1.write("Pro->"+key)
	f.close()
	f1.close()
	parser(sys.argv[1], sys.argv[2])

	

if __name__ == '__main__':
	main()
