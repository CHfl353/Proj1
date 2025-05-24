import json

def read_match_data(filename="data1.txt"):
    """
    Read match data from a local file.
    Expected format: JSON with match details including goals, red cards, and timing.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data.get('matches', [])
    except FileNotFoundError:
        print(f"File {filename} not found. Using default data.")
        return get_default_matches()
    except json.JSONDecodeError:
        print(f"Error parsing JSON from {filename}. Using default data.")
        return get_default_matches()

def get_default_matches():
    """
    Default match data if file reading fails.
    """
    return [
        {
            "home": "FC Stockholm Internazionale",
            "away": "Reymersholms IK",
            "homeGoals": 11,
            "awayGoals": 1,
            "goals": [
                {"minute": 3, "team": "home"}, {"minute": 17, "team": "home"}, {"minute": 20, "team": "home"},
                {"minute": 24, "team": "home"}, {"minute": 31, "team": "home"}, {"minute": 32, "team": "home"},
                {"minute": 49, "team": "home"}, {"minute": 50, "team": "home"}, {"minute": 75, "team": "home"},
                {"minute": 82, "team": "home"}, {"minute": 83, "team": "home"}, {"minute": 86, "team": "away"}
            ],
            "redCards": []
        },
        {
            "home": "Enskede IK",
            "away": "Bromma TFF",
            "homeGoals": 5,
            "awayGoals": 3,
            "goals": [
                {"minute": 12, "team": "home"}, {"minute": 18, "team": "home"}, {"minute": 37, "team": "home"},
                {"minute": 43, "team": "away"}, {"minute": 60, "team": "home"}, {"minute": 74, "team": "away"},
                {"minute": 78, "team": "away"}, {"minute": 86, "team": "home"}
            ],
            "redCards": []
        },
        {
            "home": "Spånga IS FK",
            "away": "BK Karlbergare",
            "homeGoals": 1,
            "awayGoals": 3,
            "goals": [
                {"minute": 65, "team": "home"}, {"minute": 74, "team": "away"},
                {"minute": 80, "team": "away"}, {"minute": 90, "team": "away"}
            ],
            "redCards": []
        },
        {
            "home": "AIK Framtid FK",
            "away": "Hammarby TFF Herrfotboll",
            "homeGoals": 2,
            "awayGoals": 1,
            "goals": [
                {"minute": 8, "team": "home"}, {"minute": 9, "team": "home"}, {"minute": 29, "team": "away"}
            ],
            "redCards": []
        },
        {
            "home": "FK Bromma",
            "away": "Älvsjö AIK FF",
            "homeGoals": 0,
            "awayGoals": 2,
            "goals": [
                {"minute": 28, "team": "away"}, {"minute": 45, "team": "away"}
            ],
            "redCards": []
        },
        {
            "home": "Enskede IK",
            "away": "Spånga IS FK",
            "homeGoals": 4,
            "awayGoals": 1,
            "goals": [
                {"minute": 3, "team": "home"}, {"minute": 31, "team": "away"}, {"minute": 50, "team": "home"},
                {"minute": 62, "team": "home"}, {"minute": 86, "team": "home"}
            ],
            "redCards": [{"minute": 1, "team": "away"}]
        },
        {
            "home": "Bromma TFF",
            "away": "AIK Framtid FK",
            "homeGoals": 1,
            "awayGoals": 0,
            "goals": [{"minute": 19, "team": "home"}],
            "redCards": []
        },
        {
            "home": "Reymersholms IK",
            "away": "FK Bromma",
            "homeGoals": 3,
            "awayGoals": 1,
            "goals": [
                {"minute": 3, "team": "home"}, {"minute": 37, "team": "home"},
                {"minute": 39, "team": "home"}, {"minute": 70, "team": "away"}
            ],
            "redCards": []
        },
        {
            "home": "BK Karlbergare",
            "away": "FC Stockholm Internazionale",
            "homeGoals": 3,
            "awayGoals": 2,
            "goals": [
                {"minute": 1, "team": "home"}, {"minute": 23, "team": "home"}, {"minute": 32, "team": "away"},
                {"minute": 54, "team": "home"}, {"minute": 56, "team": "away"}
            ],
            "redCards": []
        },
        {
            "home": "Älvsjö AIK FF",
            "away": "Hammarby TFF Herrfotboll",
            "homeGoals": 2,
            "awayGoals": 1,
            "goals": [
                {"minute": 13, "team": "home"}, {"minute": 42, "team": "home"}, {"minute": 67, "team": "away"}
            ],
            "redCards": []
        },
        {
            "home": "Hammarby TFF Herrfotboll",
            "away": "Bromma TFF",
            "homeGoals": 1,
            "awayGoals": 1,
            "goals": [{"minute": 45, "team": "home"}, {"minute": 82, "team": "away"}],
            "redCards": []
        },
        {
            "home": "Spånga IS FK",
            "away": "Älvsjö AIK FF",
            "homeGoals": 2,
            "awayGoals": 4,
            "goals": [
                {"minute": 14, "team": "home"}, {"minute": 25, "team": "away"}, {"minute": 56, "team": "away"},
                {"minute": 81, "team": "away"}, {"minute": 89, "team": "away"}, {"minute": 90, "team": "home"}
            ],
            "redCards": []
        },
        {
            "home": "AIK Framtid FK",
            "away": "Reymersholms IK",
            "homeGoals": 6,
            "awayGoals": 1,
            "goals": [
                {"minute": 17, "team": "home"}, {"minute": 20, "team": "home"}, {"minute": 22, "team": "away"},
                {"minute": 41, "team": "home"}, {"minute": 62, "team": "home"}, {"minute": 65, "team": "home"},
                {"minute": 73, "team": "home"}
            ],
            "redCards": []
        },
        {
            "home": "FC Stockholm Internazionale",
            "away": "Enskede IK",
            "homeGoals": 3,
            "awayGoals": 1,
            "goals": [
                {"minute": 32, "team": "home"}, {"minute": 42, "team": "away"},
                {"minute": 47, "team": "home"}, {"minute": 53, "team": "home"}
            ],
            "redCards": []
        },
        {
            "home": "FK Bromma",
            "away": "BK Karlbergare",
            "homeGoals": 1,
            "awayGoals": 5,
            "goals": [
                {"minute": 26, "team": "away"}, {"minute": 35, "team": "away"}, {"minute": 65, "team": "away"},
                {"minute": 69, "team": "home"}, {"minute": 72, "team": "away"}, {"minute": 89, "team": "away"}
            ],
            "redCards": []
        },
        {
            "home": "Reymersholms IK",
            "away": "Hammarby TFF Herrfotboll",
            "homeGoals": 2,
            "awayGoals": 4,
            "goals": [
                {"minute": 4, "team": "away"}, {"minute": 7, "team": "away"}, {"minute": 48, "team": "away"},
                {"minute": 52, "team": "home"}, {"minute": 76, "team": "away"}, {"minute": 88, "team": "home"}
            ],
            "redCards": []
        },
        {
            "home": "Enskede IK",
            "away": "FK Bromma",
            "homeGoals": 3,
            "awayGoals": 4,
            "goals": [
                {"minute": 8, "team": "away"}, {"minute": 20, "team": "home"}, {"minute": 53, "team": "home"},
                {"minute": 55, "team": "away"}, {"minute": 61, "team": "away"}, {"minute": 71, "team": "away"},
                {"minute": 91, "team": "home"}
            ],
            "redCards": []
        },
        {
            "home": "Spånga IS FK",
            "away": "FC Stockholm Internazionale",
            "homeGoals": 2,
            "awayGoals": 2,
            "goals": [
                {"minute": 11, "team": "away"}, {"minute": 14, "team": "home"},
                {"minute": 64, "team": "away"}, {"minute": 97, "team": "home"}
            ],
            "redCards": []
        },
        {
            "home": "Älvsjö AIK FF",
            "away": "Bromma TFF",
            "homeGoals": 0,
            "awayGoals": 0,
            "goals": [],
            "redCards": []
        },
        {
            "home": "Hammarby TFF Herrfotboll",
            "away": "BK Karlbergare",
            "homeGoals": 1,
            "awayGoals": 1,
            "goals": [{"minute": 18, "team": "away"}, {"minute": 60, "team": "home"}],
            "redCards": []
        },
        {
            "home": "AIK Framtid FK",
            "away": "Enskede IK",
            "homeGoals": 1,
            "awayGoals": 2,
            "goals": [
                {"minute": 36, "team": "away"}, {"minute": 60, "team": "away"}, {"minute": 80, "team": "home"}
            ],
            "redCards": [{"minute": 1, "team": "home"}, {"minute": 2, "team": "home"}]
        },
        {
            "home": "FK Bromma",
            "away": "Spånga IS FK",
            "homeGoals": 2,
            "awayGoals": 4,
            "goals": [
                {"minute": 8, "team": "away"}, {"minute": 21, "team": "home"}, {"minute": 40, "team": "home"},
                {"minute": 66, "team": "away"}, {"minute": 74, "team": "away"}, {"minute": 79, "team": "away"}
            ],
            "redCards": []
        },
        {
            "home": "FC Stockholm Internazionale",
            "away": "Älvsjö AIK FF",
            "homeGoals": 4,
            "awayGoals": 0,
            "goals": [
                {"minute": 51, "team": "home"}, {"minute": 57, "team": "home"},
                {"minute": 74, "team": "home"}, {"minute": 80, "team": "home"}
            ],
            "redCards": [{"minute": 19, "team": "away"}]
        },
        {
            "home": "Bromma TFF",
            "away": "Reymersholms IK",
            "homeGoals": 5,
            "awayGoals": 0,
            "goals": [
                {"minute": 30, "team": "home"}, {"minute": 47, "team": "home"}, {"minute": 72, "team": "home"},
                {"minute": 87, "team": "home"}, {"minute": 91, "team": "home"}
            ],
            "redCards": []
        }
    ]

def create_sample_data_file(filename="data1.txt"):
    """
    Create a sample data file with the default match data.
    """
    sample_data = {
        "matches": get_default_matches()
    }
    
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(sample_data, file, indent=2, ensure_ascii=False)
    
    print(f"Sample data file '{filename}' created successfully!")

if __name__ == "__main__":
    # Create sample data file if run directly
    create_sample_data_file()
