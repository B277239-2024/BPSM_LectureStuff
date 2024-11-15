#!/usr/bin/python3

flygenedata = open("data.csv")

for geneline in flygenedata :
    gene_info = geneline.split(",")
    species = gene_info[0]
    geneseqs = gene_info[1].upper()
    seqlengths = len(gene_info[1])
    genenames = gene_info[2]
    expressionlevel = int(gene_info[3])
    atcontent = (geneseqs.count('A')+geneseqs.count('T'))/seqlengths
    atstatus = "low"
    if(atcontent >= 0.45 and atcontent <= 0.65) :
        atstatus="medium"
    if(atcontent>0.65) :
        atstatus="high" 
    if "melanogaster" in species or "simulans" in species:
        print("Question 1 (melanogaster or simulans): "+ species + " "+genenames)
    else   :
        print("Question 1 (FAIL): "+ species + " "+genenames)
    if seqlengths > 90 and seqlengths < 110:
        print("Question 2 (seqlength >90 and <110): "+ species + " "+genenames)
    else   :
        print("Question 2 (FAIL): "+ species + " "+genenames)
    if atcontent < 0.5 and expressionlevel > 200:
        print("Question 3 (AT content <0.5, expr > 200): "+ species + " "+genenames)
    else   :
        print("Question 3 (FAIL): "+ species + " "+genenames)
    if (genenames.startswith("k") or genenames.startswith("h")) and ("Drosophila melanogaster" not in species)   :
        print("Question 4 (names start with k or h, not melanogaster): " + species + " " + genenames)
    else   :
        print("Question 4 (FAIL): " + species + " " + genenames)
    print("Question 5 (AT content status): " + genenames + " " + atstatus)
