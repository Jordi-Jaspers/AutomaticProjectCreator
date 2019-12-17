#!/bin/bash

function create() {
    cd 
    python3 "/Users/jordi/Google Drive/Coding Projects/AutomaticProjectCreator/create.py" $1
    cd  "/Users/jordi/Google Drive/Coding Projects/$1"
    git init
    git remote add origin https://github.com/"YOUR_GITHUB_HERE"/$1.git
    touch README.md
    git add .
    git commit -m "Initial Commit"
    git push -u origin master
    code .
}

function delete() {
    cd 
    python3 "/Users/jordi/Google Drive/Coding Projects/AutomaticProjectCreator/delete.py" $1
}
