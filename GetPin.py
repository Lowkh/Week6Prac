#expectedInput = '12345'
expectedInput = 12345
tries = 2
while True:
    userinput = int(input("Enter pin:"))
    if userinput == expectedInput:
        print(f'Correct pin entered.')
        break       
    
    elif userinput != expectedInput and tries >0:
        print(f'Invalid pin. Please try again.')
        print(f'You have {tries} left.')
        tries -= 1
          
    else:
        print(f'Your account is locked.')
        break   
    
    
'''  
    if userinput != expectedInput:
        print(f'Invalid pin. Please try again.')
        print(f'You have {tries} left.')
        tries -= 1
        
    else:
        print(f'Correct pin entered.')
        break
        
    if tries <1:
        print(f'Your account is locked.')
        break
    '''