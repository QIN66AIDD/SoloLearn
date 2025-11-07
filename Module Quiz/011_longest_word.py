def find_longest_word(word_list):
    longest_word = ''
    for word in word_list:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

li = ['this', 'is', 'a', 'longest', 'text']

print('Default list:', li)
print('Longest word of the list is:', find_longest_word(li))


'''output:

Default list: ['this', 'is', 'a', 'longest', 'text']
Longest word of the list is: longest
'''