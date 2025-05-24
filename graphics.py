import plotly.graph_objects as go

def plot_standings_interactive(standings, title="Standings"):
    teams = [t['name'] for t in standings]
    points = [t['points'] for t in standings]
    goalDiffs = [t['goalDiff'] for t in standings]
    redCards = [t.get('redCardsFor', 0) for t in standings]
    fig = go.Figure()
    fig.add_trace(go.Bar(
        y=teams,
        x=points,
        orientation='h',
        name='Points',
        marker_color='royalblue',
        hovertemplate='Points: %{x}<extra></extra>',
    ))
    fig.add_trace(go.Bar(
        y=teams,
        x=goalDiffs,
        orientation='h',
        name='Goal Diff',
        marker_color='limegreen',
        hovertemplate='Goal Diff: %{x}<extra></extra>',
    ))
    fig.add_trace(go.Bar(
        y=teams,
        x=redCards,
        orientation='h',
        name='Red Cards',
        marker_color='red',
        hovertemplate='Red Cards: %{x}<extra></extra>',
    ))
    fig.update_layout(
        barmode='group',
        title=title,
        xaxis_title="Value",
        yaxis_title="Team",
        height=600,
        template="plotly_white",
        legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1)
    )
    return fig

def plot_team_radar_interactive(analysis, team_name=None):
    if not team_name:
        team_name = "Team"
    metrics = ['formScore', 'offensiveScore', 'defensiveScore', 'consistencyScore', 'disciplineScore', 'mentalStrength']
    labels = ['Form', 'Attack', 'Defense', 'Consistency', 'Discipline', 'Mental']
    values = [analysis[m] for m in metrics]
    # close the loop
    values += values[:1]
    labels += labels[:1]
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=labels,
        fill='toself',
        name=team_name,
        line_color='royalblue'
    ))
    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 1], tickfont=dict(size=12))
        ),
        showlegend=False,
        title=f"Performance Radar: {team_name}",
        height=500,
        template="plotly_white"
    )
    return fig

def plot_comparison_interactive(analysis1, analysis2, team1_name, team2_name):
    metrics = ['formScore', 'offensiveScore', 'defensiveScore', 'consistencyScore', 'disciplineScore', 'mentalStrength']
    labels = ['Form', 'Attack', 'Defense', 'Consistency', 'Discipline', 'Mental']
    values1 = [analysis1[m] for m in metrics] + [analysis1[metrics[0]]]
    values2 = [analysis2[m] for m in metrics] + [analysis2[metrics[0]]]
    labels += [labels[0]]
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values1,
        theta=labels,
        fill='toself',
        name=team1_name,
        line_color='royalblue'
    ))
    fig.add_trace(go.Scatterpolar(
        r=values2,
        theta=labels,
        fill='toself',
        name=team2_name,
        line_color='limegreen'
    ))
    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 1], tickfont=dict(size=12))
        ),
        showlegend=True,
        title=f"Comparison: {team1_name} vs {team2_name}",
        height=500,
        template="plotly_white"
    )
    return fig