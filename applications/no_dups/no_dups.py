def no_dups(s):
    # Your code here
    cache = {}
    str_arr = s.split()

    for x in str_arr:

        if x not in cache:
            cache[x] = x

    a = ""

    for x in cache:
        a += cache[x] + " "
    
    return a.rstrip()

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))