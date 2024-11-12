#!/usr/bin/python3

input = open('input.txt').read().upper().split()

cleanseqs = open('Cleaned_seq2.txt','w')
for eachone in input:
	cleanseqs.write(eachone[14:] + '\n')

cleanseqs.close()

import subprocess
subprocess.call("cat Cleaned_seq2.txt",shell = True)

