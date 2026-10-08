import subprocess
import sys
import duckdb
import streamlit as st

@st.cache_data(ttl=3600/2)
def refresh_data():
    for script in ["fetch.py", "clean.py", "metrics.py"]:
        subprocess.run([sys.executable, script], check=True)


with st.spinner("Updating data..."):
    refresh_data()

st.set_page_config(layout="wide")

st.title("Fixture Difficulty Grader")
st.write(
    "How hard is each Premier League team's next fixture? Each team is scored out of 100 "
    "from the opponent's form, league performance and goal difference, the head to head "
    "record, and whether the game is at home or away. A higher score means a harder fixture."
)

con = duckdb.connect("data/grader.duckdb", read_only=True)
df = con.sql("SELECT * FROM fixture_grader ORDER BY difficulty").df()


def colour(score):
    if score < 20:
        return "background-color: darkgreen; color: white"
    elif score < 40:
        return "background-color: green; color: white"
    elif score < 60:
        return "background-color: yellow; color: black"
    elif score < 80:
        return "background-color: red; color: white"
    return "background-color: darkred; color: white"


styled = (
    df.style.map(colour, subset=["difficulty"])
    .format("{:.3g}", subset=df.select_dtypes("number").columns)
)

legend = [
    ("darkgreen", "white", "0-20 Very easy"),
    ("green", "white", "20-40 Easy"),
    ("yellow", "black", "40-60 Medium"),
    ("red", "white", "60-80 Hard"),
    ("darkred", "white", "80-100 Very hard"),
]

cols = st.columns(5)
for col, (bg, fg, label) in zip(cols, legend):
    col.markdown(
        f"<div style='background:{bg};color:{fg};padding:8px;"
        f"text-align:center;border-radius:6px'>{label}</div>",
        unsafe_allow_html=True,
    )

st.dataframe(styled, use_container_width=True, hide_index=True, height=740)

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
