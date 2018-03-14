import os
import sys
import optparse
import importlib
import csv
import time

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

def equal( m1 , m2 ):

	if len(m1) != len(m2): return False
	
	for i in range(len(m1)):
		if len(m1[i]) != len(m2[i]) : return False

	for i in range( len(m1) ):
		for j in range( len(m1[i]) ):
			if( m1[i][j] != m2[i][j] ) : return False

	return True

def createCsv(size):
	file = open( 'Notas.csv' , 'w' )
	file.write( 'matricula' )
	for i in range(size):
		file.write( ',time {}'.format(i+1) )
	file.write( ',nota\n' )


def run(size):
	files = os.listdir()
	with open('Notas.csv', 'a') as data:
		writer = csv.writer(data)
		for i in files:
			if 	i[-3:] != '.py' or i == 'rank.py' : 
				continue
			values = []
			values.append( i[1:-3] )
			points = 0
			try:
				loader = importlib.import_module(i[:-3])
			except Exception as e:
				for j in range(size): values.append( e )
				values.append( 0 )
				writer.writerow(values)
				continue

			for j in range(1,size+1):
				m1 , m2 = readFiles("../M1_{}.in".format(j),"../M2_{}.in".format(j))
				t1 = time.time()
				try:
					a = loader.Strassen( m1, m2 )
				except Exception as e:
					values.append( e )
					continue
				t2 = time.time() 
				m3 = readFile("../M3_{}.in".format(j), len(m1))
				if( equal(m3,a) ):
					values.append( str(t2 - t1)[:6] )
					points += 1
				else:
					values.append( 'X' )
			values.append(points)
			writer.writerow(values)

def main():
	createCsv( 10 )
	run( 10 )

main()
