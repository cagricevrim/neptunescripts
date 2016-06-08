#! /usr/bin/env python

DNAseq = raw_input ( 'Insert a DNA Sequence ' )
DNAseq = DNAseq.upper()
print( 'Sequence ' + DNAseq )
SeqLength = len( DNAseq )
print ( 'Lenght is ' + str ( SeqLength ) )
#NumberA = DNAseq.count( 'A' )
#NumberT = DNAseq.count( 'T' )
#NumberG = DNAseq.count( 'G' )
#NumberC = DNAseq.count( 'C' )

TotalStrong = 0
TotalWeak = 0


Bases = "CGTA"

for Base in Bases:
	Count = DNAseq.count (Base)
	Frequency = Count / float (SeqLength)
	print ( 'Base: {}, {:.2f}'.format( Base, Frequency ) )

	if Base in 'GC':
		TotalStrong = TotalStrong + Count

	else:
		TotalWeak = TotalWeak + Count

Counts

#print('A: {:.2}'.format(NumberA / float (SeqLength)))
#print('T: {:.2}'.format(NumberT / float (SeqLength)))
#print('G: {:.2}'.format(NumberG / float (SeqLength)))
#print('C: {:.2}'.format(NumberC / float (SeqLength)))

#TotalStrong = NumberG + NumberC
#TotalWeak = NumberA + NumberT

if SeqLength <= 14:
	MeltTemp = ( 4 * TotalStrong ) + ( 2 * TotalWeak)
	print ('Melting Temp: {:.2f}'.format(MeltTemp))

else:
	MeltTemp = 64.9 + 41 * ( TotalStrong - 16.4 ) / SeqLength 
	print ('Melting Temp: {:.2f}'.format(MeltTemp))
#
#
print "Courtesy to Thomas..." 