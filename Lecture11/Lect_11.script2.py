#!/usr/bin/python3

DNA2 = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
dna2_1 = DNA2.replace("A","t")
dna2_2 = dna2_1.replace("T","a")
dna2_3 = dna2_2.replace("C","g")
dna2_4 = dna2_3.replace("G","c")

DNA2_re = dna2_4.upper()
print("The complement sequence is " + str(DNA2_re))
