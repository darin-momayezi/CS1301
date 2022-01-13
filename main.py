# HW01


def dinnerTime():
    num_entrees = int(input("How many entrees will you be ordering today? "))
    num_drinks = int(input("How many drinks will you be ordering today? "))
    price_entree = 12
    price_drink = 4.50
    total_cost = (num_entrees * price_entree) + (num_drinks * price_drink)
    print("The total cost of all the meals and drinks is ${}".format(total_cost))


def bottleBonanza():
    radius = float(input("What is the radius of the water bottle? "))
    height = float(input("What is the height of the water bottle? "))
    pi = 3.14
    volume = pi * (radius**2) * height
    print("The volume of the water bottle is {}".format(volume))


def winterBreak():
    num_episodes = int(input("How many episodes did you watch? "))
    num_videos = int(input("How many videos did you watch? "))
    len_episode = 40
    len_video = 10
    total_hours = (num_episodes * len_episode + num_videos * len_video) // 60
    total_mins = (num_episodes * len_episode + num_videos * len_video) - (total_hours * 60)
    print("You spent {} hours and {} mins watching Netflix and Youtube over winter break.".format(total_hours, total_mins))


def skateboardMoney():
    monthly_allowance = float(input("How much is your monthly allowance? "))
    percent_saved = float(input("What percentage of your allowance do you want to save? ")) / 100
    monthly_expense = 30 * (4.4 + 5.99)
    money_saved = monthly_allowance * percent_saved
    left_over = money_saved + (monthly_allowance - money_saved - monthly_expense)
    print("You'll have ${} left to spend on your skateboard after savings and fees.".format(round(left_over, 2)))

