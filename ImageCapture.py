
import cv2
import dropbox
import random
import time
startTime = time.time()
def takeSnapshot():
    r = random.randint(0,100)
    captureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = captureObject.read()
        imageName = "img"+str(r)+".png"
        cv2.imwrite(imageName,frame)
        startTime = time.time
        result = False
    return imageName
    print("Snapshot has been taken")
    captureObject.release()
    cv2.destroyAllWindows()
def uploadFile(imageName):
    accessToken = "NWZWDC2cpigAAAAAAAAAAY3YdQ1nGubGZ8HH39cM-iViUxD_d9BB1ME-7EMI8qA7"
    fileSource = imageName  
    fileDestination = "/testfolder/" + (imageName)
    db = dropbox.Dropbox(accessToken)
    with open(fileSource,"rb")as f:
        db.files_upload(f.read(),fileDestination,mode=dropbox.files.WriteMode.overwrite)
        print("files uploaded")
def main():
    while(True):
        if((time.time()-startTime)>=5):
            iname = takeSnapshot()
            uploadFile(iname)
main()        
    

