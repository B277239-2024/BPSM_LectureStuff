#!/usr/bin/python3

DNA4 ="ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

exon1 = DNA4[0:63]
exon2 = DNA4[90:]

print("### Exons sequence is ###\n" + exon1 + exon2)

exon = exon1 + exon2
exon_length = len(exon)
length = len(DNA4)
print("### Coding percentage (rounded) ###\n" + str(int((exon_length /length) * 100)))


intron = DNA4[63:90]
intron = intron.lower()
print("### Finally  ###\n" + exon1 + intron + exon2)
