targetNumber = int(input("Enter target number of pushups:"))

inputPushup = 0
totalPushup = 0
i = 0
#while  inputPushup < targetNumber:
while totalPushup < targetNumber:
    
    i += 1    
    inputPushup = int(input(f'Day {i}: How many pushups did you do today?'))
    #inputPushup = int(input("Day {}: How many pushups did you do today?".format(i)))
    totalPushup = totalPushup + inputPushup


print(f'You did a total of {totalPushup} pushups')
print(f'You hit your target in {i} days!')   


    
'''    
while True:
    inputPushup = int(input(f'Day {i}: How many pushups did you do today?'))
    #inputPushup = int(input("Day {}: How many pushups did you do today?".format(i)))
    totalPushup = totalPushup + inputPushup
    
    if(totalPushup > targetNumber):
        break
        
print(f'You did a total of {totalPushup} pushups')
print(f'You hit your target in {i} days!')   

''' 