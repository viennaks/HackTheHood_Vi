from tabnanny import check

checklist = []

# Define Functions
def create(item):
    checklist.append(item)

def read(index):
    print(checklist[index])

def update(index, item):
    checklist[index]= item

def destroy(index):
    checklist.pop(index)

def mark_completed(index):
    checklist[index] += "*"

def list_all_items():
    print(checklist)

def user_input(prompt):
    x = input(prompt)
    return x
    
def select(function_code):  

    function_code = user_input("What functions do you want to run? Create (c), Read (r), Update (u), Destroy (d), Mark Complete (m), and List all Items (l)\n Input a letter: ")

    if function_code == "c":
        item = user_input("Input item: ")
        create(item)
        running= True
        return running

    elif function_code == "r":
        index = user_input("Input index: ")
        read(index)
        running = True
        return running

    elif function_code == "u":
        index = user_input("Input index: ")
        item = user_input("Input item: ")
        update(index, item)
        running = True
        return running

    elif function_code == "d":
        index = user_input("Input index: ")
        destroy(index)
        running = True
        return running

    elif function_code == "m":
        index = user_input("Input index: ")
        mark_completed(index)

    elif function_code == "l":
        list_all_items()

running = True

while running:
    selection = user_input( "Press any key to start")
    running = select(selection)
 
 