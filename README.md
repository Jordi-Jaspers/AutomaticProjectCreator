# AutomaticProjectCreator 

## Biography  
**Authors:**
Jordi Jaspers [[Github](https://github.com/Jordi-Jaspers "Github Page"), [Linkedin](https://www.linkedin.com/in/jordi-jaspers/ "Linkedin Page")] 
  
**Date of initial commit:**
25/09/2019 

**Description:**
Creating a shell script and a python script for an UNIX terminal that will automate the process of creating new projects and link them to github. Creating custom commands that creates folders, adds it to my desired directory, opens a web browser, navigates to GitHub, logs in to my account, creates a new repository, then adds the git remote to my local folder, adds a README file, git add and then does a commit called “initial commit”. Finally it then pushes this to master and opens the project folder in VSCode.  

## What We Learned
* Use of shell-commands  
* Creation of custom-commands  
* Automating the browser-Tasks with Python  
* Use of Git-commands with Python  
  
## TODO-List:  
- Navigate to my projects  --> ok!  
- Folder Creation with given project name  --> ok!  
- navigate into that folder  -> ok!  
- git init  -> ok!  
- go to GitHub and create the repo  -> ok!  
- copy the repo remote link  -> ok!  
- initiate the link in terminal  -> ok!  
- add the remote link to the folder  -> ok!  
- Create Readme.md file  -> ok!  
- git add  -> ok!  
- git commit  -> ok!  
- git push  -> ok!  
- code .  -> ok!  
- Method to remove repo's from the website. -> ok!
- Clean up folders in finder. --> ok!
  
## Installation:  
**1. Open Terminal & type the following commands:**  
  
```
git clone "https://github.com/Jordi-Jaspers/AutomaticProjectCreator.git"
cd AutomaticProjectCreator 
pip install -r python_add-ons.txt 
cp .custom_commands.sh ~
cd ~  
```
  
**Windows users**  
```
nano .bashrc
```
  
**Mac users**  
```
nano .bash_profile
```
  
**2. Add the following line to this file:**  
"source ~/.my_commands.sh"
  
**3. Set Github Credentials**  
Go to create.py and set the username and password to be your username and password.
Also make sure to change all directories to your directories so it should be '/Users/<your username>/path/to/your/project'
  
**4. Open VSCode and type:**  
```
Shell and select "Shell Command : Install code in PATH" 
```
  
**5. Enter password.**   
  
## Troubleshooting:  
It can occur that the terminal gives the following error: "no module named github" try using another pip install. it is probably in the wrong path.  
    
## Usage:  
To run the script type in 'create <name of your folder>'  
  
## References:  
Terminal-commands: <https://medium.com/devnetwork/how-to-create-your-own-custom-terminal-commands-c5008782a78e>
Bashrc Location: <https://superuser.com/questions/147043/where-to-find-the-bashrc-file-on-mac-os-x-snow-leopard-and-lion>
Insperation: <https://github.com/KalleHallden/>

