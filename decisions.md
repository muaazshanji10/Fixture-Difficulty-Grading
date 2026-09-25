#### Plan 1
- Load in the API key into VSCODE
- Understand what data we have available to us
- Understand how it is structured

#### Pipeline 1
- Firstly, I had to load in the API key in a way in which it never gets uploaded to git as I don't want people to have access to it. This is because it is unique to me and how my project consistently accesses the website data.
- I created a file called .gitignore to instruct git to ignire a file called .env which contained my API key.
- Git repositry didn't contain ".env" helped to confirm it wasn't being read.
- Had to download a python package onto my repositry and so added that to gitignore.
- Loaded in the API key with particular notation, as advised on the website. It asks for headers to be enveloped in a particular way.
- Free plan notes that Premier league is included, however when attempting to access it it states that it isn't.
- Queired to find what competitions are included and it says it is.
- Everything worked having recommitted, I assume this was what fixed the error code, I think there was a difference in what the key was being named as because I renamed and removed a capital letter.
- Loading in API and printing a stsus then the actual data
- Loaded in matches and standings, both returning full current season
- Now going to look at the structure better and try to understand how things are 
- Indented data to make it readable and printed keys of the data since it was clearly a bunch of nested dictionaries
