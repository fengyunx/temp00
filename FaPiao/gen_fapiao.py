import  os,sys
import  numpy as np
import random


def isvalid2(k,yall):
    if k/1.5!=int(k/1.5):
        return None
    res=yall-k
    if res%2==1:
        return None

    numx1=int(k/1.5)
    numx2=int(res/2)

    combstr='[1.5 '+str(numx1)+' '+str(k)+'],['+'2.0 '+str(numx2)+' '+str(res)+']'

    return combstr

def isvalid3(k,yall):
    if k/1.5!=int(k/1.5):
        return None
    res=yall-k
    if res%2==1:
        return None

    numx1=int(k/1.5)
    numx2=int(res/2)

    combstr='[1.5 '+str(numx1)+' '+str(k)+'],['+'2.0 '+str(numx2)+' '+str(res)+']'

    return combstr


if __name__=='__main__':
    yall=20500

    minx1=yall//3
    maxx1=yall*2//3
    print(minx1,maxx1)

    rangey1=range(minx1,maxx1)


    comblist=[]
    for i in rangey1:
        comb=isvalid2(i,yall)
        if comb is not None:
            comblist.append(comb)
    for comb in comblist:
        print(comb)

    print('finish')