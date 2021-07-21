import os
import csv
import numpy as np

csvPath = os.path.join("Resources","budget_data.csv")
with open(csvPath,'r') as budget_data:
    budget = csv.reader(budget_data, delimiter=',')
    
    differencesAmounts = []
    differencesMonths = []
    months= []
    amounts=[]
    totalPL = 0
    totalMonths = 0

    next(budget)
    for i in budget:
        totalMonths+=1
        totalPL+=int(i[1])
        amounts.append(int(i[1]))
        months.append(i[0])

    for i in range(len(amounts)):
        if i != len(amounts)-1:
            differencesAmounts.append(amounts[i+1] - amounts[i])
            differencesMonths.append(months[i+1])
            

    avgDiff = np.mean(differencesAmounts)
    maxDiff = max(differencesAmounts)
    minDiff = min(differencesAmounts)

    zipped = zip(differencesMonths, differencesAmounts)
    for i in zipped:
        if i[1] == maxDiff:
            maxDiffMonth = i[0]
        if i[1] == minDiff:
            minDiffMonth = i[0]


fa = ["Financial Analysis"]
dots = ["----------------------------"]
tm = ["Total Months: "+str(totalMonths)]
pl = ["Total: $"+str((totalPL))]
etwas = ["Average Change: $"+str(round(avgDiff,2))]
noch = ["Greatest Increase in Profits: "+maxDiffMonth+" ($"+str(maxDiff)+")"]
nochZwei = ["Greatest Decrease in Profits: "+minDiffMonth+" ($"+str(minDiff)+")"]

print("Financial Analysis")
print("----------------------------")
print("Total Months: "+str(totalMonths))
print("Total: $"+str((totalPL)))
print("Average Change: $"+str(round(avgDiff,2)))
print("Greatest Increase in Profits: "+maxDiffMonth+" ($"+str(maxDiff)+")")
print("Greatest Decrease in Profits: "+minDiffMonth+" ($"+str(minDiff)+")")


with open("analysis/analysis.txt",'w') as csvfile:
    analysis=csv.writer(csvfile)
    analysis.writerow(fa)
    analysis.writerow(dots)
    analysis.writerow(tm)
    analysis.writerow(pl)
    analysis.writerow(etwas)
    analysis.writerow(noch)
    analysis.writerow(nochZwei)
    
    
    
    
    
    
   
    

