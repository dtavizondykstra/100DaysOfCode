#Tip Calculator
import time
print("Welcome to the tip calculator.")
time.sleep(1)
total_bill = float(input("What was the total bill? $"))
choose_percentage = int(input("What percentage tip would you like to give? 10, 15, or 20? "))
percentage = choose_percentage / 100
people = int(input("How many people are splitting the bill? "))
time.sleep(2)
split_total = (total_bill / people)
tip = split_total * percentage
total_w_tip = split_total + tip
print(f"Each person should pay: ${total_w_tip}")
time.sleep(1)
print(f"Specifically, that's ${split_total} for the bill and ${tip} for the tip\n")
