#!/usr/bin/env python
# -*-coding:utf-8 -*

import sys

#return key
def sort(a):
	key, index, value = a.rstrip().split("\t")
	return key


#Map
def mat_map(mRow, mCol, nRow, nCol):
	
	mapper = []
	
	for line in sys.stdin:
		row = line.rstrip().split(",")
		matrInd = row[0].strip()
		Index_r = row[1].strip()
		e = row[2:]
			
		#mapping M
		if matrInd == '1':
			for i in range(mCol):
				element = e[i].strip()
				col = i
				for j in range(mRow):
					key = str(Index_r) + ":" + str(j)
					mapper.append("{0}\t{1}\t{2}".format(key, col, element))
		#mapping N
		elif matrInd == '2':
			for i in range(nCol):
				element = e[i].strip()
				col = i
				for j in range(nCol):
					key = str(j) + ":" + str(col) 
					mapper.append("{0}\t{1}\t{2}".format(key, Index_r, element))

		#mapping X
		elif matrInd == '3':
			for i in range(mRow):
				element = e[i].strip()
				col = i
				max_ind = 100000000000000
				
				key = str(Index_r) + ":" + str(col)
				mapper.append("{0}\t{1}\t{2}".format(key, max_ind, element))

	return mapper
				
if __name__ == '__main__':
	#Set size of matrices
	mRow = int(sys.argv[1])#number of rows of Matrix M
	mCol = int(sys.argv[2])#number of columns of Matrix M
	nRow = int(sys.argv[3])#number of rows of Matrix N
	nCol = int(sys.argv[4])#number of columns of Matrix N
	
	#Get mapper of matrices
	mapper = mat_map(mRow, mCol, nRow, nCol)
	#sort mapper by key
	mapper.sort(key = sort)

	#print mapped so that reducer can get it as input using sys.stdin
	for i in mapper:
		print("%s"%(i))