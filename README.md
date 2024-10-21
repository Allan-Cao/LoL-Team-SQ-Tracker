
# LoL Team SQ Tracker

**Please note that this code doesn't work in its current state and will not be maintained, but I hope it can be useful to anyone working on a similar project.**

This repository houses the code that ran the AOE solo queue tracker. It was run hourly to update the spreadsheet with match histories for all players.

## Run Locally

Clone the project

```bash
  git clone git@github.com:Allan-Cao/AOE-Team-Tracker.git
```

Go to the project directory.

```bash
  cd AOE-Team-Tracker
```

Create a virtual environment and activate it.

```bash
  virtualenv dev
  dev/Scripts/activate
```

Run the hourly code (do NOT run when the time is around :00 as that is when the server will be running the program, and this may cause conflicting match histories)

```bash
  python TeamTracker.py
```


## Environment Variables

To run this project, you must add the following environment variables to your .env file.

`RIOT_API`

`TEAM_SHEET_ID`

`SHEET_CLIENT_SECRET`
