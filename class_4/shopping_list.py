shopping_list = {}

while True:
    command = raw_input("Enter a command: ")
    if command == 'quit':
        break
    elif 'quantity' in command:
        key = command.split()[1]
        if key in shopping_list:
            print 'You need to pick up {} {}s'.format(shopping_list[key], key)
        else:
            print 'You have zero {}s on your list'.format(key)
    else:
        if command in shopping_list:
            shopping_list[command] += 1
        else:
            shopping_list[command] = 1

print shopping_list
