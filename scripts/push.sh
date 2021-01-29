#!/bin/bash

echo "Pushing Repo $1 to Mirror"
cd $1".git"
git push --mirror $2