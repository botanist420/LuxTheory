from nba_api.stats.static import players




# get_players returns a list of dictionaries, each representing a player.
nba_players = players.get_players()
# print('Number of players fetched: {}'.format(len(nba_players)))


input_player_name = input("Please type the player's full name:\n")

# print(nba_players[:5])

for i in nba_players:
    if i.get("full_name") == input_player_name:
        player_id = i.get("id")
        print(f"The player {input_player_name} id is:\n{player_id}")