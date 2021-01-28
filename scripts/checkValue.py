valueList = ( 1, 5, 2, 1, 10 )

invalidInput = True
while invalidInput:
    try:
        enteredValue = input("Enter an integer: ")
        inputInt = int(enteredValue)
        invalidInput = False

    except:
        print("Invalid type, please try again.\n")

        
greaterCount = list(filter(lambda value: value > inputInt, valueList))
lessCount = len(valueList) - len(greaterCount);

print(f"Above: {len(greaterCount)}, Below: {lessCount}")

