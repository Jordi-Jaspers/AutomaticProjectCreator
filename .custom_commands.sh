#!/bin/bash

# prints the input
function create() {
    cd
    python create.py $1
    cd  "/Users/jordijaspers/Google\ Drive/Coding\ Projects/$1"
    #git init
    #git remote add origin git@github:34105935+Jordi-Jaspers@users.noreply.github.com/$1.git
    #touch README.md
    #git add .
    #git commit -m "Initial Commit"
    #git push -u origin master
    #code .
}