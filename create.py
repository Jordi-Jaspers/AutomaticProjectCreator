import sys
import os
from github import Github

PATH                = "/Users/jordi/Google Drive/Coding Projects/"
USERNAME    = "Jordi-Jaspers"
PASSWORD    =  "3620Gellik"

def create():
    folderName = str(sys.argv[1])
    os.mkdir(PATH + str(folderName))

    user = Github(USERNAME, PASSWORD).get_user()
    user.create_repo(folderName)
    print("Successfully created repository & folder called -->{}".format(folderName))

if __name__ == "__main__":
    create()    