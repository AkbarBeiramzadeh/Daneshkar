# سوال یک روش اول

with open("Zen.txt" , "r" ) as f:
    text = f.read()

word_dict = {
        "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7",
        "eight": "8","nine": "9", "ten": "10", "eleven": "11", "twelve": "12", "thirteen": "13",
        "fourteen": "14", "fifteen": "15","sixteen": "16", "seventeen": "17",
        "eighteen": "18", "nineteen": "19",
    }

for word in word_dict.keys():
    text = text.replace(word, word_dict[word], 1)
print(text)

with open("newZen.txt" , "w" , encoding="UTF-8") as f:
    f.write(text)



