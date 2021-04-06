#!/bin/bash

function create() {
    if [[ $1 == "" ]] then
        echo "ERROR 404: No Arguments Found."
    else
        cd 
        mkdir "/Users/jordi/Documents/Coding Projects/$1"
        cd  "/Users/jordi/Documents/Coding Projects/$1"

        echo "Initializing Repository."
        git init
        git remote add origin https://github.com/Jordi-Jaspers/$1.git
        git remote -v

        echo "Initializing Repository."
        touch README.md
        touch .gitignore
        git add .

        echo "Commiting and pushing to github."
        git commit -m "Initial Commit"
        git push --set-upstream origin master
        code .

        echo "Status 200: Done!"
}

function delete() {
    if [[ $1 == "" ]] then
        echo "ERROR 404: No Arguments Found."
    else
        cd 
        python3 "/Users/jordi/Documents/Coding Projects/AutomaticProjectCreator/delete.py" $1
}

function gitcm() {
    if [[ $1 == "" ]] then
        echo "ERROR 404: No Arguments Found."
    else
        branch=$(git branch | sed -n -e "s/^\* \(.*\)/\1/p")
        echo "GIT LOG: Checking the status for the following branch - $branch"
        git status

        echo "GIT LOG: Adding & Committing files to current branch"
        story=${branch:8:12}

        # echo "$story: $1"
        git add .
        git commit -m "$story: $1"
    fi
}