#Write a program which accept one number from user and print that number of
#even numbers on screen.

#Input : 7
#Output: 2 4 6 8 10 12 14 

def DisplayEven(iNo):
    itemp=0
    iCnt=1
    iCount=0
    while(iCnt!=iNo*iNo):
        if(iCount==iNo):
            break
        if(iCnt%2==0):
            print("",iCnt)
            iCnt=iCnt+1
            iCount=iCount+1
        else:
            iCnt=iCnt+1

def main():
    iValue=int(input("Enter any Number.."))
    DisplayEven(iValue)

if __name__=="__main__":
    main()
        
