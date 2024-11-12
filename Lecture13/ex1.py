#!/usr/bin/python3

#Read input.txt file
input = open('input.txt').read().upper().replace('ATTCGATTATAAGC','').split()

#Open the output pipe for writing
cleanseqs = open('Cleaned_seq.txt','w')

for cleanones in input:
	cleanseqs.write(cleanones + '\n')
	cleanones

cleanseqs.close()

print(open('Cleaned_seq.txt').read().rstrip())

