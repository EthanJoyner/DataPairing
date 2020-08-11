import gspread
from oauth2client.service_account import ServiceAccountCredentials

gc = gspread.service_account(filename='Cred.json')
sh = gc.open_by_key('Enter Sheets URL Here')
worksheet = sh.sheet1

# Hasher Algo
def codeCheck (sample):
    # q1 check
    if sample[0] == "1":
        print("NW covered")
    # q2 check
    if sample[1] == "1":
        print("NE covered")
    # q3 check
    if sample[2] == "1":
        print("SW covered")
    # q4 check
    if sample[3] == "1":
        print("SE covered")
    # packaging check
    if sample[4] == "p":
        print("Packaging Confimed")
    # driving check
    if sample[5] == "d":
        print("Driving Confirmed")
    # Farming check
    if sample[6] =="f":
        print("Farming Confirmed")

fullSheet = worksheet.get_all_records()

nameList = []
codeList = []
for value in fullSheet: #Full Dict List
    currentWorkplace = []
    idx = 0
    for index in value.items(): # Dict item pair
        #print(index)
        for output in index: # listing of just the items then appending them into a list
            # print(output)
            idx += 1
            if idx % 2 == 0:
                # print(output)
                currentWorkplace.append(output)
    #add to name
    nameList.append(currentWorkplace[0])


    #format code
    currentWPCode = currentWorkplace[1:]
    currentFMTcode = ""
    for chara in currentWPCode:
         currentFMTcode = currentFMTcode + str(chara)
    codeList.append(currentFMTcode)
print("~~~~~~~~~~~~~~~~~~~~~")

if len(codeList) == len(nameList):
    print("SUCCESS!")
    # print("codeList: \n" + str(codeList))
    # print("nameList: \n" + str(nameList))
    idx3 = 0
    superList =[]
    for entry in codeList:
        currentSuperList = [nameList[idx3], codeList[idx3]]
        superList.append(currentSuperList)
        currentSuperList = []
        idx3 += 1
else:
    print("Sync error")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
for entry in superList:
    print("The volunteer's, '" + entry[0] + "' conditions.")
    codeCheck(entry[1])
    print("\n ~~~~~~~~~~~ \n")

