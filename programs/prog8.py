#Accept two numbers from user and display first number in second
# number of times.
# Input : 12 5
# Output : 12 12 12 12 12
# Input : -2 3
# Output : -2 -2 -2
# Input : 21 -3
# Output : 21 21 21

def Display(iNo1,iNo2):

    if(iNo2<0):       #Updater
        iNo2=-iNo2

    while iNo2!=0:
        print("",iNo1)
        iNo2=iNo2-1

def main():
    print("Enter First Number..")
    iValue1=int(input())
    print("Enter Second Number..")
    iValue2=int(input())

    Display(iValue1,iValue2)
if __name__=="__main__":
    main()