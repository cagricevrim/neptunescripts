#! /usr/bin/env python

#To format your DNA sequences

DNAseq = raw_input ( 'Insert a DNA Sequence ' )
DNAseq = DNAseq.upper ()
DNAseq = DNAseq.replace ( ' ', '' )
DNAseq = DNAseq.replace ( '\r', '' )
DNAseq = DNAseq.replace ( '0', '' ).replace ( '1', '' ).replace ( '2', '' ).replace ( '3', '' ).replace ( '4', '' ).replace ( '5', '' ).replace ( '6', '' ).replace ( '7', '' ).replace ( '8', '' ).replace ( '9', '' )

print ( DNAseq )
