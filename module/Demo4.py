#import modules as M
#import modules 
#from modules import Addition,Substraction,multiplication
from modules import*
def main():
    print("__name__from main",__name__)
    print("Enter first number..")
    value1=int(input())

    
    print("Enter second number..")
    value2=int(input())

    ret1=Addition(value1,value2)
    ret2=Substraction(value1,value2)
    ret3=multiplication(value1,value2)

    print("Addtion is:",ret1)
    print("Substraction is :",ret2)
    print("multiplication is:",ret3)
#code starter
if __name__ =="__main__":
    main()
