#Due to online school I have to take in pictures of my home work and then create a pdf of it and
#finally have to upload it. This can be made much easier through the cv2 class.
import cv2
import random
import time
begin=time.time()
def snapShot():
    num=random.randint(1,20)
    imageCaptureObj=cv2.VideoCapture(0)
    #To capture the image
    result=True
    while(result):
        ret,frame=imageCaptureObj.read()
        hw_name="HW"+str(num)+".png"
        print(ret) #It will print true if the image is taken else false
        cv2.imwrite(hw_name,frame)
        result=False
    return hw_name
    print("Picture taken successfully")
    begin=time.time()
    imageCaptureObj.release()
    cv2.destroyAllWindows()

def main():
    cond="true"
    while(cond=="true"):
        if((time.time()-begin)>=10):
            name=snapShot()
            print(name)
            
            cond=input(("Enter True to continue and F to exit "))
main()
