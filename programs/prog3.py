#Program to print reverse  order numbers on screen.

def PrintNumbers(iNo):
    
    while iNo!=0:
        print("",iNo)
        iNo=iNo-1
def main():
    
    print("Enter number to print in reverse order")
    iValue=int(input())
    ret=PrintNumbers(iValue)

if __name__ =="__main__":
    main()
