is_male = False
is_tall = False

if is_male:
    print("You are a male")
else:
    print("You are not a male")

print("\n")
if is_male or is_tall: #TF FT TT
    print("You are a male or tall or both")
else: #FF
    print("You are neither male nor tall")

print("\n")
if is_male and is_tall: #TT
    print("You are a tall male")
elif is_male and not(is_tall): #TF
    print("You're a short male")
elif not(is_male) and is_tall: #FT
    print("You're not a male but are tall")
else: #FF
    print("You're not a male and not are tall")


