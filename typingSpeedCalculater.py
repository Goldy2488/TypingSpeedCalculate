from time import *
import random as r


def mistake(para,userPara):
    TotalmistakeWords=0
    for i in range(len(para)):
        try:
            if para[i]!=userPara[i]:
                TotalmistakeWords+=1
        except:
            TotalmistakeWords+=1
    return TotalmistakeWords


def speed_time(time_s,time_e,userinput):
    time_dalay = time_e - time_s
    time_R = round(time_dalay,2)
    speed=len(userinput)/time_R
    return round(speed,2)
    

test=["The quick brown fox jumps over the lazy dog.",
     "Collect information about your geographical location which can be accurate to within several meters.",
      "Necessary cookies help make a website usable by enabling basic functions like page navigation and access to secure areas of the website. The website cannot function properly without these cookies.",
        "Statistic cookies help website owners to understand how visitors interact with websites by collecting and reporting information anonymously.",
       "Marketing cookies are used to track visitors across websites. The intention is to display ads that are relevant and engaging for the individual user and thereby more valuable for publishers and third party advertisers.",
        "We and our advertising partners process your personal data using technology such as cookies in order to serve advertising, analyse our traffic and deliver customised experiences for you. You have a choice in who uses your data and for what purposes." ]

test1 =r.choice(test)
print("~"*10+" Typing Test "+"~"*10)
print(test1)
print()
print()
time_s=time()
testinput=input("Enter above sentance : ")
time_e=time()

print("Speed : ",speed_time(time_s,time_e,testinput)," w/sec")
print("ALL Mistaks : ",mistake(test1,testinput))