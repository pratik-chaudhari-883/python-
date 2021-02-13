import marvellus
#defination of addition function 
def Addition(no1,no2):
    ans=no1+no2
    return ans
#defination of substraction function 
def Substraction(no1,no2):
    ans=no1-no2
    return ans
#entrypoint function

def main():
    print("Enter first number..")
    value1=int(input())

    
    print("Enter second number..")
    value2=int(input())

    ret1=Addition(value1,value2)
    ret2=Substraction(value1,value2)
    ret3=marvellus.multiplication(value1,value2)

    print("Addtion is:",ret1)
    print("Substraction is :",ret2)
    print("multiplication is:",ret3)
#code starter
if __name__ =="__main__":
    main()
