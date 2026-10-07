import duckdb
import streamlit as st

st.title("Fixture Difficulty Grader")
st.write(
    "How hard is each Premier League team's next fixture? Each team is scored out of 100 "
    "from the opponent's form, league performance and goal difference, the head to head "
    "record, and whether the game is at home or away. A higher score means a harder fixture."
)

con = duckdb.connect("data/grader.duckdb", read_only=True)
df = con.sql("SELECT * FROM fixture_grader ORDER BY difficulty").df()


def colour(score):
    if score < 35:
        return "background-color: darkgreen; color: white"
    elif score < 45:
        return "background-color: green; color: white"
    elif score < 55:
        return "background-color: yellow; color: black"
    elif score < 65:
        return "background-color: red; color: white"
    return "background-color: darkred; color: white"


styled = (
    df.style.map(colour, subset=["difficulty"])
    .format("{:.3g}", subset=df.select_dtypes("number").columns)
)
st.dataframe(styled)

st.subheader("How the score is calculated")
st.markdown(
    """
| Metric | Weight | How it's scored |
|---|---|---|
| Opponent's form | 0.30 | Points from their last 5 games, out of 15 |
| Opponent's league performance | 0.30 | Points per game this season |
| Head to head | 0.20 | Your team's points per game against them over the last 6 meetings, flipped so a worse record means harder |
| Opponent's goal difference | 0.10 | Ranked 1-20, best gets the full weight |
| Home or away | 0.10 | 0.36 if at home, 0.64 if away |
"""
)