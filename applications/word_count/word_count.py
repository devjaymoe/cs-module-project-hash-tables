def word_count(s):
    # Your code here
    cache = {}
    bad_chars = ["\"", ":", ";", ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']

    nice_string = s.lower()

    for i in bad_chars:

        nice_string = nice_string.replace(i, '')

    string_arr = nice_string.split()

    for x in string_arr:

        if x not in cache:
            cache[x] = 1
        else:
            cache[x] += 1

    return cache

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))