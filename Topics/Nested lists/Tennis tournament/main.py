n = int(input())
players = [input().split() for _ in range(n)]
players_who_won = [player_data[0] for player_data in players if player_data[1] == "win"]
print(players_who_won)
print(len(players_who_won))
