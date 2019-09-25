import sys
import os
from github import Github

path = "/Users/jordijaspers/Google\ Drive/Coding\ Projects/"

def create():
    folderName = str(sys.argv[1])
    os.mkdir(path + str(folderName))

if __name__ == "__main__":
    create()    