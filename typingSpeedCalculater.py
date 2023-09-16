from time import time
import random as r

def calculate_mistakes(para, userPara):
    total_mistake_words = 0
    for i in range(len(para)):
        try:
            if para[i] != userPara[i]:
                total_mistake_words += 1
        except:
            total_mistake_words += 1
    return total_mistake_words

def calculate_speed(time_s, time_e, user_input):
    time_delay = time_e - time_s
    time_r = round(time_delay, 2)
    speed = len(user_input) / time_r
    return round(speed, 2)

while True:
    choice = input("Do you want to play a game (y/n): ")
    
    if choice.lower() == "y":
        tests = [
            "The quick brown fox jumps over the lazy dog.",
            "Collect information about your geographical location which can be accurate to within several meters.",
            "Necessary cookies help make a website usable by enabling basic functions like page navigation and access to secure areas of the website. The website cannot function properly without these cookies.",
            "Statistic cookies help website owners to understand how visitors interact with websites by collecting and reporting information anonymously.",
            "Marketing cookies are used to track visitors across websites. The intention is to display ads that are relevant and engaging for the individual user and thereby more valuable for publishers and third party advertisers.",
            "We and our advertising partners process your personal data using technology such as cookies in order to serve advertising, analyse our traffic and deliver customised experiences for you. You have a choice in who uses your data and for what purposes."
        ]

        test1 = r.choice(tests)
        
        print("~" * 50)
        print("~" * 18 + " Typing Test " + "~" * 18)
        print("~" * 50)
        print()
        print(test1)
        print()
        print()
        
        time_start = time()
        user_input = input("Enter the above sentence: ")
        time_end = time()

        speed = calculate_speed(time_start, time_end, user_input)
        mistakes = calculate_mistakes(test1, user_input)

        print("Speed:", speed, "w/sec")
        print("All Mistakes:", mistakes)
        
    elif choice.lower() == "n":
        print()
        print("~" * 2 + "  Thank you for playing. You played very well.  ~~")
        break
    else:
        print("You entered a wrong choice. Please enter only 'y' or 'n'.")
