#### Plan 1
- Load in the API key into VSCODE
- Understand what data we have available to us
- Understand how it is structured

#### Pipeline
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
- From first calling the data it is clear that there is no pagination when data is requested since all 380 games are outputted. So it may benefit when I do call data to input the ranges as present till next match so that it's cleaner to filter data.
- I needed to look at the rest of the data and begin noting down what my metrics would be. 
- Tried seeing how far back the data went and got data for 2023/24, 2024/25, and 2025/26 seasons which is sufficient data to make a head to head metric.
- Form would be another potential metric, league standing another, goal difference another and home and away another.
- Let's now see if we can attain all that from a matches and standings call.
- Next I wanted to pull data for just one match so that I could see what I had at disposal, to build my metrics. So I decided to use DuckDB an embedded SQL database to see the data more cleanly in a table.
- I printed the data into a table but everything printed as one column, so I needed to query it to ensure columns were cleanly seperated
- I found it easier to look at an indented raw json file to see the data
- I can now see the raw data of one match clearly so I know the keys of the sub dictionaries and then the sub dictionaries in those sub dictionaries. I now need to sql query it to get it into a cleaner form.
- Did the same for standings for one season so I could see things more cleanly and dot chain to get results I actually need, this time I had to unnest the data as I was looking at multiple rows
- from these two cleaned tables we now have: points tally and position which can be rolled into one metric; goal difference which will be scaled into a metric and home or away which will also be its own metric.
- We need to attain form and head to head from the data as it isn't its own category
