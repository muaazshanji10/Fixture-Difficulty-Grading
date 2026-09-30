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
- Queired to find what competitions are included and it says the Premier league is.
- Everything worked having recommitted, I assume this was what fixed the error code, I think there was a difference in what the key was being named as because I renamed and removed a capital letter and so the API wasn't correctly loading in.
- Loading in API and printing a stsus then the actual data
- Loaded in matches and standings, both returning full current season
- Now going to look at the structure better and try to understand how things are 
- Indented data to make it readable and printed keys of the data since it was clearly a bunch of nested dictionaries
- From first calling the data it is clear that there is no pagination when data is requested since all 380 games are outputted. So it may benefit when I do call data to input the ranges as present till next match so that it's cleaner to filter data.
- I needed to look at the rest of the data and begin noting down what my metrics would be.
- Fixture congestion was intended to be a metric however, games outside of the premier are not free and require a subscription for access.
- Tried seeing how far back the data went and got data for 2023/24, 2024/25, and 2025/26 seasons which is sufficient data to make a head to head metric.
- Form would be another potential metric, league standing another, goal difference another and home and away another.
- Let's now see if we can attain all that from a matches and standings call.
- The reason these have been chosen will be explained one by one:
    - Points tally will be the current position of the team in the league and will impact how difficult they are likely to be as a fixture.
    - Form gives FPL users an indication as to how much momentum a team has. It can demonstrate that even if the team isn't doing the best over the season outlook they are in a purple patch which means that they are more likely to win. This contributes to the grader because when teams win in FPL most players get a baseline points tally even despite heavy individual player contribution and so it is often beneficial to have a player from a team likely to win. 
    - Goal difference is another metric and this is used since it can help to paint a broader picture, for players over how good a team actually is. FPL points are boosted for players who are defenders/midfielders and their teams concede no goals. Whilst players who are attackers and have scored many goals get many points too and so these will contribute to deciding whether a fixture is more dfficult or less difficult.
    - Head to head is an important metric since it compensates for the fact that certain games have more than just form or points tally as key contributors. In some games form goes out of the window due to team style clashes, players historically turning up against particular opponents or just general occaions of derbies changing the atmosphere of a game. Therefore accounting for how teams are head to head which we can do off a 6 game and past 3 year basis is an important factor too.
    - Home or away, perhaps the least important but still a signficant factor since across most stats a team performs better at home than away. 
- Next I wanted to pull data for just one match so that I could see what I had at disposal, to build my metrics. So I decided to use DuckDB an embedded SQL database to see the data more cleanly in a table and use SQL to filter out what I didn't need
- I printed the data into a table but everything printed as one column, so I needed to query it to ensure columns were cleanly seperated
- I found it easier to look at an indented raw json file to see the data
- I can now see the raw data of one match clearly so I know the keys of the sub dictionaries and then the sub dictionaries in those sub dictionaries. I now need to sql query it to get it into a cleaner form.
- Did the same for standings for one season so I could see things more cleanly and dot chain to get results I actually need, this time I had to unnest the data as I was looking at multiple rows
- from these two cleaned tables we now have: points tally and position which can be rolled into one metric; goal difference which will be scaled into a metric and home or away which will also be its own metric.
- We need to attain form and head to head from the data as it isn't its own category
- Form was supposed to be attained from the API but it returned NONE and so it is something we are going to have to create ourselves.
- Form will be tricky to attain because teams matches are split across two columns, its not that each team has their name and whether they won its structured home_team or away_team.
- Lets pull up past 5 gameweeks and see how things are structured in our current one match table. I created a new file called Creating_form_code




