import cv2
import numpy as np
import random
from random import seed

class hide_image:

    
    def __init__(self,b_img,h_img):
        self.b_img=b_img
        self.h_img=h_img
        
    def pixel_to_bit(self):
        himg=cv2.imread(self.h_img,0)
        print(himg.shape)
        himg1=cv2.resize(himg,(50,50))
        print(himg1.shape)
        self.himg0=himg1.shape[0]
        self.himg1=himg1.shape[1]
        himg2=np.reshape(himg1,(self.himg0*self.himg1,1))
        print(himg2.shape)
        l=[]
        for i in range(himg2.shape[0]):
            k=himg2[i][0]
            kk=self.decimal_to_binary(k)
            #print(kk)
            l.append(kk)
        #print(l)    
        self.bits=[]
        for i in range(len(l)):
            p1=l[i]
            for j in range(8):
                self.bits.append(p1[j])
        
        return(self.bits,self.himg0,self.himg1)  
    def decimal_to_binary(self,w):
        k=w
        l1=[]
        while k>0:
            l1.append(k%2)
            k=k//2
        l2=[]
        for i in range(1,len(l1)+1):
            l2.append(l1[-i])
        k1=8-len(l2)
        l3=[]
        for i in range(k1):
            l3.append(0)
        l3=l3+l2
        return l3
    
    def coding(self):
    
        import random
        from random import seed
        #from random import sample
    
        img=cv2.imread(self.b_img)
        print(img.shape)
        self.img1=np.reshape(img,(img.shape[0]*img.shape[1]*3,1))
        seed(1)
        a=[i for i in range(len(self.img1))]
        subset=random.sample(a,len(self.bits))
        for i in range(len(self.bits)):
            a1=self.bits[i]
            a2=subset[i]
            if (a1==0 and self.img1[a2][0]%2!=0)or (a1==1 and self.img1[a2][0]%2==0):
                self.img1[a2][0]+=1
        return(self.img1,img.shape[0],img.shape[1])
    
    
    def decoding(self,myseed):

        random.seed(myseed)
        a=[i for i in range(len(self.img1))]
        subsetRecovery=random.sample(a,len(self.bits))
    
        q1=[]
        for i in range(len(self.bits)):
            q2=subsetRecovery[i]
            if self.img1[q2][0]%2==0:
                q1.append(0)
            else:
                q1.append(1)
            
        z=[]
        for i in range(int(len(q1)/8)):
            z1=[]
            z1=q1[i*8:i*8+8]
            qq=self.binary_to_decimal(z1)
            z.append(qq)  
        
        recovered_pixels=z
        #print(recovered_pixels)
        recovered_pixels=np.array(recovered_pixels)
        rec_img=recovered_pixels.astype(np.uint8)
        rec_img1=np.reshape(rec_img,(self.himg0,self.himg1))
        return(rec_img1)
    
    def binary_to_decimal(self,l):
        print(l)
        c=0
        for i in range(8):
            c+=(np.power(2,7-i)*l[i])
        return c

    
