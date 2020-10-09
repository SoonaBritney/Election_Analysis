counties_dict={}
counties_dict["Arapahoe"] = 422829
counties_dict["Jefferson"] = 432438
counties_dict["Denvere"] = 463353
print(counties_dict)
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    message_to =(
        f"{county} county has {voters:,} registered voters.")
    
    print(message_to)

candidate_votes = 3345
total_votes = 23123
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate) 
