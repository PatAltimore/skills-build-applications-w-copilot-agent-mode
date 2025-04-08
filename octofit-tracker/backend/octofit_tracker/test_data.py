from datetime import timedelta

test_data = {
    "users": [
        {"username": "thundergod", "email": "thundergod@mhigh.edu", "password": "thundergodpassword"},
        {"username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "metalgeekpassword"},
        {"username": "zerocool", "email": "zerocool@mhigh.edu", "password": "zerocoolpassword"},
        {"username": "crashoverride", "email": "crashoverride@mhigh.edu", "password": "crashoverridepassword"},
        {"username": "sleeptoken", "email": "sleeptoken@mhigh.edu", "password": "sleeptokenpassword"},
    ],
    "teams": [
        {"name": "Blue Team"},
        {"name": "Gold Team"},
    ],
    "activities": [
        {"username": "thundergod", "activity_type": "Cycling", "duration": timedelta(hours=1)},
        {"username": "metalgeek", "activity_type": "Crossfit", "duration": timedelta(hours=2)},
        {"username": "zerocool", "activity_type": "Running", "duration": timedelta(hours=1, minutes=30)},
        {"username": "crashoverride", "activity_type": "Strength", "duration": timedelta(minutes=30)},
        {"username": "sleeptoken", "activity_type": "Swimming", "duration": timedelta(hours=1, minutes=15)},
    ],
    "leaderboard": [
        {"team_name": "Blue Team", "points": 150},
        {"team_name": "Gold Team", "points": 120},
    ],
    "workouts": [
        {"name": "Cycling Training", "description": "Training for a road cycling event", "duration": timedelta(hours=1)},
        {"name": "Crossfit", "description": "Training for a crossfit competition", "duration": timedelta(hours=2)},
        {"name": "Running Training", "description": "Training for a marathon", "duration": timedelta(hours=1, minutes=30)},
        {"name": "Strength Training", "description": "Training for strength", "duration": timedelta(minutes=30)},
        {"name": "Swimming Training", "description": "Training for a swimming competition", "duration": timedelta(hours=1, minutes=15)},
    ],
}
