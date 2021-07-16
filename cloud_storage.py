import dropbox
class Transfer:
    def __init__(self,key):
        self.key = key
    def uploadFile(self,source,destination):
        db = dropbox.Dropbox(self.key)
        f = open(source,"rb")
        db.files_upload(f.read(),destination)
def main():
    key1 = "NWZWDC2cpigAAAAAAAAAAY3YdQ1nGubGZ8HH39cM-iViUxD_d9BB1ME-7EMI8qA7"
    t = Transfer(key1)
    sourcefile = input("enter the file that you need to be stored")
    destinationfile = input("enter the full path of the dropbox")
    t.uploadFile(sourcefile,destinationfile)
    print("file has been moved")
main()

    
    