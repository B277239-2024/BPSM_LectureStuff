#!/usr/bin/python3

sequencein = "atatatatatcgcgtatatatacgactatatgcattaattatagcatatcgatatatatatcgatattatatcgcattatacgcgcgtaattatatc"

possible_kmer_sizes = list(range(2,7))
kmerfound_minimum = 3

for window in possible_kmer_sizes   :
    kmersfound = []
    kmerrange = list(range(0,len(sequencein)))
    for startingbase in kmerrange:
        if (startingbase+window)<len(sequencein)+1   :
            seqout = (sequencein)[startingbase:startingbase+window]
            kmersfound = kmersfound + [seqout]

    nonredundantset = list(set(kmersfound))
    for kmerfrequencies in nonredundantset   :
       if kmersfound.count(kmerfrequencies) > kmerfound_minimum :
           print("Lots! " + str(kmerfrequencies)+" "+str(kmersfound.count(kmerfrequencies)))
       else   :
           print(str(kmerfrequencies) + " " + str(kmersfound.count(kmerfrequencies)))

