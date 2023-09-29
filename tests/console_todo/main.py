import json
import os


work_dir = os.path.dirname(__file__)
os.chdir(work_dir)


def mark_done(todo_list:list, id:int):
    for item in todo_list:
        if item['id'] == id:
            item['done'] = True


while True:
    file = open('todo.json')

    todo_list = json.load(file)

    last_id = 0

    for todo in todo_list:
        if not todo['done']:
            print(f"{todo['id']}. {todo['todo']}")
        last_id = todo['id']

    print()
    print('1. Add new')
    print('2. Mark as done')

    choise = input('> ')

    while choise not in ['1','2']:
        print('Incorect input, try again:')
        choise = input('> ')

    if choise == '1':
        new_todo_text = input('New todo > ')
        new_todo = {}
        new_todo['id'] = last_id+1
        new_todo['todo'] = new_todo_text
        new_todo['done'] = False
        todo_list.append(new_todo)
        file = open('todo.json', 'w')
        json.dump(todo_list, file)
        file.close()


    if choise == '2':
        todo_done_id = input('Mark done todo # > ')
        mark_done(todo_list, int(todo_done_id))
        file = open('todo.json', 'w')
        json.dump(todo_list, file)
        file.close()

    print()
    print()
    print()


