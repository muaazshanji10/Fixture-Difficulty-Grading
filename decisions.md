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
