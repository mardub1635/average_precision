import numpy as np
from scipy import stats

def calcAvgP(y,y_scores,verbose=True):
	
	"""
	array, array-> float
	Given the true positive and their score for class 1 (True class), returns the average precision.
	This function takes as an input two lists. The first are your instances labeled as True (1) or False (0), the second are the scores
	 that your retrieval system has assigned to those instances. 
	 It  gives as an output the average precision score.
	 Example:
	[1,0,1],[0.9,0.8,0.1]
	->0.8333
	"""
	#First convert the list of proba scores y_scores into a list of ranks

	y_scores= np.asarray([-x for x in y_scores])
	ranks=stats.rankdata(y_scores,method='min')#rank automatically in the "competition" ranking

	
	i_true=0.0
	precs=[]
	i_rank=0
	only_true_ranks=[]
	for instance in y:
		
		if instance==1.:
			i_true+=1.0
			only_true_ranks.append(ranks[i_rank])
		i_rank+=1
	only_true_ranks.sort()
	if verbose==True:
		print "the true pos are:" ,only_true_ranks
	i=0
	for true_rank in only_true_ranks:
			
		
		prec=(i+1)/float(true_rank)
		
		precs.append(prec)
		i+=1
	
	avP=np.mean(precs)
	return avP
#Below an example of how to run the function:
#anExample=calcAvgP([1,0,1],[0.9,0.8,0.1])
#print anExample