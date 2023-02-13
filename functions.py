FILEPATH = "todos.txt"

def get_todos():
    with open(FILEPATH, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(list_of_todos, filepath = FILEPATH):
    with open(filepath, 'w') as file:
            file.writelines(list_of_todos)
