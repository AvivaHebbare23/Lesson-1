input1 = int(input("Enter a number to cube: "))

def difference(input1):
    numberCubed = input1 * input1 * input1
    numberSquared = input1 * input1

    difference = numberCubed - numberSquared

    return difference 

print("The difference between the cubed number and the squared number is: ", difference(input1))