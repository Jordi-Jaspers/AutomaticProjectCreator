import sys
import os
import shutil
from github import Github

PATH        = "/Users/jordi/Documents/Coding Projects/"
USERNAME    = "Jordi-Jaspers"
PASSWORD    = "3620Gellik"
OAUTH       = "2096304fa2d06f2489ec9b18b5957f662e589131"

def delete():
  repoExist =  bool(True)

  folderName = str(sys.argv[1])
  user = Github(OAUTH).get_user()

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