
# Team Tracker

This repository houses the code that runs the AOE solo queue tracker. This code should be run ~hourly to update the spreadsheet with match history for all players.


## Run Locally

Clone the project

```bash
  git clone git@github.com:Allan-Cao/AOE-Team-Tracker.git
```

Go to the project directory

```bash
  cd AOE-Team-Tracker
```

Create a virtual enviroment and activate it

```bash
  virtualenv dev
  dev/Scripts/activate
```

Run the hourly code (do NOT run when the time is around :00 as that is when the server will be running the program and this may cause conflicting match histories)

```bash
  python TeamTracker.py
```


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`RIOT_API`

`TEAM_SHEET_ID`

`SHEET_CLIENT_SECRET`
