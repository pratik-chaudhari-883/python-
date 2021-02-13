#.Accept one number from user and print that number of * on screen. 
def Display(iNo):
    iCnt=0
    
    if iNo<0:        #Updater
        iNo=-iNo

    while(iCnt<iNo):
        print("*")
        iNo=iNo-1

def main():
    print("Enter any Number..")
    iValue=int(input())
    Display(iValue)

if __name__=="__main__":
    main()
