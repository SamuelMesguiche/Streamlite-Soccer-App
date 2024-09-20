import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import random

teams = ['Liverpool', 'Arsenal', 'Manchester City', 'Chelsea', 'Manchester United']
data = {
    'Team': teams,
    'Goals Scored': [68, 72, 83, 68, 61],
    'Goals Conceded': [44, 33, 36, 32, 48],
    'Points': [86, 82, 81, 71, 67]
}

df = pd.DataFrame(data)

st.title('Soccer Stats and Predictor')

st.header('Team Statistics')
st.dataframe(df)

st.subheader('Goals Scored by Team')
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(df['Team'], df['Goals Scored'])
plt.xticks(rotation=45, ha='right')
plt.ylabel('Goals Scored')
st.pyplot(fig)

st.header('Match Predictor')
team1 = st.selectbox('Select Home Team', teams)
team2 = st.selectbox('Select Away Team', teams, index=1)

if st.button('Predict Match Outcome'):
    team1_strength = df[df['Team'] == team1]['Points'].values[0]
    team2_strength = df[df['Team'] == team2]['Points'].values[0]
    
    total_strength = team1_strength + team2_strength
    team1_win_prob = team1_strength / total_strength
    
    random_outcome = random.random()
    
    if random_outcome < team1_win_prob:
        result = f"{team1} Wins!"
    elif random_outcome < team1_win_prob + 0.2:  
        result = "It's a Draw!"
    else:
        result = f"{team2} Wins!"
    
    st.success(f"Predicted Outcome: {result}")
    st.info(f"Win probability for {team1}: {team1_win_prob:.2%}")
    st.info(f"Win probability for {team2}: {1-team1_win_prob:.2%}")

st.header('Team Comparison')
team_a = st.selectbox('Select Team A', teams, key='team_a')
team_b = st.selectbox('Select Team B', teams, index=1, key='team_b')

if st.button('Compare Teams'):
    team_a_data = df[df['Team'] == team_a].iloc[0]
    team_b_data = df[df['Team'] == team_b].iloc[0]
    
    comparison_data = pd.DataFrame({
        'Metric': ['Goals Scored', 'Goals Conceded', 'Points'],
        team_a: [team_a_data['Goals Scored'], team_a_data['Goals Conceded'], team_a_data['Points']],
        team_b: [team_b_data['Goals Scored'], team_b_data['Goals Conceded'], team_b_data['Points']]
    })
    
    st.table(comparison_data.set_index('Metric'))
    
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(projection='polar'))
    metrics = ['Goals Scored', 'Goals Conceded', 'Points']
    angles = [n / float(len(metrics)) * 2 * 3.141593 for n in range(len(metrics))]
    angles += angles[:1]
    
    ax.plot(angles, team_a_data[metrics].tolist() + [team_a_data[metrics[0]]], 'o-', linewidth=2, label=team_a)
    ax.fill(angles, team_a_data[metrics].tolist() + [team_a_data[metrics[0]]], alpha=0.25)
    ax.plot(angles, team_b_data[metrics].tolist() + [team_b_data[metrics[0]]], 'o-', linewidth=2, label=team_b)
    ax.fill(angles, team_b_data[metrics].tolist() + [team_b_data[metrics[0]]], alpha=0.25)
    
    ax.set_thetagrids([a * 180/3.141593 for a in angles[:-1]], metrics)
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
    st.pyplot(fig)