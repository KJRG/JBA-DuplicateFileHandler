gryffindor = set(input().split())
ravenclaw = set(input().split())
slytherin = set(input().split())
hufflepuff = set(input().split())
all_wizards = gryffindor.union(ravenclaw).union(slytherin).union(hufflepuff)
print(all_wizards)
