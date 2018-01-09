from nltk.corpus import brown
from random import *
from numpy import *
import numpy as np
import operator
#sen12=raw_input("input sentence")
word_s = brown.words()
k = brown.sents()
k123=brown.sents()
#print k[int(1)]
#print k[1:3]
len_total = len(word_s)
uniq_brown = list(set(brown.words()))
len_uniq = len(uniq_brown)
a=[]
b={}
from decimal import *
from math import *
context = Context(prec=50)
setcontext(context)
'''-------------------------------------------------------------------
 Counting words with some tag for evaluting emission probabilities
--------------------------------------------------------------------'''
'''count=[]
cou_dit={}
for i in range(0,10):
    count.append(Decimal(0))
for i in range(0,len_uniq):
    cou_dit[uniq_brown[i]] = {0: Decimal(0), 1: Decimal(0), 2: Decimal(0), 3: Decimal(0), 4: Decimal(0), 5: Decimal(0), 6: Decimal(0), 7: Decimal(0), 8: Decimal(0), 9: Decimal(0)}
for i in range(0,len_total):
    ra = (randint(0,9))
    count[ra] = count[ra] + Decimal(1)
    cou_dit[word_s[i]][ra] = cou_dit[word_s[i]][ra] + Decimal(1)
s--------------------------------------------------------
 Initializing random initial transition proabilities
-------------------------------------------------------
sum_column=[]
sum_row=[]
for i in range(1,11):
    sum_column.append(Decimal(1))
    sum_row.append(Decimal(1))
for i in range(0,9):
    l1=[]
    for j in range(0,9):
        limit = min(sum_column[j],sum_row[i])
        re = uniform(0,double(limit))
	re = Decimal(re)
        l1.append(Decimal(re))
        sum_column[j] = sum_column[j] - re
        sum_row[i] = sum_row[i] -re
    l1.append(Decimal(sum_row[i]))
    sum_column[9]= sum_column[9] - sum_row[i]
    sum_row[i] = 0
    a.append(l1)
l2=[]
for i in range(0,10):
    l2.append(Decimal(sum_column[i]))
a.append(l2)'''

log_a = []
log_b = {}
for i in range(0,10):
	e = np.random.dirichlet((1,1,1,1,1,1,1,1,1,1),1)[0]
	rt = []		
	for tr in range(0,10):			
		rt.append(log(e[tr],10))
	#a.append(e)
	log_a.append(rt)
#----------------------------------------------------------------
'''Initializing initial random emission probabilities'''
#---------------------------------------------------------------
#for i in range(0,len_uniq):
#    b[uniq_brown[i]] = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
#    log_b[uniq_brown[i]] = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

for j in range(0,len_uniq):
	e = np.random.dirichlet((1,1,1,1,1,1,1,1,1,1),1)[0]
	#b[uniq_brown[j]] = e
	rt = []
	for tr in range(0,10):
		rt.append(log(e[tr],10))
	log_b[uniq_brown[j]] = rt

# M_PI probabilities
pi= np.random.dirichlet((1,1,1,1,1,1,1,1,1,1),1)[0]
log_pi = []
for i in range(0,10):
	log_pi.append(log(pi[i],10))
	#log_b[uniq_brown[j]][i] = rt

'''
for i in range(0,10):
    pi.append(0)
for i in range(0,10):
    pi[i] = (count[i])/Decimal(len_total))

#Observsation sequence
'''
sen_len = 50
ler = []
k1=[]
for i in range(0,sen_len):
	ler.append(len(k[i]))
for i in range(0,sen_len):
	k1.append(k[i])
sen_c = 0
#br_le=[]
#for i in range(0,sen_len):
#br_le.append(len(k[i])
#print k[int(1)]
def logSumExp(ns):
    m = np.max(ns)
    ds = ns - m
    s = np.power(10,ds).sum()
    return m + np.log10(s)
ct=0
while ct<1:
	sen_c = 0
	ct = ct + 1
	while(sen_c < sen_len):
		#Forward Algorithm
		if int(sen_c) >1:
			break
		print "Working on Sentence ", sen_c
		
		#print "@##"
		#print len(k[1])
		obse = ler[sen_c]
		o1 = k1[sen_c]
		#for i in range(0,obse):
		#    o1.append(uniq_brown[randint(0,len_uniq)])

		sen_c = sen_c + 1
		alpha=[]
		for i in range(0,10):
		    rty=[]
		    for j in range(0,obse):
			rty.append(0)
		    alpha.append(rty)
	
		def forward():
			for i in range(0,10):
			    alpha[i][0] = log_pi[i]+log_b[o1[0]][i]
			    #print alpha[i][0],
			for i in range(1,obse):
			    for j in range(0,10):
				su = 0
				temp=[]
				for k in range(0,10):
					temp.append(alpha[k][i-1]+log_a[k][j])
				'''ma=-1290
				for k in range(0,10):
				    #su = su + pow(10,alpha[k][i-1]+log_a[k][j])
				    #print alpha[k][i-1],log_a[k][j] 
				    if alpha[k][i-1]+log_a[k][j] > ma:
					ma=alpha[k][i-1]+log_a[k][j]
				for k in range(0,10):
				    su = su + pow(10,alpha[k][i-1]+log_a[k][j]-ma)
				if su!=0:
					su = log(su,10) +  ma
				else:
					su = -1290
				'''
				alpha[j][i] = log_b[o1[i]][j]+logSumExp(temp)
		forward()
		print obse-1
		s1 = 0
		ma=-1290
		su =[]
		for i in range(0,10):
			su.append(alpha[i][obse-1])
		#print su
		print logSumExp(su)
		for i in range(0,10):
			if alpha[i][obse-1] > ma:
		  		ma=alpha[i][obse-1]
		for i in range(0,10):
			s1 = s1 + pow(10,alpha[i][obse-1]-ma)			 
		s1 = log(s1,10) + ma
		#print s1
		#Backword Algorithm

		beta =[]
		for i in range(0,10):
		    poo=[]
		    for j in range(obse):
			poo.append(0)
		    beta.append(poo)
		for i in range(0,10):
		    beta[i][obse-1]=0.0
		def backword():
			for i in range(0,obse-1):
			    y=obse-2-i
			    for j in range(0,10):
				su=0
				ma = -1290
				temp=[]
				for k in range(0,10):
					temp.append(beta[k][y+1] + log_a[j][k] + log_b[o1[y+1]][k])
				beta[j][y]=logSumExp(temp)
		backword()
		qw =0
		ma = -1290
		temp=[]
		for i in range(0,10):
			temp.append(log_pi[i]+log_b[o1[0]][i]+ beta[i][0])
	
		print logSumExp(temp) 

		#-------------------------------------------------------------------
		''' Baum Welch Algorithm '''
		#-------------------------------------------------------------------
		no_of_loops = 1
		ty = 0
		while ty<no_of_loops:
			ty = ty + 1
			gamma = []

			for i in range(0,10):
			    poo=[]
			    for j in range(0,obse):
				poo.append(0)
			    gamma.append(poo)
			for i in range(0,10):
			    for j in range(0,obse):
				gamma[i][j] = alpha[i][j]+beta[i][j]
				se = 0
				ma = -1290
				for k in range(0,10):
					if alpha[k][j]+beta[k][j]>ma:
						ma = alpha[k][j]+beta[k][j]
				for k in range(0,10):
				    se = se + pow(10,alpha[k][j]+beta[k][j]-ma)
				if se!=0:
					gamma[i][j] = gamma[i][j] - (log(se,10) + ma)
				else:
					gamma[i][j] = -1290

			eeta = []
			for i in range(0,10):
			    poo=[]
			    for j in range(0,10):
				po = []
				for k in range(0,obse):
				    po.append(0)
				poo.append(po)
			    eeta.append(poo)
			usage = []
			for k in range(0,obse-1):
			    s = 0
			    ma = -1290
			    for i in range(0,10):
				for j in range(0,10):
					if alpha[i][k]+log_a[i][j]+beta[j][k+1]+log_b[o1[k+1]][j]>ma:
						ma = alpha[i][k]+log_a[i][j]+beta[j][k+1]+log_b[o1[k+1]][j]
			    for i in range(0,10):
				for j in range(0,10):	
				    s = s + pow(10,alpha[i][k]+log_a[i][j]+beta[j][k+1]+log_b[o1[k+1]][j]-ma)
			    usage.append(log(s,10) + ma)
			for i in range(0,10):
			    for j in range(0,10):
				for k in range(0,obse-1):
				    eeta[i][j][k] = alpha[i][k]+log_a[i][j]+beta[j][k+1]+log_b[o1[k+1]][j]
				    eeta[i][j][k] = eeta[i][j][k] - usage[k]

			#Updating the pi,a,b
			#pi
			to=0
			ma = -1290
			for i in range(0,10):
				if gamma[i][0]>ma:
					ma = gamma[i][0]
			for i in range(0,10):
			    to = to + pow(10,gamma[i][0]-ma)
		
			for i in range(0,10):
	       		    log_pi[i] = gamma[i][0]-(log(to,10)+ma)
			#a
			for i in range(0,10):
			    for j in range(0,10):
				so =0
				so1=0
				ma=-1290
				ma1 = -1290
				for k in range(0,obse-1):
				    if gamma[i][k]>ma:
					ma = gamma[i][k]
				    if eeta[i][j][k]>ma1:
					ma1 = eeta[i][j][k]
				for k in range(0,obse-1):
				    so1 = so1 + pow(10,gamma[i][k]-ma)
				    so = so + pow(10,eeta[i][j][k]-ma)
				if so!=0 and so1!=0:
				    	we = log(so,10)-log(so1,10)-ma+ma1
				    	log_a[i][j] = we
				else:
					log_a[i][j] = log_a[i][j]
			for i in range(0,10):
			    so = 0
			    ma =-1290
			    for j in range(0,10):
				if log_a[i][j]>ma:
					ma = log_a[i][j]
			    for j in range(0,10):
				so = so + pow(10,log_a[i][j]) - ma
			    for j in range(0,10):
				log_a[i][j] = log_a[i][j] - (log(so,10)+ma)
			#b
			for i in range(0,10):
			    for j in range(0,len_uniq):
				so =0
				so1=0
				ma = -1290
				ma1 = -1290
				for k in range(0,obse):
					if gamma[i][k]>ma:
						ma = gamma[i][k]
					if o1[k] == uniq_brown[j] and  gamma[i][k]>ma1:
						ma1 = gamma[i][k]
				for k in range(0,obse):
					so = so + pow(10,gamma[i][k]-ma)
					if o1[k] == uniq_brown[j]:
						so1 = so1 + pow(10,gamma[i][k] - ma1)
				if so1!=0 and so!=0:
					wrrr = log(so1,10) + ma1 - log(so,10) - ma
					log_b[uniq_brown[j]][i] = wrrr
				else:
					log_b[uniq_brown[j]][i] = log_b[uniq_brown[j]][i] 
			for j in range(0,len_uniq):
			    so = 0
			    ma = -1290
			    for i in range(0,10):
				if log_b[uniq_brown[j]][i]>ma:
					ma = log_b[uniq_brown[j]][i]
			    for i in range(0,10):
				so = so+pow(10,log_b[uniq_brown[j]][i]-ma)

			    for i in range(0,10):
				log_b[uniq_brown[j]][i] = log_b[uniq_brown[j]][i]-(log(so,10)+ma)
			'''s1 = 0
			ma=-1290
			for i in range(0,10):
				if alpha[i][obse-1] > ma:
		  			ma=alpha[i][obse-1]
			for i in range(0,10):
				s1 = s1 + pow(10,alpha[i][obse-1]-ma)			 
			s1 = log(s1,10) + ma
			print s1'''
			forward()
			backword()
			s1 = 0
			ma=-1290
			for i in range(0,10):
				if alpha[i][obse-1] > ma:
		  			ma=alpha[i][obse-1]
			for i in range(0,10):
				s1 = s1 + pow(10,alpha[i][obse-1]-ma)			 
			s1 = log(s1,10) + ma
			print s1
		
#Completed

#Returning top n words of every tag
outp = []
for j in range(0,10):
	dittt={}
	for i in range(0,len_uniq):
		dittt[uniq_brown[i]] = log_b[uniq_brown[i]][j]
	outp.append(dittt)
for i in range(0,10):
	print i
	x = outp[i]
	sorted_x = sorted(x.items(), key=operator.itemgetter(1),reverse=True)
	for j in range(0,10):
		print sorted_x[j][0],
	print ""
duc={}
mainsen={}
#mainw=sen12.split()
print k123[0]
mainw=k123[0]
for j in range(len(mainw)):
	for i in range(0,10):
		duc[i]=log_b[mainw[j]][i]
	sorted_x = sorted(duc.items(), key=operator.itemgetter(1),reverse=True)	
	duc.clear()
	mainsen[mainw[j]]=[]
	print sorted_x
	dict2={}
	for k in range(3):
		print sorted_x[k]
		if(sorted_x[k][0]==0 or sorted_x[k][0]==6 ):
			if "noun" not in dict2:			
				mainsen[mainw[j]].append("noun")
				dict2["noun"]=1;
		if(sorted_x[k][0]==1 or sorted_x[k][0]==8):
			#mainsen[mainw[j]].append("verb")
			if "verb" not in dict2:			
				mainsen[mainw[j]].append("verb")
				dict2["verb"]=1;
		if(sorted_x[k][0]==2 ):
			#mainsen[mainw[j]].append("adverb")
			if "adverb" not in dict2:			
				mainsen[mainw[j]].append("adverb")
				dict2["adverb"]=1;
		if(sorted_x[k][0]==4 or sorted_x[k][0]==5):
			#print "add"
			#mainsen[mainw[j]].append("adjective")
			if "adjective" not in dict2:			
				mainsen[mainw[j]].append("adjective")
				dict2["adjective"]=1;
		if(sorted_x[k][0]==9):
			if "preposition" not in dict2:			
				mainsen[mainw[j]].append("preposition")
				dict2["preposition"]=1;
			#mainsen[mainw[j]].append("preposition")
   		if(sorted_x[k][0]==3 or sorted_x[k][0]==7):
			#mainsen[mainw[j]].append("other")
			if "other" not in dict2:			
				mainsen[mainw[j]].append("other")
				dict2["other"]=1;
print mainsen




