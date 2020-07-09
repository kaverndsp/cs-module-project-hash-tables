def word_count(s):

    # create a hash that contains a key and value
    # iterate through each letter in the string
    # create an exception for empty space and puncuation to pass over those
    # the key will be each letter that occurs in the string and the value will be how many times it occurs
    # when a letter occurs, it will add + 1 to that key.
    # we can then maybe call some function on the values in the hash to sort from largets to smallest

    store = {}

    for letter in s.lower():
        if letter.isspace():
            continue
        if letter in store:
            store[letter] += 1
        else:
            store[letter] = 1
    return store

    # reminder to self, actually read the problem fully before writing code..........


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
