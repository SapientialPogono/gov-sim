# Clear Screen Command
import os

def clear_screen():
    if os.name == 'nt':
        os.system('cls')

    else:
        os.system('clear')

# Influence Variables

exporttax = 50
importtax = 50
istax = 50
col = 50
jobmarket = 50
homeless = 50
freedom = 50
freedomw = 50
govtpop = 50
rulerpop = 50
govpop = 50
militaryn = 50
mleader = 50
msoldier = 50
msoldierloyalty = 80

# Chosen Gov. Type
government = 0
# Government Type: 1 = Democracy, 2 = Monarchy, 3 = Republic, 4 = Oligarchy

print("Welcome to Government Simulator!")
print("Please choose your type of government: 1 Democracy, 2 Monarchy/Dictatorship, 3 Republic, 4 Oligarchy")
    
while True:
 government = input("Enter the number of your choice: ")

 try:
        government = int(government)
 except ValueError:
        clear_screen()
        print("That's not a number!")
        continue

 if government < 1 or government > 4:
        clear_screen()
        print("That's not a government!")
        continue
 break


if government == 1:
    print("You have chosen to be a Democracy. The people are thrilled at their newfound freedoms.")
    freedom = 90
    govtpop = 80

if government == 2:
    print("You have chosen to be a Monarchy/Dictatorship. The people stand behind you. For now...")
    freedom = 20
    freedomw = 50
    mleader = 80
    msoldier = 70
    govtpop = 60

if government == 3:
    print("You have chosen to be a Republic. The people are excited to decide who will form their government.")
    freedom = 70
    freedomw = 20
    govtpop = 90

if government == 4:
    print("You have chosen to be an Oligarchy. The people are cautious, but hope for a thriving economy.")
    freedom = 35
    freedomw = 30
    govtpop = 55
    
# Indepth Setup

print("\nNow we will set up your government in more detail.")
print("Please choose your foundation: 1 Constitution, (You may only choose a constitution at this time)")


while True:
    fgov = input("Enter the number of your choice: ")
    try:
        fgov = int(fgov)
    except ValueError:
        clear_screen()
        print("That's not a number!")
        continue
    if fgov < 1 or fgov > 1:
        clear_screen()
        print("That's not a foundation!")
        continue

    break

if fgov == 1:
   print("You have chosen to have a Constitution. Your leadership skills in leading the reveloution has made the people trust you with writing it.")

   