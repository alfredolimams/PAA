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


l = ["c14111252"]

for i in l:
	try:
		loader = importlib.import_module(i)
	except ImportError as err:
		print('Error:', err)
	m1 , m2 = readFiles("../M1_1.in","../M2_1.in")
	

	a = loader.Strassen( m1, m2 )

	m3 = readFile("../M3_1.in", len(m1))

	print("A" , m3)
	print("F" , a)
	
