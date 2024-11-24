#1
def check_letter():
    vowel = ['a','e','i','o','u']
    letter = input('enter a letter')
    if letter in vowel:
        print(f'the letter {letter} is a vowel')
    else:
        print(f'the letter {letter} is a constanant')
check_letter()


# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
    # Your control flow logic goes here
    voting_age = 18

    age = int(input('How old are you?'))
    if age < 0:
        print('please enter a correct age')
    elif age < 18:
        print('You are to young to vote')
    else:
        print('Congrats, you can vote')

# Call the function
check_voting_eligibility()


# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    # Your control flow logic goes here
    age = int(input('Enter your dogs age in human years here'))

    if age <= 0:
        print('please enter a correct age')
    elif age <= 2:
        if age == 1:
            age += 10
            print(f'your dogs age is {age}')
        else:
            age += 20
            print(f'your dogs age is {age}')
    else:
        age = age * 7 + 20
        print(f'your dogs age is {age}')
# Call the function
calculate_dog_years()


# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    # Your control flow logic goes here
    cold = input('is it cold (yes/no)')
    rain = input('is it raining? (yes/no)')

    if cold == 'yes' and rain == 'yes':
        print('Wear a waterproof coat.')
    elif cold == 'yes' and rain == 'no':
        print("Wear a warm coat.")
    elif cold == 'no' and rain == 'yes':
        print("Carry an umbrella.")
    elif cold == 'no' and rain == 'no':
        print('wear light clothing')
    else:
        print(' please input yes or no')
# Call the function
weather_advice()


# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
    month = input('Please tell me what month it is in MMM format').upper()

    day = int(input('please tell me what day of the month it is in DD format'))

    valid_months = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']

    if month not in valid_months:
        print('Please enter a valid month in MMM format')
        return 
    
    if day < 1 or day > 31:
        print('Pease enter a valid day of the month')
        return
    if (month == 'DEC' and day >= 21) or month in ['JAN','FEB'] or (month == 'MAR' and day <= 19):
        season = 'WINTER'
    elif (month == 'MAR' and day >= 20) or month in ['APR', 'MAY'] or (month == 'JUN' and day <= 20):
        season = 'SPRING'
    elif (month == 'JUN' and day >= 21) or month in  ['JUL', 'AUG'] or (month == 'SEP' and day <=21):
        season = 'SUMMER'
    elif (month == 'SEP' and day >= 22) or month in ['OCT', 'NOV'] or (month == 'DEC' and day <= 20):
        season = 'FALL'
    else:
        print('Please enter a valid date')
    
    print(f'{month} {day} is in {season}')




determine_season()
# Exercise 7: Number Guessing Game
#
# Write a Python function named `guess_number` that allows a user to guess a predetermined number within a range.
#
# Requirements:
# - Set a fixed number as the target for guessing (e.g., 42).
# - Prompt the user to guess a number within a range (e.g., 1 to 100).
# - Allow the user to guess up to five times.
# - After each guess, use conditional statements with AND, OR, and NOT to give the user hints like:
#   - "Guess is too low" or "Guess is too high."
#   - "Last chance!" when they are on their fifth guess.
# - Print "Congratulations, you guessed correctly!" if they guess the number.
# - Print "Sorry, you failed to guess the number in five attempts." if they do not succeed.
#
# Hints:
# - Use a for loop with a range to limit guesses to five.
# - Use logical AND, OR, and NOT to check conditions and provide appropriate feedback.

# def guess_number():
import random

def guess_number():
    target = random.randint(1,100)
    max_attempts = 5

    for attempt in range(1,max_attempts + 1):
        try:
            guess = int(input(f'Attempt {attempt}/{max_attempts}: Enter your guess'))
        except ValueError:
            print('Enter a valid number')
        if guess < 1 or guess > 100:
            print('Please enter a number from 1 - 100')
            continue
        if guess == target:
            print('YOU GOT IT RIGHT')
            return
        elif guess < target:
            print('Your guess is to low')
        else:
            print('Your guess is too high')

        if attempt == max_attempts - 1:
            print('Last chance')
    print(f'Sorry, you failed to guess the number. The number was {target}')

# Call the function
guess_number()