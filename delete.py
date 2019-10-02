import sys
import os
import shutil
from github import Github

PATH                = "/Users/jordi/Google Drive/Coding Projects/"
USERNAME    = "USERNAME"
PASSWORD    =  "PASSWORD"

def delete():
  repoExist =  bool(True)

  folderName = str(sys.argv[1])
  user = Github(USERNAME, PASSWORD).get_user()

  try:
    repo = user.get_repo(folderName)
  except:
    print("Error 404: Repo called {} not found!".format(folderName))
    repoExist =  bool(False)

  if  repoExist:
    try:
      shutil.rmtree(PATH + str(folderName))
      repo.delete()
    except OSError as e:
      print ("Error: %s - %s." % (e.filename, e.strerror))
    
    print("Successfully deleted repository & folder called -->{}".format(folderName))

if __name__ == "__main__":
    delete()