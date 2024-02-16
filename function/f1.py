def func ():
    print("I am function!")

func()

def func2 (num1 , num2):
    return num1+num2

print(func2(2,3))
#function asign to anothere function 
anotherFunc = func2
print(anotherFunc(76,76))




