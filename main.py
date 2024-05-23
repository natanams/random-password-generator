from random import randint,randrange

x=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
y=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
z=['0','1','2','3','4','5','6','7','8','9']
newlst=[]

newlst.append(y)
newlst.append(x)
newlst.append(z)

def getlst():
    st = randrange(0,3)
    return st

def getchr(*args):
    nlst=args[0]
    rchr=args[1]
    sublst=nlst[rchr]
    lensublst=len(sublst)
    newchridx=randint(0,lensublst-1)
    newchr=sublst[newchridx]
    return newchr

length_of_password=int(input("Enter the length of password: "))
i=1
newp=''
while i<=length_of_password:
    i+=1
    lstnum=getlst()
    nchr=getchr(newlst,lstnum)
    newp=newp+nchr
    nchr=''


print(newp)