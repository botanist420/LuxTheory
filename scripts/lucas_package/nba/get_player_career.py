from nba_api.stats.endpoints import playercareerstats


id_num = input("Please type the player id:\n")

career = playercareerstats.PlayerCareerStats(player_id=id_num) 

# pandas data frames (optional: pip install pandas)
result_df = career.get_data_frames()[0]

print(result_df.head())

# json
# career.get_json()

# dictionary
# career.get_dict()