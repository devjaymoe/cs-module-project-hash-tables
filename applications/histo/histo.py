# Your code here

# Read in all the words in one go
with open("robin.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here

bad_chars = ["\"", ":", ";", ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']

words = words.lower()

for x in bad_chars:

    words = words.replace(x, '')

words_arr = words.split()
cache = {}

for x in words_arr:

    if x in cache:
        cache[x] += 1
    else:
        cache[x] = 1

if __name__ == "__main__":
    while True:
        text = input("Enter text: ")

        if text in cache:

            number_of_times_appeared = cache[text]

            print(text, end="      ")
            print("#" * number_of_times_appeared)

        else:
            
            print('word not found...')