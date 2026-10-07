import duckdb
import streamlit as st

con = duckdb.connect("data/grader.duckdb", read_only=True)
df = con.sql("SELECT * FROM fixture_grader").df()
st.dataframe(df)

