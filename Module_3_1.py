calls = 0
def count_calls():
    global calls
    calls+=1
def string_info(text):
    count_calls()
    return (len(text),text.upper(), text.lower())
def is_contains(text, mylist):
    count_calls()
    for i in range(len(mylist)):
        if (text.lower() == mylist[i].lower()):
            contains = True
            break
        else:
            contains = False
    return contains
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)