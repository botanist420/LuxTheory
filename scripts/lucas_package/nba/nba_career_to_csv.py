from nba_api.stats.endpoints import playercareerstats
import pandas as pd


id_num = input("Please type the player id:\n")

career = playercareerstats.PlayerCareerStats(player_id=id_num) 

# pandas data frames (optional: pip install pandas)
result_df = career.get_data_frames()[0]
print("Export data frame to data srouce...")

file_path = "../../../data/nba_player_career.csv"

print(f"The file path would be {file_path}")

result_df.to_csv(file_path, sep=",", index=False)

print("All done!!!")