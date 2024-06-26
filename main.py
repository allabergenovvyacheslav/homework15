calls = 0
def count_calls():
    global calls
    calls += 1
count_calls()
def string_info(string):
    a = (len(string), string.upper(), string.lower())
    count_calls()
    return a
def is_contains(string, list_to_search):
    list_to_search = [x.upper() for x in list_to_search]
    if string.upper() in list_to_search:
        print(True)
    else:
        print(False)
        count_calls()

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycle', 'cyclic']))
print(calls)
