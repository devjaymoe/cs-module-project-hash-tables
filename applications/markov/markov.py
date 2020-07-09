import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here

words_arr = words.split()
cache = {}

ending_punc = [".",  "?", "!"]
starting_words = set()
stop_words = set()

for i in range(len(words_arr)):

    cur_word = words_arr[i]

    if i + 1 > len(words_arr) - 1:
        next_word = None
    else:
        next_word = words_arr[i + 1]

    if cur_word not in cache:
        cache[cur_word] = []
    
    if next_word is not None:
        cache[cur_word].append(next_word)

    if cur_word[0:1].isupper() or cur_word[1:2].isupper():
        starting_words.add(cur_word)
    
    if cur_word[len(cur_word) - 2: len(cur_word) - 1] in ending_punc:
        stop_words.add(cur_word)

# TODO: construct 5 random sentences
# Your code here

random_starting_word = random.choice(list(starting_words))

sentence = [random_starting_word]
cur_word = cache[random_starting_word]

stop_seq = False
while not stop_seq:

    cur_word = random.choice(cur_word)

    if cur_word in stop_words:
        stop_seq = True

    sentence.append(cur_word)

    cur_word = cache[cur_word]

x = " ".join(sentence)

print(x)