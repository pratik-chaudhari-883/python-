#Write a program which accept number from user and print even factors of that
#number.
#Input : 24
#Output: 1 2 4 6 8 12 

def DisplayEvenFactor(iNo):
    iCnt=1
    if iNo<0:
        iNo=-iNo   #Updator
    while(iCnt!=iNo):
        if(iNo%iCnt==0):
            if(iCnt%2==0):
                print("",iCnt)
            iCnt=iCnt+1
        else:
             iCnt=iCnt+1

def main():
    iValue=int(input("Enter any Number...."))
    DisplayEvenFactor(iValue)

if __name__=="__main__":
    main()

