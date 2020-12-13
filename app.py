#Translator that translates all vowels to 'g'
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            #translation += 'g'
            if letter.isupper():
                translation += 'G'
            else:
                translation += 'g'
        else:
            translation += letter
    return translation

print(translate(input("Enter Phrase: ")))
