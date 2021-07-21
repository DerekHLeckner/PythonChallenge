import os
import csv
import numpy as np

csvPath = os.path.join("Resources","election_data.csv")
with open(csvPath,'r') as election_data:
    electionData = csv.reader(election_data, delimiter=',')
    
    
    voteCount = 0
    uniqueCandidates = []
    candidates = []
    voterId = []
    county = []
    Khan = 0
    Correy = 0
    Li = 0
    Tooley = 0
    countNumbers = []
 


    next(electionData)
    for i in electionData:
        voteCount+=1
        candidates.append(i[2])
        county.append(i[1])
        voterId.append(i[0])

    for candidate in candidates:
        if candidate not in uniqueCandidates:
            uniqueCandidates.append(candidate)
        if candidate == uniqueCandidates[0]:
            Khan+=1
        elif candidate == uniqueCandidates[1]:
            Correy+=1
        elif candidate == uniqueCandidates[2]:
            Li+=1
        elif candidate == uniqueCandidates[3]:
            Tooley+=1
    countNumbers.append(Khan)
    countNumbers.append(Correy)
    countNumbers.append(Li)
    countNumbers.append(Tooley)


electionResults = zip(uniqueCandidates,countNumbers)
percentKhan = (Khan/voteCount) * 100
percentCorrey = (Correy/voteCount) * 100
percentLi = (Li/voteCount) * 100
percentTooley = (Tooley/voteCount) * 100

winner = uniqueCandidates[0]
  
with open("analysis/analysis.txt", "w") as txtfile: 
    print("Election Results", file = txtfile)
    print("-------------------------",file = txtfile)
    print("Total Votes: "+str(voteCount),file = txtfile)
    print("-------------------------",file = txtfile)
    print("Khan: "+str(percentKhan)+"% ("+str(Khan)+")",file = txtfile)
    print("Correy: "+str(percentCorrey)+"% ("+str(Correy)+")",file = txtfile)
    print("Li: "+str(percentLi)+"% ("+str(Li)+")",file = txtfile)
    print("Tooley: "+str(percentTooley)+"% ("+str(Tooley)+")",file = txtfile)
    print("-------------------------",file = txtfile)
    print("Winner: "+winner,file = txtfile)
    print("-------------------------",file = txtfile)
