# program to divide two number 

def DivideNumbers(iNo1,iNo2):
    iAns=iNo1/iNo2
    return iAns

def main():
    print("Enter First Number..")
    iValue1=int(input())

    print("Enter Second n=Number..")
    iValue2=int(input())

    iRet=DivideNumbers(iValue1,iValue2)

    print("Division of two Number is:",iRet)

if __name__=="__main__":
    main()


