#!/usr/bin/python3

DNA1 = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
A_num = DNA1.count("A")
T_num = DNA1.count("T")
AT_num = A_num + T_num

length = len(DNA1)
AT_content = AT_num/length

print("The A+T content is:", str(int(100 * AT_content)), "percent")


