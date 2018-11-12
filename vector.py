# -*- coding: utf-8 -*-
import csv
from sklearn.cluster import KMeans
import numpy as np
import uniout
def main():
	tags=[]
	vec=[]
	t0=[]
	t1=[]
	t2=[]
	t3=[]
	t4=[]
	t5=[]
	typevec = []
	typevec1 = np.array([])
	same_num=[]
	name=[]
	friend=[]	
	distance = np.array([])
	dist_num = np.array([])
	type1 = np.array([])
	sort = []
	user=[]
#find same type
	i=0
	f=open('type0.txt','r')
	for type in f:
		t0.append(type)
	
	f=open('type1.txt','r')
	for type in f:
		t1.append(type)

	f=open('type2.txt','r')
	for type in f:
		t2.append(type)
	
	f=open('type3.txt','r')
	for type in f:
		t3.append(type)

	f=open('type4.txt','r')
	for type in f:
		t4.append(type)

	f=open('type5.txt','r')
	for type in f:
		t5.append(type)
#input name and type
	file = open('user.txt','r')
	for line in file:
		tags.append(line)
	print tags

#vec	
	a0=0
	a1=0
	a2=0
	a3=0
	a4=0
	a5=0
	for type in t0 :
		a0=tags.count(type)+a0
	vec.append(a0)
	for type in t1 :
		a1=tags.count(type)+a1
	vec.append(a1)
	for type in t2 :
		a2=tags.count(type)+a2
	vec.append(a2)	
	for type in t3 :
		a3=tags.count(type)+a3
	vec.append(a3)
	for type in t4 :
		a4=tags.count(type)+a4
	vec.append(a4)
	for type in t5 :
		a5=tags.count(type)+a5
	vec.append(a5)
	print vec
	
	r = open ('un.txt', 'r')
	for n in r:
		print n
		user.append(n)
	
#write name/vector 
#2
	t=0
	print len(name)
	read = open ('name.txt', 'r')
	for n in read:
		name.append(n)
		
	for people in name:	
		if (people==user[0]):
			t=1
			print 123
		
	print t	
	if (t==0): 
		vector = open('vec.txt','a')
		w = csv.writer(vector)
		a=[vec]
		w.writerows(a)
		vector.close()
#
	print len(name)
	read = open ('name.txt', 'r')
	for n in read:
		name.append(n)
	
#read vectors from csv
	file = open( 'vec.csv', 'r')
	csvsor = csv.reader(file)
	for r in csvsor:
		typevec.append(r)
	print typevec
	print 111
	typevec.append(vec)
	print 456
	print typevec[0]

#k-means
#	type1 = np.array([typevec],dtype=float64)
	num_clusters = 2
	km_cluster = KMeans(n_clusters=num_clusters, max_iter=300, n_init=40, init='k-means++',n_jobs=-1)
	result = km_cluster.fit_predict(typevec)
	print "Predicting result: ", result


#find same type
	i=0
	while i < len(result)-1:
		if(result[i]==result[-1]):
			same_num.append(i)
		i+=1
	print same_num
#rank
	vec1 = np.loadtxt(open("vec.csv","rb"),delimiter=",",skiprows=0)  
	vec2 = np.array(vec)
	
	print vec1
	print vec2
	for n in same_num:	
		dist = np.linalg.norm(vec1[n]-vec2)
		distance=np.append(distance, dist)
	print 'distance'
	print distance
	dist_num=np.argsort(distance)
	print dist_num
	for n in dist_num:
		
		sort.append(same_num[n])
	print sort

###rank_num
	a=0
	while a < 3:
		print sort[a]
		n = int(sort[a])
		s = name[n]
		print s
		friend.append(s)
		a+=1	
	print friend

#delete same name
	i=0
	print friend.count(user[0])
	num=friend.count(user[0])
	while i< num:	
		friend.remove(user[0])
		i+=1 
	print friend
	print len(friend)
	if (len(friend)!=3):
		a=int(sort[3])
		friend.append(name[a])
		print friend
#output
	f =open('friend.txt','w')
	for n in friend :	
		f.write(n)
	f.close()

if __name__ == "__main__":
	main()
