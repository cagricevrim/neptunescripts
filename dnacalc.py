#! /usr/bin/env python

DNAseq = raw_input ( 'Insert a DNA Sequence ' )
DNAseq = DNAseq.upper()
print( 'Sequence ' + DNAseq )
SeqLength = len( DNAseq )
print ( 'Lenght is ' + str ( SeqLength ) )
NumberA = DNAseq.count( 'A' )
NumberT = DNAseq.count( 'T' )
NumberG = DNAseq.count( 'G' )
NumberC = DNAseq.count( 'C' )

print('A: {:.2}'.format(NumberA / float (SeqLength)))
print('T: {:.2}'.format(NumberT / float (SeqLength)))
print('G: {:.2}'.format(NumberG / float (SeqLength)))
print('C: {:.2}'.format(NumberC / float (SeqLength)))

TotalStrong = NumberG + NumberC
TotalWeak = NumberA + NumberT

if SeqLength <= 14:
	MeltTemp = ( 4 * TotalStrong ) + ( 2 * TotalWeak)
	print ('Melting Temp: {:.2f}'.format(MeltTemp))

else:
	MeltTemp = 64.9 + 41 * ( TotalStrong - 16.4 ) / SeqLength 
	print ('Melting Temp: {:.2f}'.format(MeltTemp))


print "Courtesy to Thomas..."