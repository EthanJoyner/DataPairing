import csv
codeList =[]
with open('pcdCodes.csv') as codes_csv:
    currentCode= ""
    for line in codes_csv:
        idx=0
        for chara in line:
            print(chara)
            if idx % 2 == 0:
                currentCode = currentCode + chara
            else:
                currentCode = currentCode
            idx += 1 
        print(currentCode)
        codeList.append(currentCode)
        currentCode = ""
print(codeList)

















#0000 _ _ _ is the key
#Q1, q2, q3, q4, delivery, Packaging, Farming

sample = "1111pdf"
print(sample[0])

# q1 check
if sample[0] == "1":
    print("NW covered")
else:
    print("void")
# q2 check
if sample[1] == "1":
    print("NE covered")
else:
    print("void")
# q3 check
if sample[2] == "1":
    print("SW covered")
else:
    print("void")
# q4 check
if sample[3] == "1":
    print("SE covered")
else:
    print("void")