import streamlit as st
from data_reader import read_matches
from analysis import calculate_advanced_standings, generate_enhanced_analysis
from predictor import predict_enhanced_matches, calculate_final_standings
import graphics

st.set_page_config(page_title="Soccer Standings Explorer", layout="wide")

matches = read_matches('data1.txt')
current_standings = calculate_advanced_standings(matches)
predicted_matches = predict_enhanced_matches(current_standings, matches)
final_standings = calculate_final_standings(current_standings, predicted_matches)

team_names = [team['name'] for team in current_standings]
team_analyses = {team['name']: generate_enhanced_analysis(team, current_standings) for team in current_standings}

tab1, tab2, tab3, tab4 = st.tabs(["Current Standings", "Predicted Final", "Team Analysis", "Team Comparison"])

with tab1:
    st.header("Current Standings")
    st.dataframe(current_standings)
    st.plotly_chart(graphics.plot_standings_interactive(current_standings, "Current Standings"), use_container_width=True)

with tab2:
    st.header("Predicted Final Standings")
    st.dataframe(final_standings)
    st.plotly_chart(graphics.plot_standings_interactive(final_standings, "Predicted Final Standings"), use_container_width=True)

with tab3:
    st.header("Team Analysis")
    selected_team = st.selectbox("Select a team", team_names)
    analysis = team_analyses[selected_team]
    st.write(f"### {selected_team}")
    st.write("**Analysis:**", analysis)
    st.plotly_chart(graphics.plot_team_radar_interactive(analysis, team_name=selected_team), use_container_width=True)

with tab4:
    st.header("Team Comparison")
    team1 = st.selectbox("Select first team", team_names, key="team1")
    team2 = st.selectbox("Select second team", [n for n in team_names if n != team1], key="team2")
    analysis1 = team_analyses[team1]
    analysis2 = team_analyses[team2]
    st.write(f"**{team1}** vs **{team2}**")
    st.plotly_chart(graphics.plot_comparison_interactive(analysis1, analysis2, team1, team2), use_container_width=True)

st.info("Tip: Use the tabs above to explore the data and dive deep into each team!")