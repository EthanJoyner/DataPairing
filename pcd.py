import csv

#Name list maker
nameList = []
with open('names.csv') as names_csv:
    for name in names_csv:
        print(name)
        nameList.append(name.replace("\n",""))
print("nameList:")
print(nameList)

# Code list Maker
codeList =[]
with open('pcdCodes.csv') as codes_csv:
    currentCode= ""
    for line in codes_csv:
        idx=0
        for chara in line:
            if idx % 2 == 0:
                currentCode = currentCode + chara
            else:
                currentCode = currentCode
            idx += 1 
        codeList.append(currentCode)
        currentCode = ""
print("codeList:")
print(codeList)


# Binder
nameCodeList=[]
smallsec=[]
if len(codeList) == len(nameList):
    thisIdx = 0
    for x in codeList:
        smallsec.append(nameList[thisIdx])
        smallsec.append(codeList[thisIdx])
        nameCodeList.append(smallsec)
        smallsec=[]
        thisIdx +=1
    print("Full Result:")
    print(nameCodeList)
else:
    print("The csv files are out of sync")

















#0000 _ _ _ is the key
#Q1, q2, q3, q4, delivery, Packaging, Farming



def codeCheck (sample):
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
    # packaging check
    if sample[4] == "p":
        print("Packaging Confimed")
    else: 
        print("void")    
    # driving check
    if sample[5] == "d":
        print("Driving Confirmed")
    else: 
        print("void")  
    # Farming check
    if sample[6] =="f":
        print("Farming Confirmed")
    else: 
        print("void")