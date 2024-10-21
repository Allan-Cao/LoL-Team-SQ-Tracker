from cassiopeia import get_match_history
from cassiopeia import Summoner, Queue
from datetime import timedelta

from lol_team_tracker.match_lib.match_helper import get_player_stats, region_string

# Constants
MINIMUM_MATCH_DURATION = timedelta(minutes=10)

def upsert_player_match(MATCH_WKS, player_name, player_accounts, IMPORTED_MATCH_IDS, DEFAULT_REGION, START_TIME):
    try:
        player_imported_matches = IMPORTED_MATCH_IDS[player_name]
    except KeyError:
        player_imported_matches = set()
    for account in player_accounts:
        table = []
        account_region = DEFAULT_REGION if account['region'] == '' else account['region']
        summoner = Summoner(puuid=account['puuid'], region=account_region)
        # try:
        #     # Lazy load the summoner object to verify it exists
        #     _ = summoner.level
        #     print(f"Importing match history for {player_name} on {summoner.name}")
        # except:
        #     print(f"Failed to import match history for {player_name} on ID - {account['account_name']}#{account['tagline']}- Invalid PUUID received - {account['puuid']} - {account_region}")
        #     continue
        match_history = get_match_history(continent=summoner.region.continent, start_time=START_TIME, puuid=summoner.puuid, queue=Queue.ranked_solo_fives)
        for match in match_history:
            if region_string(match) not in player_imported_matches and match.duration > MINIMUM_MATCH_DURATION:
                try:
                    for participant in match.participants:
                        if participant.summoner.puuid == summoner.puuid:
                            table.append([player_name] + get_player_stats(participant, account, match))
                except ValueError:
                    print(f"Failed to import match {match.id} for {player_name} on {account['account_name']}#{account['tagline']}")
        if len(table) > 0:
            MATCH_WKS.append_table(table)