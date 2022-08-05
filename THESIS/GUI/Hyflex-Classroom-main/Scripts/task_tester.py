# Task Tester
import caller_main

while True:
    task = input('Task: ')

    if task == 'call':
        contact_name = input('Contact Name: ')
        caller_main.call(contact_name)

    else:
        print('Invalid task')
