# سوال یک روش دوم

word_dict = {
    "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7",
    "eight": "8", "nine": "9", "ten": "10", "eleven": "11", "twelve": "12", "thirteen": "13",
    "fourteen": "14", "fifteen": "15", "sixteen": "16", "seventeen": "17",
    "eighteen": "18", "nineteen": "19"
}

with open("Zen.txt" , "r" ) as f:
    text = f.read()

# Splitting text lines
lines = text.split('\n')

# Creating a new text by replacing words with their numerical equivalents
new_text = ''
for line in lines:
    words = line.split(' ')
    if len(words) > 1 and words[0] in word_dict:
        words[0] = word_dict[words[0]]
        new_text += ' '.join(words) + '\n'
    else:
        new_text += line + '\n'

# Writing the new text into the output file
with open("newZen_2.txt", 'w') as f:
    f.write(new_text)