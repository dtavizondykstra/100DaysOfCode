# Love Compatibility Tester
print("Welcome to the Love Calculator!")
name1 = input("What is your name? ").lower()
name2 = input("What is their name? ").lower()
name = name1 + " " + name2


def compatibility_counter(name):
    true_count = str(len([char for char in name if char in 'true']))
    love_count = str(len([char for char in name if char in 'love']))
    total_count = int(true_count + love_count)
    if total_count < 10 or total_count > 90:
        print(f"Your score is {total_count}, you go together like coke and mentos.")
    elif total_count >= 40 and total_count <= 50:
        print(f"Your score is {total_count}, you are alright together.")
    else:
        print(f"Your score is {total_count}.")


compatibility_counter(name)
