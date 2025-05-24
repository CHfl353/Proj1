import React, { useState } from 'react';
import { 
  BarChart, 
  Bar, 
  XAxis, 
  YAxis, 
  CartesianGrid, 
  Tooltip, 
  Legend, 
  ResponsiveContainer, 
  RadarChart, 
  PolarGrid, 
  PolarAngleAxis, 
  PolarRadiusAxis,
  Radar,
  LineChart,
  Line
} from 'recharts';

export default function SoccerStandings() {
  // Enhanced match results with timing and red cards
  const detailedMatches = [
    {
      home: "FC Stockholm Internazionale", away: "Reymersholms IK", homeGoals: 11, awayGoals: 1,
      goals: [
        {minute: 3, team: "home"}, {minute: 17, team: "home"}, {minute: 20, team: "home"}, 
        {minute: 24, team: "home"}, {minute: 31, team: "home"}, {minute: 32, team: "home"},
        {minute: 49, team: "home"}, {minute: 50, team: "home"}, {minute: 75, team: "home"},
        {minute: 82, team: "home"}, {minute: 83, team: "home"}, {minute: 86, team: "away"}
      ],
      redCards: []
    },
    {
      home: "Enskede IK", away: "Bromma TFF", homeGoals: 5, awayGoals: 3,
      goals: [
        {minute: 12, team: "home"}, {minute: 18, team: "home"}, {minute: 37, team: "home"},
        {minute: 43, team: "away"}, {minute: 60, team: "home"}, {minute: 74, team: "away"},
        {minute: 78, team: "away"}, {minute: 86, team: "home"}
      ],
      redCards: []
    },
    {
      home: "Spånga IS FK", away: "BK Karlbergare", homeGoals: 1, awayGoals: 3,
      goals: [
        {minute: 65, team: "home"}, {minute: 74, team: "away"}, 
        {minute: 80, team: "away"}, {minute: 90, team: "away"}
      ],
      redCards: []
    },
    {
      home: "AIK Framtid FK", away: "Hammarby TFF Herrfotboll", homeGoals: 2, awayGoals: 1,
      goals: [
        {minute: 8, team: "home"}, {minute: 9, team: "home"}, {minute: 29, team: "away"}
      ],
      redCards: []
    },
    {
      home: "FK Bromma", away: "Älvsjö AIK FF", homeGoals: 0, awayGoals: 2,
      goals: [
        {minute: 28, team: "away"}, {minute: 45, team: "away"}
      ],
      redCards: []
    },
    {
      home: "Enskede IK", away: "Spånga IS FK", homeGoals: 4, awayGoals: 1,
      goals: [
        {minute: 3, team: "home"}, {minute: 31, team: "away"}, {minute: 50, team: "home"},
        {minute: 62, team: "home"}, {minute: 86, team: "home"}
      ],
      redCards: [{minute: 1, team: "away"}]
    },
    {
      home: "Bromma TFF", away: "AIK Framtid FK", homeGoals: 1, awayGoals: 0,
      goals: [{minute: 19, team: "home"}],
      redCards: []
    },
    {
      home: "Reymersholms IK", away: "FK Bromma", homeGoals: 3, awayGoals: 1,
      goals: [
        {minute: 3, team: "home"}, {minute: 37, team: "home"}, 
        {minute: 39, team: "home"}, {minute: 70, team: "away"}
      ],
      redCards: []
    },
    {
      home: "BK Karlbergare", away: "FC Stockholm Internazionale", homeGoals: 3, awayGoals: 2,
      goals: [
        {minute: 1, team: "home"}, {minute: 23, team: "home"}, {minute: 32, team: "away"},
        {minute: 54, team: "home"}, {minute: 56, team: "away"}
      ],
      redCards: []
    },
    {
      home: "Älvsjö AIK FF", away: "Hammarby TFF Herrfotboll", homeGoals: 2, awayGoals: 1,
      goals: [
        {minute: 13, team: "home"}, {minute: 42, team: "home"}, {minute: 67, team: "away"}
      ],
      redCards: []
    },
    {
      home: "Hammarby TFF Herrfotboll", away: "Bromma TFF", homeGoals: 1, awayGoals: 1,
      goals: [{minute: 45, team: "home"}, {minute: 82, team: "away"}],
      redCards: []
    },
    {
      home: "Spånga IS FK", away: "Älvsjö AIK FF", homeGoals: 2, awayGoals: 4,
      goals: [
        {minute: 14, team: "home"}, {minute: 25, team: "away"}, {minute: 56, team: "away"},
        {minute: 81, team: "away"}, {minute: 89, team: "away"}, {minute: 90, team: "home"}
      ],
      redCards: []
    },
    {
      home: "AIK Framtid FK", away: "Reymersholms IK", homeGoals: 6, awayGoals: 1,
      goals: [
        {minute: 17, team: "home"}, {minute: 20, team: "home"}, {minute: 22, team: "away"},
        {minute: 41, team: "home"}, {minute: 62, team: "home"}, {minute: 65, team: "home"},
        {minute: 73, team: "home"}
      ],
      redCards: []
    },
    {
      home: "FC Stockholm Internazionale", away: "Enskede IK", homeGoals: 3, awayGoals: 1,
      goals: [
        {minute: 32, team: "home"}, {minute: 42, team: "away"}, 
        {minute: 47, team: "home"}, {minute: 53, team: "home"}
      ],
      redCards: []
    },
    {
      home: "FK Bromma", away: "BK Karlbergare", homeGoals: 1, awayGoals: 5,
      goals: [
        {minute: 26, team: "away"}, {minute: 35, team: "away"}, {minute: 65, team: "away"},
        {minute: 69, team: "home"}, {minute: 72, team: "away"}, {minute: 89, team: "away"}
      ],
      redCards: []
    },
    {
      home: "Reymersholms IK", away: "Hammarby TFF Herrfotboll", homeGoals: 2, awayGoals: 4,
      goals: [
        {minute: 4, team: "away"}, {minute: 7, team: "away"}, {minute: 48, team: "away"},
        {minute: 52, team: "home"}, {minute: 76, team: "away"}, {minute: 88, team: "home"}
      ],
      redCards: []
    },
    {
      home: "Enskede IK", away: "FK Bromma", homeGoals: 3, awayGoals: 4,
      goals: [
        {minute: 8, team: "away"}, {minute: 20, team: "home"}, {minute: 53, team: "home"},
        {minute: 55, team: "away"}, {minute: 61, team: "away"}, {minute: 71, team: "away"},
        {minute: 91, team: "home"}
      ],
      redCards: []
    },
    {
      home: "Spånga IS FK", away: "FC Stockholm Internazionale", homeGoals: 2, awayGoals: 2,
      goals: [
        {minute: 11, team: "away"}, {minute: 14, team: "home"}, 
        {minute: 64, team: "away"}, {minute: 97, team: "home"}
      ],
      redCards: []
    },
    {
      home: "Älvsjö AIK FF", away: "Bromma TFF", homeGoals: 0, awayGoals: 0,
      goals: [],
      redCards: []
    },
    {
      home: "Hammarby TFF Herrfotboll", away: "BK Karlbergare", homeGoals: 1, awayGoals: 1,
      goals: [{minute: 18, team: "away"}, {minute: 60, team: "home"}],
      redCards: []
    },
    {
      home: "AIK Framtid FK", away: "Enskede IK", homeGoals: 1, awayGoals: 2,
      goals: [
        {minute: 36, team: "away"}, {minute: 60, team: "away"}, {minute: 80, team: "home"}
      ],
      redCards: [{minute: 1, team: "home"}, {minute: 2, team: "home"}]
    },
    {
      home: "FK Bromma", away: "Spånga IS FK", homeGoals: 2, awayGoals: 4,
      goals: [
        {minute: 8, team: "away"}, {minute: 21, team: "home"}, {minute: 40, team: "home"},
        {minute: 66, team: "away"}, {minute: 74, team: "away"}, {minute: 79, team: "away"}
      ],
      redCards: []
    },
    {
      home: "FC Stockholm Internazionale", away: "Älvsjö AIK FF", homeGoals: 4, awayGoals: 0,
      goals: [
        {minute: 51, team: "home"}, {minute: 57, team: "home"}, 
        {minute: 74, team: "home"}, {minute: 80, team: "home"}
      ],
      redCards: [{minute: 19, team: "away"}]
    },
    {
      home: "Bromma TFF", away: "Reymersholms IK", homeGoals: 5, awayGoals: 0,
      goals: [
        {minute: 30, team: "home"}, {minute: 47, team: "home"}, {minute: 72, team: "home"},
        {minute: 87, team: "home"}, {minute: 91, team: "home"}
      ],
      redCards: []
    }
  ];

  // Calculate advanced team statistics
  const calculateAdvancedStandings = (matches) => {
    const teams = {};
    
    // Initialize teams
    matches.forEach(match => {
      [match.home, match.away].forEach(teamName => {
        if (!teams[teamName]) {
          teams[teamName] = {
            name: teamName,
            played: 0, wins: 0, draws: 0, losses: 0,
            goalsFor: 0, goalsAgainst: 0, goalDiff: 0, points: 0,
            earlyGoals: 0, lateGoals: 0, firstHalfGoals: 0, secondHalfGoals: 0,
            redCardsFor: 0, redCardsAgainst: 0,
            matchesWithRedCards: 0, pointsWithRedCards: 0, pointsWithoutRedCards: 0,
            gamesWithRedCards: 0, gamesWithoutRedCards: 0,
            averageGoalsFor: 0, averageGoalsAgainst: 0,
            comebacks: 0, collapsesToDefeat: 0
          };
        }
      });
    });

    // Calculate detailed statistics
    matches.forEach(match => {
      const homeTeam = teams[match.home];
      const awayTeam = teams[match.away];
      
      // Basic stats
      homeTeam.played++;
      awayTeam.played++;
      homeTeam.goalsFor += match.homeGoals;
      homeTeam.goalsAgainst += match.awayGoals;
      awayTeam.goalsFor += match.awayGoals;
      awayTeam.goalsAgainst += match.homeGoals;
      
      // Goal timing analysis
      match.goals.forEach(goal => {
        const team = goal.team === "home" ? homeTeam : awayTeam;
        if (goal.minute <= 15) team.earlyGoals++;
        if (goal.minute >= 75) team.lateGoals++;
        if (goal.minute <= 45) team.firstHalfGoals++;
        else team.secondHalfGoals++;
      });
      
      // Red card analysis
      const homeRedCards = match.redCards.filter(card => card.team === "home").length;
      const awayRedCards = match.redCards.filter(card => card.team === "away").length;
      
      homeTeam.redCardsFor += homeRedCards;
      homeTeam.redCardsAgainst += awayRedCards;
      awayTeam.redCardsFor += awayRedCards;
      awayTeam.redCardsAgainst += homeRedCards;
      
      const matchHasRedCards = homeRedCards > 0 || awayRedCards > 0;
      
      // Points and results
      let homePoints = 0, awayPoints = 0;
      if (match.homeGoals > match.awayGoals) {
        homeTeam.wins++;
        awayTeam.losses++;
        homePoints = 3;
      } else if (match.homeGoals < match.awayGoals) {
        awayTeam.wins++;
        homeTeam.losses++;
        awayPoints = 3;
      } else {
        homeTeam.draws++;
        awayTeam.draws++;
        homePoints = awayPoints = 1;
      }
      
      homeTeam.points += homePoints;
      awayTeam.points += awayPoints;
      
      // Red card impact tracking
      if (matchHasRedCards) {
        homeTeam.matchesWithRedCards++;
        awayTeam.matchesWithRedCards++;
        homeTeam.pointsWithRedCards += homePoints;
        awayTeam.pointsWithRedCards += awayPoints;
        homeTeam.gamesWithRedCards++;
        awayTeam.gamesWithRedCards++;
      } else {
        homeTeam.pointsWithoutRedCards += homePoints;
        awayTeam.pointsWithoutRedCards += awayPoints;
        homeTeam.gamesWithoutRedCards++;
        awayTeam.gamesWithoutRedCards++;
      }
      
      // Comeback/collapse analysis
      let homeLeading = 0, awayLeading = 0;
      let homeScore = 0, awayScore = 0;
      
      match.goals.forEach(goal => {
        if (goal.team === "home") {
          homeScore++;
          if (homeScore > awayScore && awayLeading > 0) {
            homeTeam.comebacks++;
            awayTeam.collapsesToDefeat++;
          }
          homeLeading = homeScore > awayScore ? 1 : 0;
          awayLeading = 0;
        } else {
          awayScore++;
          if (awayScore > homeScore && homeLeading > 0) {
            awayTeam.comebacks++;
            homeTeam.collapsesToDefeat++;
          }
          awayLeading = awayScore > homeScore ? 1 : 0;
          homeLeading = 0;
        }
      });
    });
    
    // Calculate averages and final stats
    Object.values(teams).forEach(team => {
      team.goalDiff = team.goalsFor - team.goalsAgainst;
      team.averageGoalsFor = team.played > 0 ? team.goalsFor / team.played : 0;
      team.averageGoalsAgainst = team.played > 0 ? team.goalsAgainst / team.played : 0;
    });
    
    return Object.values(teams).sort((a, b) => {
      if (a.points !== b.points) return b.points - a.points;
      if (a.goalDiff !== b.goalDiff) return b.goalDiff - a.goalDiff;
      return b.goalsFor - a.goalsFor;
    });
  };

  // Enhanced team analysis with timing and red card factors
  const generateEnhancedAnalysis = (team, standings) => {
    const position = standings.findIndex(t => t.name === team.name) + 1;
    
    // Form analysis
    const formScore = team.played > 0 ? (team.wins * 3 + team.draws) / (team.played * 3) : 0;
    const form = formScore >= 0.7 ? "Excellent" : formScore >= 0.5 ? "Good" : 
                 formScore >= 0.3 ? "Average" : "Poor";
    
    // Timing analysis
    const earlyGoalRatio = team.goalsFor > 0 ? team.earlyGoals / team.goalsFor : 0;
    const lateGoalRatio = team.goalsFor > 0 ? team.lateGoals / team.goalsFor : 0;
    const firstHalfRatio = team.goalsFor > 0 ? team.firstHalfGoals / team.goalsFor : 0;
    
    // Red card impact
    const redCardImpact = team.gamesWithRedCards > 0 ? 
      (team.pointsWithRedCards / team.gamesWithRedCards) - 
      (team.gamesWithoutRedCards > 0 ? team.pointsWithoutRedCards / team.gamesWithoutRedCards : 0) : 0;
    
    // Discipline rating (fewer red cards = better)
    const disciplineScore = Math.max(0, 1 - (team.redCardsFor / Math.max(team.played, 1)) * 2);
    
    // Mental strength (comebacks vs collapses)
    const mentalStrength = team.played > 0 ? 
      (team.comebacks - team.collapsesToDefeat) / team.played : 0;
    
    // Defensive and offensive ratings with timing consideration
    const defensiveScore = team.played > 0 ? 
      Math.max(0, 1 - (team.goalsAgainst / team.played) / 3) : 0;
    const offensiveScore = team.played > 0 ? 
      Math.min(1, (team.goalsFor / team.played) / 3) : 0;
    
    // Consistency based on performance variation
    const consistencyScore = team.played > 0 ? 
      Math.max(0, 1 - Math.abs(team.wins - team.losses) / team.played * 0.5) : 0;
    
    return {
      position, form, formScore: Math.max(0, Math.min(1, formScore)),
      defensiveScore: Math.max(0, Math.min(1, defensiveScore)),
      offensiveScore: Math.max(0, Math.min(1, offensiveScore)),
      consistencyScore: Math.max(0, Math.min(1, consistencyScore)),
      disciplineScore: Math.max(0, Math.min(1, disciplineScore)),
      mentalStrength: Math.max(0, Math.min(1, (mentalStrength + 1) / 2)),
      earlyGoalRatio, lateGoalRatio, firstHalfRatio, redCardImpact,
      timingStrength: (earlyGoalRatio + lateGoalRatio) / 2,
      seasonPrediction: position <= 2 ? "Title contender" : position <= 4 ? "Top 4 finish" : 
                       position <= 6 ? "Mid-table finish" : "Lower-table finish"
    };
  };

  // Enhanced prediction with red card and timing factors
  const predictEnhancedMatches = (standings) => {
    const teams = standings.map(team => team.name);
    const existingPairs = new Set();
    
    detailedMatches.forEach(match => {
      existingPairs.add(`${match.home}-${match.away}`);
    });
    
    const predictions = [];
    const teamAnalyses = {};
    standings.forEach(team => {
      teamAnalyses[team.name] = generateEnhancedAnalysis(team, standings);
    });
    
    for (let i = 0; i < teams.length; i++) {
      for (let j = 0; j < teams.length; j++) {
        if (i !== j) {
          const homeTeam = teams[i];
          const awayTeam = teams[j];
          
          if (!existingPairs.has(`${homeTeam}-${awayTeam}`)) {
            const homeAnalysis = teamAnalyses[homeTeam];
            const awayAnalysis = teamAnalyses[awayTeam];
            
            // Enhanced strength calculation
            const homeStrength = (homeAnalysis.formScore * 0.3) + 
                                (homeAnalysis.offensiveScore * 0.25) + 
                                (homeAnalysis.defensiveScore * 0.25) + 
                                (homeAnalysis.disciplineScore * 0.1) + 
                                (homeAnalysis.mentalStrength * 0.1) + 0.2; // home advantage
            
            const awayStrength = (awayAnalysis.formScore * 0.3) + 
                               (awayAnalysis.offensiveScore * 0.25) + 
                               (awayAnalysis.defensiveScore * 0.25) + 
                               (awayAnalysis.disciplineScore * 0.1) + 
                               (awayAnalysis.mentalStrength * 0.1);
            
            const strengthDiff = homeStrength - awayStrength;
            
            // Predict goals based on team characteristics
            let homeGoals, awayGoals;
            const randomFactor = (Math.random() - 0.5) * 0.4;
            
            if (strengthDiff + randomFactor > 0.3) {
              homeGoals = Math.max(1, Math.round(2 + homeAnalysis.offensiveScore * 2 + Math.random()));
              awayGoals = Math.max(0, Math.round(awayAnalysis.offensiveScore * 1.5 + Math.random() * 0.8));
            } else if (strengthDiff + randomFactor < -0.3) {
              homeGoals = Math.max(0, Math.round(homeAnalysis.offensiveScore * 1.5 + Math.random() * 0.8));
              awayGoals = Math.max(1, Math.round(2 + awayAnalysis.offensiveScore * 2 + Math.random()));
            } else {
              homeGoals = Math.max(0, Math.round(1 + homeAnalysis.offensiveScore + Math.random()));
              awayGoals = Math.max(0, Math.round(1 + awayAnalysis.offensiveScore + Math.random()));
            }
            
            // Red card probability (teams with poor discipline more likely)
            const redCardProbability = (2 - homeAnalysis.disciplineScore - awayAnalysis.disciplineScore) * 0.1;
            const willHaveRedCard = Math.random() < redCardProbability;
            
            predictions.push({
              home: homeTeam,
              away: awayTeam,
              homeGoals,
              awayGoals,
              willHaveRedCard,
              confidence: Math.abs(strengthDiff) * 100
            });
          }
        }
      }
    }
    
    return predictions;
  };

  // Calculate final standings with predictions
  const calculateFinalStandings = (currentStandings, predictions) => {
    const teams = {};
    currentStandings.forEach(team => {
      teams[team.name] = { ...team };
    });
    
    predictions.forEach(match => {
      teams[match.home].played++;
      teams[match.away].played++;
      teams[match.home].goalsFor += match.homeGoals;
      teams[match.home].goalsAgainst += match.awayGoals;
      teams[match.away].goalsFor += match.awayGoals;
      teams[match.away].goalsAgainst += match.homeGoals;
      
      if (match.homeGoals > match.awayGoals) {
        teams[match.home].wins++;
        teams[match.home].points += 3;
        teams[match.away].losses++;
      } else if (match.homeGoals < match.awayGoals) {
        teams[match.away].wins++;
        teams[match.away].points += 3;
        teams[match.home].losses++;
      } else {
        teams[match.home].draws++;
        teams[match.home].points += 1;
        teams[match.away].draws++;
        teams[match.away].points += 1;
      }
    });
    
    Object.keys(teams).forEach(team => {
      teams[team].goalDiff = teams[team].goalsFor - teams[team].goalsAgainst;
    });
    
    return Object.values(teams).sort((a, b) => {
      if (a.points !== b.points) return b.points - a.points;
      if (a.goalDiff !== b.goalDiff) return b.goalDiff - a.goalDiff;
      return b.goalsFor - a.goalsFor;
    });
  };

  // Main calculations
  const currentStandings = calculateAdvancedStandings(detailedMatches);
  const predictedMatches = predictEnhancedMatches(currentStandings);
  const finalStandings = calculateFinalStandings(currentStandings, predictedMatches);
  
  const teamAnalyses = {};
  currentStandings.forEach(team => {
    teamAnalyses[team.name] = generateEnhancedAnalysis(team, currentStandings);
  });
  
  const [activeTab, setActiveTab] = useState('current');
  const [selectedTeam, setSelectedTeam] = useState(null);
  const [compareTeam, setCompareTeam] = useState(null);
  
  const getPositionColor = (position) => {
    if (position <= 2) return 'bg-green-600';
    if (position <= 4) return 'bg-blue-600';
    if (position <= 6) return 'bg-gray-500';
    return 'bg-red-600';
  };
  
  const chartData = currentStandings.map(team => ({
    name: team.name.split(' ').slice(0, 2).join(' '),
    Points: team.points,
    'Goal Difference': team.goalDiff,
    'Red Cards': team.redCardsFor
  }));

  return (
    <div className="p-4 bg-gray-100 rounded-lg">
      {/* Tabs */}
      <div className="flex mb-4 flex-wrap">
        <button 
          className={`px-4 py-2 mr-2 mb-2 rounded-t-lg ${activeTab === 'current' ? 'bg-blue-500 text-white' : 'bg-gray-300'}`}
          onClick={() => setActiveTab('current')}
        >
          Current Standings
        </button>
        <button 
          className={`px-4 py-2 mr-2 mb-2 rounded-t-lg ${activeTab === 'predicted' ? 'bg-blue-500 text-white' : 'bg-gray-300'}`}
          onClick={() => setActiveTab('predicted')}
        >
          Predicted Final
        </button>
        <button 
          className={`px-4 py-2 mr-2 mb-2 rounded-t-lg ${activeTab === 'matches' ? 'bg-blue-500 text-white' : 'bg-gray-300'}`}
          onClick={() => setActiveTab('matches')}
        >
          Predictions
        </button>
        <button 
          className={`px-4 py-2 mr-2 mb-2 rounded-t-lg ${activeTab === 'analysis' ? 'bg-blue-500 text-white' : 'bg-gray-300'}`}
          onClick={() => setActiveTab('analysis')}
        >
          Team Analysis
        </button>
        <button 
          className={`px-4 py-2 rounded-t-lg ${activeTab === 'comparison' ? 'bg-blue-500 text-white' : 'bg-gray-300'}`}
          onClick={() => setActiveTab('comparison')}
        >
          Team Comparison
        </button>
      </div>
      
      <div className="bg-white p-4 rounded-lg shadow-md">
        {activeTab === 'current' && (
          <>
            <h2 className="text-xl font-bold mb-4">Current Standings</h2>
            <div className="overflow-x-auto mb-6">
              <table className="min-w-full bg-white">
                <thead className="bg-blue-600 text-white">
                  <tr>
                    <th className="py-2 px-4 text-left">Pos</th>
                    <th className="py-2 px-4 text-left">Team</th>
                    <th className="py-2 px-4 text-center">MP</th>
                    <th className="py-2 px-4 text-center">W</th>
                    <th className="py-2 px-4 text-center">D</th>
                    <th className="py-2 px-4 text-center">L</th>
                    <th className="py-2 px-4 text-center">GF</th>
                    <th className="py-2 px-4 text-center">GA</th>
                    <th className="py-2 px-4 text-center">GD</th>
                    <th className="py-2 px-4 text-center">Pts</th>
                    <th className="py-2 px-4 text-center">RC</th>
                  </tr>
                </thead>
                <tbody>
                  {currentStandings.map((team, index) => (
                    <tr 
                      key={team.name}
                      className={`${index % 2 === 0 ? 'bg-gray-50' : 'bg-white'} hover:bg-blue-50 cursor-pointer`}
                      onClick={() => setSelectedTeam(team.name)}
                    >
                      <td className="py-2 px-4">
                        <span className={`inline-block w-6 h-6 rounded-full ${getPositionColor(index + 1)} text-white text-center`}>
                          {index + 1}
                        </span>
                      </td>
                      <td className="py-2 px-4 font-medium">{team.name}</td>
                      <td className="py-2 px-4 text-center">{team.played}</td>
                      <td className="py-2 px-4 text-center">{team.wins}</td>
                      <td className="py-2 px-4 text-center">{team.draws}</td>
                      <td className="py-2 px-4 text-center">{team.losses}</td>
                      <td className="py-2 px-4 text-center">{team.goalsFor}</td>
                      <td className="py-2 px-4 text-center">{team.goalsAgainst}</td>
                      <td className={`py-2 px-4 text-center ${team.goalDiff > 0 ? 'text-green-600' : team.goalDiff < 0 ? 'text-red-600' : ''}`}>
                        {team.goalDiff > 0 && '+'}{team.goalDiff}
                      </td>
                      <td className="py-2 px-4 text-center font-bold">{team.points}</td>
                      <td className={`py-2 px-4 text-center ${team.redCardsFor > 0 ? 'text-red-600' : 'text-green-600'}`}>
                        {team.redCardsFor}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
            
            <h3 className="text-lg font-semibold mb-2">Performance Overview</h3>
            <div className="h-64">
              <ResponsiveContainer width="100%" height="100%">
                <BarChart data={chartData}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="name" />
                  <YAxis />
                  <Tooltip />
                  <Legend />
                  <Bar dataKey="Points" fill="#3B82F6" />
                  <Bar dataKey="Goal Difference" fill="#10B981" />
                  <Bar dataKey="Red Cards" fill="#EF4444" />
                </BarChart>
              </ResponsiveContainer>
            </div>
          </>
        )}
        
        {activeTab === 'predicted' && (
          <>
            <h2 className="text-xl font-bold mb-4">Predicted Final Standings</h2>
            <div className="overflow-x-auto">
              <table className="min-w-full bg-white">
                <thead className="bg-green-600 text-white">
                  <tr>
                    <th className="py-2 px-4 text-left">Pos</th>
                    <th className="py-2 px-4 text-left">Team</th>
                    <th className="py-2 px-4 text-center">MP</th>
                    <th className="py-2 px-4 text-center">W</th>
                    <th className="py-2 px-4 text-center">D</th>
                    <th className="py-2 px-4 text-center">L</th>
                    <th className="py-2 px-4 text-center">GF</th>
                    <th className="py-2 px-4 text-center">GA</th>
                    <th className="py-2 px-4 text-center">GD</th>
                    <th className="py-2 px-4 text-center">Pts</th>
                  </tr>
                </thead>
                <tbody>
                  {finalStandings.map((team, index) => {
                    const currentPos = currentStandings.findIndex(t => t.name === team.name) + 1;
                    const posDiff = currentPos - (index + 1);
                    
                    return (
                      <tr 
                        key={team.name}
                        className={`${index % 2 === 0 ? 'bg-gray-50' : 'bg-white'} hover:bg-blue-50`}
                      >
                        <td className="py-2 px-4">
                          <span className={`inline-block w-6 h-6 rounded-full ${getPositionColor(index + 1)} text-white text-center`}>
                            {index + 1}
                          </span>
                          {posDiff !== 0 && (
                            <span className={`ml-2 text-sm ${posDiff > 0 ? 'text-green-600' : 'text-red-600'}`}>
                              {posDiff > 0 ? `↑${posDiff}` : `↓${Math.abs(posDiff)}`}
                            </span>
                          )}
                        </td>
                        <td className="py-2 px-4 font-medium">{team.name}</td>
                        <td className="py-2 px-4 text-center">{team.played}</td>
                        <td className="py-2 px-4 text-center">{team.wins}</td>
                        <td className="py-2 px-4 text-center">{team.draws}</td>
                        <td className="py-2 px-4 text-center">{team.losses}</td>
                        <td className="py-2 px-4 text-center">{team.goalsFor}</td>
                        <td className="py-2 px-4 text-center">{team.goalsAgainst}</td>
                        <td className={`py-2 px-4 text-center ${team.goalDiff > 0 ? 'text-green-600' : team.goalDiff < 0 ? 'text-red-600' : ''}`}>
                          {team.goalDiff > 0 && '+'}{team.goalDiff}
                        </td>
                        <td className="py-2 px-4 text-center font-bold">{team.points}</td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>
          </>
        )}
        
        {activeTab === 'matches' && (
          <>
            <h2 className="text-xl font-bold mb-4">Match Predictions</h2>
            <div className="grid gap-4 grid-cols-1 md:grid-cols-2">
              {predictedMatches.slice(0, 12).map((match, index) => (
                <div key={index} className="border rounded-lg p-3 shadow-sm hover:shadow-md transition-shadow">
                  <div className="flex justify-between items-center mb-2">
                    <div className="font-medium text-sm">{match.home}</div>
                    <div className="text-lg font-bold">{match.homeGoals} - {match.awayGoals}</div>
                    <div className="font-medium text-sm text-right">{match.away}</div>
                  </div>
                  <div className="text-xs text-gray-500 text-center">
                    Confidence: {match.confidence.toFixed(0)}%
                    {match.willHaveRedCard && " • Red card likely"}
                  </div>
                </div>
              ))}
            </div>
          </>
        )}
        
        {activeTab === 'analysis' && (
          <>
            <h2 className="text-xl font-bold mb-4">Team Analysis</h2>
            
            {selectedTeam ? (
              <div className="bg-gray-50 p-4 rounded-lg">
                <h3 className="text-lg font-bold mb-2">{selectedTeam}</h3>
                
                {(() => {
                  const team = currentStandings.find(t => t.name === selectedTeam);
                  const analysis = teamAnalyses[selectedTeam];
                  
                  return (
                    <div>
                      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
                        <div className="bg-white p-3 rounded shadow">
                          <h4 className="font-semibold mb-2">Current Stats</h4>
                          <p><span className="font-medium">Position:</span> {analysis.position}</p>
                          <p><span className="font-medium">Points:</span> {team.points}</p>
                          <p><span className="font-medium">Record:</span> {team.wins}W-{team.draws}D-{team.losses}L</p>
                          <p><span className="font-medium">Goals:</span> {team.goalsFor} scored, {team.goalsAgainst} conceded</p>
                          <p><span className="font-medium">Red Cards:</span> {team.redCardsFor} received</p>
                        </div>
                        
                        <div className="bg-white p-3 rounded shadow">
                          <h4 className="font-semibold mb-2">Advanced Metrics</h4>
                          <p><span className="font-medium">Early Goals:</span> {team.earlyGoals} (≤15 min)</p>
                          <p><span className="font-medium">Late Goals:</span> {team.lateGoals} (≥75 min)</p>
                          <p><span className="font-medium">1st Half Goals:</span> {team.firstHalfGoals}</p>
                          <p><span className="font-medium">Comebacks:</span> {team.comebacks}</p>
                          <p><span className="font-medium">Collapses:</span> {team.collapsesToDefeat}</p>
                        </div>
                      </div>
                      
                      <div className="bg-white p-3 rounded shadow mb-4">
                        <h4 className="font-semibold mb-2">Performance Spider Chart</h4>
                        <div className="h-64">
                          <ResponsiveContainer width="100%" height="100%">
                            <RadarChart outerRadius={90} data={[
                              { subject: 'Form', A: analysis.formScore * 100 },
                              { subject: 'Attack', A: analysis.offensiveScore * 100 },
                              { subject: 'Defense', A: analysis.defensiveScore * 100 },
                              { subject: 'Consistency', A: analysis.consistencyScore * 100 },
                              { subject: 'Discipline', A: analysis.disciplineScore * 100 },
                              { subject: 'Mental Strength', A: analysis.mentalStrength * 100 }
                            ]}>
                              <PolarGrid />
                              <PolarAngleAxis dataKey="subject" />
                              <PolarRadiusAxis angle={90} domain={[0, 100]} />
                              <Radar name="Performance" dataKey="A" stroke="#8884d8" fill="#8884d8" fillOpacity={0.6} />
                              <Tooltip />
                            </RadarChart>
                          </ResponsiveContainer>
                        </div>
                      </div>
                      
                      <div className="bg-white p-3 rounded shadow mb-4">
                        <h4 className="font-semibold mb-2">Detailed Analysis</h4>
                        <p className="mb-2">
                          <strong>Goal Timing:</strong> {team.name} scores {(analysis.earlyGoalRatio * 100).toFixed(1)}% of their goals early in matches and {(analysis.lateGoalRatio * 100).toFixed(1)}% late, showing {analysis.earlyGoalRatio > 0.3 ? 'strong early pressure' : analysis.lateGoalRatio > 0.3 ? 'late game resilience' : 'balanced scoring throughout matches'}.
                        </p>
                        
                        <p className="mb-2">
                          <strong>Discipline:</strong> With {team.redCardsFor} red cards in {team.played} games, they have {team.redCardsFor / team.played < 0.2 ? 'excellent' : team.redCardsFor / team.played < 0.4 ? 'good' : 'poor'} discipline.
                          {team.gamesWithRedCards > 0 && (
                            <span> When playing with red cards, they average {(team.pointsWithRedCards / team.gamesWithRedCards).toFixed(1)} points per game vs {team.gamesWithoutRedCards > 0 ? (team.pointsWithoutRedCards / team.gamesWithoutRedCards).toFixed(1) : 0} points in normal games.</span>
                          )}
                        </p>
                        
                        <p className="mb-2">
                          <strong>Mental Resilience:</strong> {team.name} has made {team.comebacks} comeback(s) and suffered {team.collapsesToDefeat} collapse(s), indicating {team.comebacks > team.collapsesToDefeat ? 'strong' : team.comebacks === team.collapsesToDefeat ? 'average' : 'weak'} mental strength in difficult situations.
                        </p>
                        
                        <p>
                          <strong>Season Outlook:</strong> Based on current performance metrics including timing patterns, discipline record, and mental resilience, {team.name} are projected for a {analysis.seasonPrediction.toLowerCase()}.
                        </p>
                      </div>
                    </div>
                  );
                })()}
              </div>
            ) : (
              <div className="text-center p-6 bg-gray-50 rounded-lg">
                <p className="text-lg mb-4">Select a team to view detailed analysis</p>
                <div className="grid grid-cols-2 md:grid-cols-3 gap-2">
                  {currentStandings.map((team, index) => (
                    <button 
                      key={team.name}
                      onClick={() => setSelectedTeam(team.name)}
                      className="p-2 border rounded-lg hover:bg-blue-100 transition-colors text-sm"
                    >
                      {index + 1}. {team.name}
                    </button>
                  ))}
                </div>
              </div>
            )}
          </>
        )}
        
        {activeTab === 'comparison' && (
          <>
            <h2 className="text-xl font-bold mb-4">Team Comparison</h2>
            {selectedTeam ? (
              <div>
                <div className="mb-4">
                  <label className="block text-sm font-medium mb-1">Compare {selectedTeam} with:</label>
                  <select 
                    className="border rounded p-2 w-full"
                    onChange={(e) => setCompareTeam(e.target.value)}
                    value={compareTeam || ""}
                  >
                    <option value="">Select a team...</option>
                    {currentStandings
                      .filter(t => t.name !== selectedTeam)
                      .map(team => (
                        <option key={team.name} value={team.name}>{team.name}</option>
                      ))
                    }
                  </select>
                </div>
                
                {compareTeam && (
                  <div className="bg-white p-4 rounded-lg shadow">
                    <h3 className="text-lg font-bold mb-4">{selectedTeam} vs {compareTeam}</h3>
                    
                    {(() => {
                      const team1 = currentStandings.find(t => t.name === selectedTeam);
                      const team2 = currentStandings.find(t => t.name === compareTeam);
                      const analysis1 = teamAnalyses[selectedTeam];
                      const analysis2 = teamAnalyses[compareTeam];
                      
                      const radarData = [
                        { subject: 'Form', A: analysis1.formScore * 100, B: analysis2.formScore * 100 },
                        { subject: 'Attack', A: analysis1.offensiveScore * 100, B: analysis2.offensiveScore * 100 },
                        { subject: 'Defense', A: analysis1.defensiveScore * 100, B: analysis2.defensiveScore * 100 },
                        { subject: 'Consistency', A: analysis1.consistencyScore * 100, B: analysis2.consistencyScore * 100 },
                        { subject: 'Discipline', A: analysis1.disciplineScore * 100, B: analysis2.disciplineScore * 100 },
                        { subject: 'Mental Strength', A: analysis1.mentalStrength * 100, B: analysis2.mentalStrength * 100 }
                      ];
                      
                      return (
                        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                          <div>
                            <h4 className="font-semibold mb-2">Statistics Comparison</h4>
                            <table className="w-full border text-sm">
                              <thead className="bg-gray-100">
                                <tr>
                                  <th className="p-2">Metric</th>
                                  <th className="p-2">{team1.name.split(' ')[0]}</th>
                                  <th className="p-2">{team2.name.split(' ')[0]}</th>
                                </tr>
                              </thead>
                              <tbody>
                                <tr><td className="p-2 border-t">Position</td><td className="p-2 border-t text-center">{analysis1.position}</td><td className="p-2 border-t text-center">{analysis2.position}</td></tr>
                                <tr><td className="p-2 border-t">Points</td><td className="p-2 border-t text-center">{team1.points}</td><td className="p-2 border-t text-center">{team2.points}</td></tr>
                                <tr><td className="p-2 border-t">Goal Diff</td><td className="p-2 border-t text-center">{team1.goalDiff}</td><td className="p-2 border-t text-center">{team2.goalDiff}</td></tr>
                                <tr><td className="p-2 border-t">Red Cards</td><td className="p-2 border-t text-center">{team1.redCardsFor}</td><td className="p-2 border-t text-center">{team2.redCardsFor}</td></tr>
                                <tr><td className="p-2 border-t">Early Goals</td><td className="p-2 border-t text-center">{team1.earlyGoals}</td><td className="p-2 border-t text-center">{team2.earlyGoals}</td></tr>
                                <tr><td className="p-2 border-t">Comebacks</td><td className="p-2 border-t text-center">{team1.comebacks}</td><td className="p-2 border-t text-center">{team2.comebacks}</td></tr>
                              </tbody>
                            </table>
                          </div>
                          
                          <div className="h-64">
                            <h4 className="font-semibold mb-2">Performance Comparison</h4>
                            <ResponsiveContainer width="100%" height="100%">
                              <RadarChart outerRadius={80} data={radarData}>
                                <PolarGrid />
                                <PolarAngleAxis dataKey="subject" />
                                <PolarRadiusAxis angle={90} domain={[0, 100]} />
                                <Radar name={team1.name.split(' ')[0]} dataKey="A" stroke="#8884d8" fill="#8884d8" fillOpacity={0.6} />
                                <Radar name={team2.name.split(' ')[0]} dataKey="B" stroke="#82ca9d" fill="#82ca9d" fillOpacity={0.6} />
                                <Legend />
                                <Tooltip />
                              </RadarChart>
                            </ResponsiveContainer>
                          </div>
                        </div>
                      );
                    })()}
                  </div>
                )}
              </div>
            ) : (
              <div className="text-center p-6 bg-gray-50 rounded-lg">
                <p>Please select a team first to begin comparison.</p>
              </div>
            )}
          </>
        )}
      </div>
    </div>
  );
}