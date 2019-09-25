# Author:  
Jordi Jaspers  
  
# Date of initial commit:  
25/09/2019   
  
# AutomaticProjectCreator [Biography]:  
Creating a shell script and a python script for an UNIX terminal that will automate the process of creating new projects and link them to github. Creating custom commands that creates folders, adds it to my desired directory, opens a web browser, navigates to GitHub, logs in to my account, creates a new repository, then adds the git remote to my local folder, adds a README file, git add and then does a commit called “initial commit”. Finally it then pushes this to master and opens the project folder in VSCode.  
  
# What I Learned:  
* Use of shell-commands  
* Creation of custom-commands  
* Automating the browser-Tasks with Python  
* Use of Git-commands with Python  
  
# TODO-List:  
- Navigate to my projects  
- Folder Creation with given project name  
- navigate into that folder  
- git init  
- go to GitHub and create the repo  
- copy the repo remote link  
- initiate the link in terminal  
- add the remote link to the folder  
- Create Readme.md file  
- git add  
- git commit  
- git push  
- code .  
  
# Installation:  
Open Terminal & type the following commands:  
1. git clone "https://github.com/Jordi-Jaspers/AutomaticProjectCreator.git"  
2. cd AutomaticProjectCreator  
3. pip install -r python_add-ons.txt  
4. cp .custom_commands.sh ~  
5. cd ~  
6.1 nano .bash_profile (for mac)  
6.2 nano .bashrc (for windows)  
  
Add the following line to this file:  
7. source ~/.my_commands.sh  
  
Then go to create.py and set the username and password to be your username and password.
Also make sure to change all directories to your directories so it should be '/Users/<your username>/path/to/your/project'
  
# Usage:  
To run the script type in 'create <name of your folder>'  
  
# References:  
https://medium.com/devnetwork/how-to-create-your-own-custom-terminal-commands-c5008782a78e 
  
https://superuser.com/questions/147043/where-to-find-the-bashrc-file-on-mac-os-x-snow-leopard-and-lion  

