import random as rand
greetings = [
    "Hi {},how are you?",
    "Hello {},you good?",
    "goodday{},hope you are good?"
    ]
greetings_size = range(1, len(greetings)+1)
greetings_dict = dict(zip(greetings_size,greetings))
def choose_random_number() -> str:
    random_num = rand.choice(greetings_size)
    return greetings_dict[random_num]
def selected_digit() -> str:
    try:
        pick = int(input(f"Enter a digit between 1 and {max(greetings_size)}:"))
        greeting = greetings_dict[pick]
    except ValueError as Error:
        print("pls enter a digit")
    except IndexError as Error:
        print("digit not found!!!")
    else:
        return greeting
def run_all() -> None:
    name = input("Enter a name:")
    if not name:
        return
    try:
       your_choice = int(input("choose 1 for random or 2 for selected greeting:"))
    except ValueError:
        print("Try Again!!!")
        return
    if your_choice == 1:
        random_message = choose_random_number()
        print(random_message.format(name))
    elif your_choice == 2:
        selected_message = selected_digit()
        print(selected_message.format(name))
    else:
        print("you have to choose between 1 or 2")
run_all()

    

