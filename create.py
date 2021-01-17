import sys
import os
from github import Github

PATH        = "/Users/jordi/Documents/Coding Projects/"

USERNAME    = "Jordi-Jaspers"
PASSWORD    = "3620Gellik"
OAUTH       = "2096304fa2d06f2489ec9b18b5957f662e589131"

def create():
    folderName = str(sys.argv[1])
    os.mkdir(PATH + str(folderName))

    user = Github(OAUTH).get_user()
    user.create_repo(folderName)
    
    print("Successfully created repository & folder called --> '{}' ".format(folderName))

if __name__ == "__main__":
    create()    