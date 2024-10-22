#!/usr/bin/python3

DNA3 = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
seq1 = DNA3[:DNA3.find("GAATTC")+1]
length1 = len(seq1)

seq2 = DNA3[DNA3.find("GAATTC")+1:]
length2 = len(seq2)

print("Lengths of each fragments are ", str(length1),"and",str(length2))


