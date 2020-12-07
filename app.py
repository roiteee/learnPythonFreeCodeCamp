friends1 = ["Kevin", 2, True]
print(friends1)

friends = ["Kevin", "Karen", "Jim"]
print(friends[2]) #Jim

print(friends[-2]) #Karen

friends.append("Oscar")
friends.append("Toby")

print(friends)

print(friends[1:]) #2nd to last
print(friends[1:3]) #2nd to 3rd not including 4

friends[1] = "Mike"  #Mike instead of Karen
print(friends)


