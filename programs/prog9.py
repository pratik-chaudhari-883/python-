#Accept number from user and check whether number is even or
#odd.

def CheckEvenOdd(iNo):
    if iNo<0:     #Updater
        iNo=-iNo
    A=True
    if (iNo%2==0):
        return A
    else:
        A=False
        return A 

def main():
    print("Enter any Number...")
    iValue=int(input())

    bRet=True
    bRet=CheckEvenOdd(iValue)
    if(bRet==True):
        print("Number is Even Number..")
    else:
        print("Number is odd Number...")