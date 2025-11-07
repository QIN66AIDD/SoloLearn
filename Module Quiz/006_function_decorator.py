text = input('Enter your text: ')

# decorator function
def uppercase_decorator(func):
    def wrapper(text):
        return text.upper()
    return wrapper

    
@uppercase_decorator    
def display_text(text):
    return(text)
    
print(display_text(text))


'''output:

Enter your text: this is my text
THIS IS MY TEXT
'''