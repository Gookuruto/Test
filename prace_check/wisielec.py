import random

word_list = ["jazz", "xylophone", "yachtsman", "zigzag", "kayak", "zombie", "funny", "galaxy", "subway", "staff"]

word = word_list[random.randint(0,9)]
answer = ["_" for x in word ]
life = 5
print(f"Your lives: {life}")
def output():
    output_answer = ""
    for i in answer:
        output_answer = output_answer + i
    return output_answer

print(f"Unlock all letters in this word: {output()} ({len(output())})")

def letter_search():
    temp = 0
    for i in word:
        if k == i:
            answer[temp] = i
        temp += 1

while life > 0 and output() != word:
    k = str(input("Podaj literę")).lower().strip()
    if k not in output() and k in word:
        letter_search()
        print(output())
    else:
        life-=1
        print(f"No such letter. Your lives: {life}")

if output() == word:
    print("You win!")
else:
    print(f"You loose. Correct answer: {word}")
