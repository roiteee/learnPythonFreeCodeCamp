friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby", "Jim"]
lucky_numbers = [4,8,5,16,23,4]
print(friends)

friends.extend(lucky_numbers)
print(friends)

friends.append("Creed")
print(friends)

friends.insert(1, "Kelly") #inserts at 2nd position and all other gets pushed
print(friends)

friends.remove("Kevin")
print(friends)

#friends.clear() #[] removes all
friends.pop() #removes last element
print(friends)

print(friends.index(4)) 
#print(friends.index('oscar')) #error
print(friends.index('Toby'))
print(friends.count('Jim'))

lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)

friends2 = friends.copy()
print(friends2)
