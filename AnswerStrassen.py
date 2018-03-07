import os
import sys
import optparse
import importlib

def readFile( name , lineM ):
	matrix = []

	readM = open(name, 'r')
	for i in range(lineM):
		matrix += 	[list(map( int, readM.readline().split() ))]

	return matrix

def readFiles( name_m1 , name_m2 ):

	matrix1 = []
	matrix2 = []

	readM1 = open(name_m1, 'r')
	lineM1, rowM1 = map( int, readM1.readline().split() )
	for i in range(lineM1):
		matrix1 += 	[list(map( int, readM1.readline().split() ))]

	readM2 = open(name_m2, 'r')
	lineM2, rowM2 = map( int, readM2.readline().split() )
	for i in range(lineM2):
		matrix2 += 	[list(map( int, readM2.readline().split() ))]

	readM2.close()
	readM1.close()

	return matrix1 , matrix2


l = ["Aluno1", "Aluno2"]

def equal( m1 , m2 ):

	if len(m1) != len(m2): return False
	
	for i in range(len(m1)):
		if len(m1[i]) != len(m2[i]) : return False

	for i in range( len(m1) ):
		for j in range( len(m1[i]) ):
			if( m1[i][j] != m2[i][j] ) : return False

	return True


for i in l:
	points = 0
	try:
		loader = importlib.import_module(i)
	except Exception as e:
		print('Error:', e)
		continue

	for j in range(1,11):
		m1 , m2 = readFiles("../M1_{}.in".format(j),"../M2_{}.in".format(j))
		try:
			a = loader.Strassen( m1, m2 )
		except Exception as e:
			print('Caso {}: Error -'.format(j), e)
			continue
		m3 = readFile("../M3_{}.in".format(j), len(m1))
		if( equal(m3,a) ):
			print('Caso {}: OK'.format(j))
			points += 1
		else:
			print('Caso {}: Error -'.format(j), "Diferente")

	print( i , points )
