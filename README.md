# Fission_Assistant
Platform9 Hackathon Project

# create nodejs docker image with the package.json and Dockerfile in this path
docker build -t <repo>/nodejs env/

# create nodejs environment with the package.json and Dockerfile in this path
fission environment create --name nodejs --image <repo>/nodejs

# create function with the index.js in functions directory
fission function create --name silly-name --env nodejs-google-action-3 --code index.js

# create http route with POST for this function
fission route create --function silly-name --method POST --url /sillyname

# finally use the relative path in "fulfillment" -> "webhook" section of dialogFlow app.

# another python function with a slightly better use-case 
fission environment create --name python --image fission/python-env
fission function create --name githubissue --env python --code github.py
fission route create --function githubissue --method POST --url /githubissue
