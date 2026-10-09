# Fixture Difficulty Grader

### Introduction
For my project I will be presenting "Fixture Difficulty Grader" which will essentially pull a football team's next match and colour grade how hard it's going to be based off many well reasoned metrics. A few examples include: head to head record, home or away, form coming into the game, fixture congestion and a few more. This tool will mainly be useful for FPL (Fantasy premier league) managers who want to adapt their team before a game to maximise their points. FPL is essentially a game where you create a mini team of players from across the premier league and based off of their performance and team performance each player earns points and your weekly total points get tallied, allowing you to compete in mini leagues with friends and family. I decided to use an API from "https://www.football-data.org". I plan to pull all the data from the website and structure it cleanly, then build justified metrics from what I see available to me which will inform me how difficult a teams next fixture is about to be. The intent is for it to be as accurate as possible with a check being conducted in the future improvements section, where I compare my model to "The Athletic" who have a similar model. I will then conduct a short case study breaking down similarities and gaps for future improvement.

### About me & Motives For Applying
My name is Muaaz Shanji, I have just graduated from Physics at UCL securing a 2:1 in September 2026. Throughout my degree I worked part time at Apple as a product specialist where my love for consulting and aiding people towards solutions first surfaced. I am very social person, I love an extended conversation where I get to know and understand someone well. I'm very active with gym and running being a huge passion of mine, I'm currently rehabilitating from an injury with plans to run a marathon next year. I'm also a huge football fan and have taken a particular interest in seeing how clubs that are overachieving are doing so because of the data available to them. This is a strong reason why I have a huge interest in data. Seeing clubs structure frameworks and models to sign players for cheap due to their data being an outlier in particular metrics, they are able to progress without having to compete financially. The power of organising data and transforming it to view it in a way which may not have been visible before allows for such large gains like this in football, so it must be the same in every industry. I don't have the experience of building a full API pipeline end to end but I am a very fast learner especially with something I'm this passionate about. As evidence I have begun creating a football consultant for football teams that analyses what the best player was over the course of a season from a particular language prompt. I hope my passion and willingness to learn comes across throughout this process.

### Plan & Scope
##### Scope
- I intend to load in the API and see what data I have access to so that I know what metrics we can build the rating from
- I intend to understand the structure of the data sent by the API - as in the pagination, rate limits and authentication.
- I will save the raw API data
- I plan on then transforming it into a clean table, ensuring everything is clearly labelled and runs smoothly.
- Once in a cleaner format I will query the data and set metrics that translate to a difficulty grader
- This will be accessible via a streamline website
- Throughout this process I will be justifying every decision in relevant sections (data source, pipeline, how to run, future improvements, how did Ai help), refer to decisions.md for a more comprehensive breakdown and step by step pipeline.

### Data Source
I had a few data sources to choose from for my chosen brief. I had a few things to consider, firstly whether the API was actually free - many claimed to be free but open more rigorous investigation only offered very basic stats for free. Secondly, identifying what the rate limit was and whether the calling of data was was fast enough - both of these things in the forefront of my mind as I'm considering a targeted audience who will probably be slightly younger, impatient and frustrated since the threat of a forfeit for scoring badly in FPL looms over them. Many didn't specify a rate limit too. Thirdly, whether authentication was required every time the API key was accessed - I wanted to ensure this was the case having read the project brief to demonstrate the ability to handle a more complex system. Having accounted for all things, despite the plethora of options - some perhaps giving more detailed and tailored stats for a better "difficulty" metric - I decided to use the API from "https://www.football-data.org". This was a free source that had a clear rate limit of 10 per minute and caught my eye since it specified immediately roughly how fast data would be called. It also required authentication and wasn't pre-packaged or aligned with what my project scope was. What I mean by that is, there are many FPL API keys out there with more data but very well structured and with their own difficulty scores and so it defeated the project brief of demonstrating the capability to clean and structure the data myself. This did mean however, there would likely be a few less particular stats to contribute to the difficulty grader, like injuries. I trusted that my knowledge of the sport should mean I was able to work around this and create sufficient metrics with the data available to me to build an accurate grader. 

### How AI helped
- I read the brief of the project that information lab wants us to create and utilised Claude to understand the nuances of what is expected of us by defining key terms I was unaware of (pagination, rate limits and how an API actually works) and understanding their impacting. From it I understood that they want us to use an API to download data into GitHub unchanged, then clean the data into a clean consistent form accounting for the different defects. At that point it is expected of us to then build something useful for a clearly defined audience with a README, explaining the entire project. Ensuring to explain cohesively how everything works, through daily commits.
- Used it to understand authentication concepts (headers, tokens) and debug a real bug where my API key was loading as None due to a naming mismatch between my .env file and my code — I diagnosed and fixed this myself once I understood what to check.
- Learned the general shape of an authenticated API request (headers, GET calls, status codes) through explanation and small unrelated examples, then wrote my own extraction code against football-data.org's actual endpoints.
- Learned to inspect a large JSON response progressively (checking top-level keys, then count, then one example) rather than dumping the whole thing - this is now how I explore and save raw API data in the pipeline itself.
- Used AI to teach me what duckDB was and how to install it
- I used Claude to understand why I couldn't filter using the column aliases I'd just created in the same SELECT, which led me into SQL's actual execution order (FROM then WHERE then SELECT) rather than just being told to move the condition and accepting it blindly.
- Learned what a window function actually is through ROW_NUMBER(), and specifically why ROW_NUMBER() rather than RANK() was the right choice here, since RANK() would let tied dates distort the count away from exactly 5 games.
- Learned what a CTE actually is through the WITH x AS (...) syntax I'd already been writing without knowing its name, and that chaining a second one (ranked) uses a comma under the same single WITH, not a second WITH.
- Rather than attempting all of this directly on the real 380-match dataset, I practiced the whole reshape -> rank -> filter -> sum pattern on a small made-up dataset first, which let me catch my own mistakes (missing commas, wrong CASE structure, comparing against the wrong case-sensitive string) somewhere small enough to check the right answer by hand before trusting it on the real data.
- I find it far more structured to work in intense smaller bursts when it comes to thinking and reasoning through complex ideas. Throughout my degree I've come to understand exactly how I learn and work best and so I think and plan on exactly what needs to be done, then I write it down and tell the AI my thoughts and plans and once I've completed everything I use it as a second pair of eyes to scrutinse my work and ensure I haven't missed anything I set out to do.
- If errors existed that I couldn't work out, I would use AI to aid in debugging. However, I wouldn't make it tell me exactly what was wrong as that wouldn't allow me to build the necessary prblem skills when the same or similar issue arose. I would let it prompt me into thinking about particular parts of my code/SQL structure which may be causing an error and get it to make me justify my decision allowing me to reach well reasoned conclusions over why errors were occuring.
- Used Claude to understand how a Streamlit app actually works. I learned that it is a normal Python script where each st. call draws something on the page, and that the whole file reruns from top to bottom every time the page is refreshed. I practised on a small made up table first so I could see how the pieces fit together before touching my own data.
- Learned how to get my DuckDB table into the app. con.sql() returns a query result which has to be converted into a pandas DataFrame with .df() before Streamlit can display it, and the app should open the database file as read only. I found this out when my notebook was still holding the file and Streamlit gave me a lock error.
- Learned how to colour the table through the pandas styler, by writing a function that takes a difficulty score and returns a colour, then applying it to just the difficulty column.
- Used it to understand the environment problems I hit. My terminal was using my other project's virtual environment so Python couldn't find streamlit, which taught me the difference between .venv (a private folder of packages for one project) and .env (my hidden API key), and between installing a package once and starting the app each time with streamlit run.
- I didn't know how to make the website refresh itself with current data, so I asked Claude. It explained that refreshing the page only re-runs the Streamlit file and not my fetch, clean and metrics scripts, and it taught me the options (a scheduled job on GitHub versus running the scripts from the app itself). I chose to run them from the app and cache the result, and Claude gave me the code for this part, using `subprocess` to run the three scripts and `st.cache_data` to stop it running on every refresh. I then went through it until I understood what each line did, and I tested it myself.
- I wasn't sure how to prove my project works for someone else, so I asked Claude to explain the fresh clone test. It taught me what a clone is (a copy of the repo that only contains what's on GitHub), why a virtual environment and `requirements.txt` are needed so the packages match, and why I should test in a separate folder with only the README steps. Claude also helped me write the "How to run" section of my README, and I will follow it step by step on a clean clone to check it works.

## How to run it

You can use the live app at (https://fixture-difficulty-grading-cxwttqbkmmsq7wywqi93jh.streamlit.app) with nothing to install. To run it yourself:

**1. Clone the repo and open the folder**
```bash
git clone https://github.com/muaazshanji10/fixture-difficulty-grading.git
cd fixture-difficulty-grading
```

**2. Create a virtual environment and install the packages**
```bash
python -m venv .venv
source .venv/bin/activate        
pip install -r requirements.txt
```

**3. Add your API key**

Get a free key from [football-data.org](https://www.football-data.org/client/register). Copy `.env.example` to a new file called `.env` and put your key in it:
```
football_data_api_key=your-key-here
```
`.env` is git-ignored so the key never reaches GitHub.

**4. Run the app**
```bash
python -m streamlit run streamlit_app.py
```
It opens at `http://localhost:8501`. The first load takes about 30 seconds because the app runs the pipeline itself before showing the table. After that the data is cached for 30 minutes.

### What the app runs, in order
1. `fetch.py` downloads Premier League matches (current and past seasons) and the current standings from the API into `data/raw/`. Past seasons are only downloaded once, and the current ones are fetched fresh each run.
2. `clean.py` loads the raw JSON into DuckDB and cleans it into `matches_clean` and `standings_clean`.
3. `metrics.py` builds the form and head-to-head tables, then the final `fixture_grader` table with the 0-100 difficulty score.
4. `streamlit_app.py` reads `fixture_grader` and shows the colour-graded table.

You can also run steps 1-3 yourself, in this order, with `python fetch.py`, `python clean.py`, `python metrics.py`.

### Troubleshooting
- **403 error from the API:** your key is missing or wrong. Check `.env`.
- **DuckDB lock error:** something else (like a notebook) has `data/grader.duckdb` open. Close it and try again.
- **`No module named ...`:** make sure the virtual environment is activated and you ran `pip install -r requirements.txt`.

### Future Improvements
- Plan the data source testing better. I had trusted much of what was on the website for the data available to me. If I had begun by testing the limits of the data I would have perhaps had more accurate metrics like injuries and fixture congestion and not been limited for head to head form for example. Beginning by exhausting the limits of the data available to me is an important lesson for next time, and would have better shaped what API and data source I ended up using.
- Had I more time in the future in order to produce a more accurate result, I would've focused more on the accuracy of the statistics and been more thorough in the data science scrutiny that went behind justifying the stats. 
- In my introduction I said I would compare my model to The Athletic’s. I instead compared it to the official FPL Fixture Difficulty Rating, since that’s what FPL managers actually use and I could read it directly. I used Spearman’s rank correlation. Spearman’s ignores the actual numbers, ranks every fixture from hardest to easiest in each model, then measures how closely those two rankings line up. It gives a score from -1 (completely opposite order) to 1 (identical order). I chose it because the two models aren’t on the same scale. Mine is a 0-100 score and the FPL only uses 2 to 5, so comparing raw values would have been meaningless. What I care about is whether we agree on which fixtures are harder. I compared the 20 gameweek 6 fixtures and got a Spearman score of 0.59 (p = 0.006), so the agreement is very unlikely to be down to chance. The FPL only has four grades with lots of ties, so the best any model could score against it is about 0.92, which means I reached roughly 64% of the maximum. Every disagreement was only one grade out. The catch is that simply ranking by the opponent’s league points scores 0.57, and my grader’s ranking matches that table at 0.975, so my extra metrics weren’t adding much. Looking back, my form metric was identical to the opponent’s points, so it was counting league position twice rather than looking at their last 5 games. My conclusion is that the grader is moderately similar to the FPL and captures real difficulty, but it isn’t yet better than a simple league table.