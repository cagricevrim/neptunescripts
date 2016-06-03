#! /usr/bin/env python

DNAseq = 'ATGAAC'
print( 'Sequence ' + DNAseq )
SeqLength = len( DNAseq )
print ( 'Lenght is ' + str ( SeqLength ) )
NumberA = DNAseq.count( 'A' )
NumberT = DNAseq.count( 'T' )
NumberG = DNAseq.count( 'G' )
NumberC = DNAseq.count( 'C' )
print('A: ' + str( NumberA / float ( SeqLength ) ) )
print('T: ' + str( NumberT / float ( SeqLength ) ) )
print('G: ' + str( NumberG / float ( SeqLength ) ) )
print('C: ' + str( NumberC / float ( SeqLength ) ) )

 
print "Thanks Thomas..."