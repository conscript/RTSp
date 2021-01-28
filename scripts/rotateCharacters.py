enteredStr = input("Enter a string: ")

invalidInput = True
while invalidInput:
    try:        
        enteredValue = input("Enter a rotate amount: ")
        rotateInt = int(enteredValue)
        if rotateInt > len(enteredStr):
            print("Length cannot be longer than string, please try again\n")
            continue
        
        invalidInput = False
    except:
        print("Invalid rotate, please try again.\n")
            
rotatedStr = enteredStr[len(enteredStr) - rotateInt:]
cutStr = enteredStr[:len(enteredStr) - rotateInt]
result = rotatedStr + cutStr

print(f"{enteredStr} rotated by {rotateInt} is {result}")
