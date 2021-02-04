import random

random_number = random.randint(0, 9)
magic_numbers = [random_number,random_number]

def ask_user_and_check_number():
    user_input = int(input("Enter a number between 0 to 9: "))
    if user_input in magic_numbers:
        return "You Won!"
    else:
        return "You Lose!"

def run_programs_in_x_times(user_attempt):
    for attempt in range(user_attempt): #range(chances) is a list that contained [0,1,2]
        print(f"This is attempt {attempt}.")
        answer = ask_user_and_check_number()
        print(answer)


user_attempt = int(input("How Many Numbers Of Attempt You Want? "))
run_programs_in_x_times(user_attempt)

