#Accept one number and check whether it  is divisible by 5 or not.

def Divisible(iNo):

    if(iNo%5==0):
        return 1
    elif(iNo%5==1):
        return 0

def main():
    print("Enter any Number that you want to check")
    iValue=int(input())

    iRet=Divisible(iValue)

    if(iRet==1):
        print("Number is divisible by 5")
    else:
        print("Number is not Divisible by 5")


if __name__=="__main__":
    main()