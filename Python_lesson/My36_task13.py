# create text mebu

def search():
    print("Searching")


def add():
    print("adding")


def delete():
    print("deleting")


def menu(menu_actions: list):
    action = None
    while action != "exit":
        print("Please select position from below:")
        for i, a in enumerate(menu_actions):
            action_text, _ = a
            print(f"{i}: {action_text}")
        action = input("Choice: ").lower()

        for a in menu_actions:
            action_text, action_func = a
            if action_text.lower() == action:
                if action_func is None:
                    break
                action_func()


def main():
    menu_actions = [
        ("Search", search),
        ("Add", add),
        ("Delete", delete),
        ("Exit", None),
        ]
    
    menu(menu_actions=menu_actions)

main()
