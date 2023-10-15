retry = 'Y'
choice = 'N'
retry1 = 'Y'
retry2 = 'Y'
where_am_i = 'N'
what_did_i_do = 'N'
def reset_choice():
    global choice
    global choice_A
    global choice_B
    global choice_C
    global choice_D
    choice = 'N'
    choice_A = 0
    choice_B = 0
    choice_C = 0
    choice_D = 0

class player():
    def __init__(self):
        self.gender = 'undecided'
        self.name = 'unknown'
        self.race = 'unknown'
        self.health = 5
        self.instanity = 3
        self.intelligence = 0
        self.speed = 0
        self.strength = 0
        self.endurance = 0
        self.luck = 0
        self.achievements = []
    def __str__(self):
        return self.name

player1 = player()

def run():
    global retry, retry1, retry2, choice, choice_A, choice_B, choice_C, choice_D, player1, where_am_i, what_did_i_do
    while retry1 == 'Y' or retry1 == 'y':
        print('You wake up in a dim and dry room, the only light comes from a 6in tall\nby 4in wide window in a steel door. This small window is barred with 3\n1 inch bars with 1 inch between each, you can see the door is 6in thick.\nYou are laying on a uncomfortable cot with a small pillow and a very thin\nblanket. You have no memory before waking up you do not know your\nstrengths or weaknesses, your name, your age, or why you are here.\n')
        player1.gender = (input('What gender would you like to be? This will not have an effect on gameplay.\n')).capitalize()
        reset_choice()
        while choice_A < 1 or choice_B < 1 or choice_C < 1:
            choice = (input('\nYou now have choices about what to do. \nA. Look around the rest of the room. \nB. Try to open the door. \nC. Call out.\n')).lower()
            if choice == 'a':
                print('\nYou look around the rest of the room you find that there is a sink\nand toilet in one corner of the room and a screen in the opposite.\nThe walls are solid concrete with no cracks. The hinges of the door\nare on the outside.')
                choice_A += 1
            elif choice == 'b':
                print('\nThe door is locked and wont budge.')
                choice_B += 1
            elif choice == 'c':
                print('\nThere is no response, it is unnaturally silent.')
                choice_C += 1
        print('There is no way to get out without some kind of help.')
        reset_choice()
        while choice_C < 1:
            print('\nWhat would you like to do? \nA. Splash your face with water from the sink. Maybe its just a dream.')
            choice = input('B. Try to sleep in the bed.\nC. Go to the screen and try to get it working.\n').lower()
            if choice == 'a':
                print('\nThe water is cold no matter how you move the handle. You splash your face\nwith the water. Its refreshing and cool running down your face, but this\nis real not a dream.')
                choice_A += 1
            elif choice == 'b':
                print('\nYou lay down close your eyes and try to relax. After several minutes you\ngive up, you cant relax not until you know who you are, why youre here,\nand where here is.')
                choice_B += 1
            elif choice == 'c':
                print('\nYou go to the screen there are no buttons and you dont see a way to turn\nit on.')
                Tap = input('Would you like to try tapping it? Respond with y for yes or n for no.\n').lower()
                if Tap == 'y':
                    choice_C += 1
                    
                else:
                    print('\nYou turn away but have a feeling you will have to come back to this.')
        print('\nYou tap the screen and it turns on instantly. its extremely bright causing\nyou to cover your eyes with your arm. You slowly lower it to look at the\nscreen blinking a lot as your eyes begin to adjust. The screen displays\na string of text in green, typing out words with a flashing green space\nin front. "Welcome to your new home Prisoner 6029."')
        print('\nYou look at the screen with confusion, you are some sort of prisoner? Were\nyou a criminal? Did you kill someone? Were you framed? Were you a hitman\nfor a criminal organization who earned international infamy for being\nan effiecnt and cold killer armed with a katana? Or maybe a sniper rifle,\nnever being seen or heard even by the people who hired you, taking your\nhits from unmarked deaddrops? Maybe you were inprisoned by the mob, the\nvictim of a corrupt system as someone bribed the cops to take you\nin place of a hitman. Your thoughts run wild with possiblities as the\nscreen sits in front of you, flashing its green space, as if awaiting a\nresponse.')
        reset_choice()
        while (choice_B < 1) and (choice_C < 1) and (choice_D < 1):
            print('\nYou decide to respond to the flashing green light, the closest thing you\nhave to another person. how do you respond?')
            choice = input("\nA. Tap the screen, it worked before seems like the most logically option.\nB. Talk to the screen, after all there isnt a keyboard so you cant type\nin a response to the green light.\nC. Scream at it full karen mode and demand to see the manager!\nD. Punch the screen you are nobody's prisoner!\n").lower()
            if choice == 'a':
                print('\nThe green text clears and is slowly replaced with a new sentence.\n"Awaiting response...')
                choice_A += 1
            elif choice == 'b':
                print('\n"Hello?" you say. The green text clears and is replaced slowly with a new\nsentence. "hello prisoner 6029. You may ask me where you are, what your\ncrimes are, or how to get out of here."')
                choice_B += 1
            elif choice =='c':
                print('\nYou are a bad person. The green text clears and is slowly replaced with a\nnew sentence. "I have no manager prisoner 6029, and you are not in charge.\nTerminal powering down..." with that the screen fades to black and doesnt\nrespond you have no hope of ever getting out now.')
                choice_C += 1
            elif choice == 'd':
                print('\nYou slam your fist into the screen, you are no prisoner, the screen is made of glass so your fist smashes through it. Shards of broken glass spray up\nyour arm and into your face, covering you in small cuts. The screen ceases to function, try as you might there is no hope of ever getting out now.')
                choice_D += 1
        if choice_B > 0:
            retry1 = 'N'
        if choice_C > 0:
            print('\nYou lost, Dont be a karen.')
            retry1 = (input('Would you like to try again? Y for yes N for no.\n')).lower()
            if retry1 == 'n':
                quit()
        if choice_D > 0:
            print('\nYou lost, violence isnt always the answer.')
            retry1 = (input('Would you like to try again? Y for yes N for no.\n')).lower()
            if retry1 == 'n':
                quit()
    while retry2 == 'Y' or retry2 == 'y':
        reset_choice()
        while choice_C < 1:
            choice = input('\nWhat do you want to say?\nA. Where am I?\nB. What was my crime?\nC. How do I get out of here?\n').lower()
            if choice == 'a':
                print('\nThe green text begins to type "You are in the interplanetary prison for\nhuman assosciated species." Your mind races with the realization that\nthere is now an interplanetary government of some kind, which also\nprobably means aliens, now the only question is is this a star wars or a\nstar trek kind of space?')
                choice_A += 1
                where_am_i = 'Y'
            elif choice == 'b':
                print('\nYou have to know why youre here, the green text begins to type "you were\nconvicted of 1 count of interplanetary level auto theft, 326 counts of\nmurder, and 1 count of using a massively destructive weapon, qualifying\nyou as a very dangerous prisoner." HOLY CRAP, 326 PEOPLE! AND\nINTERPLANETARY AUTO THEFT? THAT HAS TO MEAN A SPACESHIP RIGHT??')
                choice_B += 1
                what_did_i_do = 'Y'
            elif choice == 'c':
                print('\nThe green text begins to type "I will open your cell door once you are\nstable and choose your new lifeform. You will be able to explore the rest\nof the prison, but you will never again see the outside worlds."')
                print('You know how to get out, now you can ask it another question or try to become stable, whatever that means.')
                stable = input('\nwould you like to become stable?\n').lower()
                if stable == 'y':
                    choice_C += 1
                    if what_did_i_do == 'Y' and where_am_i == 'Y':
                        player1.intelligence = player1.intelligence + 1
                        player1.achievements.append('Informed')
                        print('\nAchievement unlocked! Informed\n')
                else:
                    print('\nIts a good idea to get some more information first.')
        print('Its time to get out of this cell, but first you have to become stable.')
        reset_choice()
        choice = input('How would you like to continue.\nA. Ask the screen how to become stable.\nB. Try to sleep again, your questions have been answered and you feel more relaxed.\nC. Start doing some workouts, crunches, leg lifts, lunges, fit body stable mind.\nD. Run around the cell, getting in a good run will clear your head and make you sweat.\n')
        if choice == 'A' or choice == 'a':
            player1.intelligence += 1
            print('\nThe screen responds "Taking vitals... You are stable prisoner, It is time to select your new lifeform.')
        if choice == 'B' or choice == 'b':
            player1.endurance += 1
            print('\nYou go and lay down on the bed, some rest will help your mind wrap around this. You fall asleep rather quickly, and wake up a few hours later, you feel more sturdy and level-headed. you go to the screen and it begins to type, "Taking vitals... you are stable prisoner, time to select your new lifeform."')
        if choice == 'C' or choice == 'c':
            player1.strength += 1
            print(player1.strength)
            print('\nYou begin to do a full body workout, hitting every muscle in your body. you head feels clearer and sharper as you work. once youre done you strech out, releasing the lactic acid from your muscles, feeling more energetic and ready for action. you go to the screen and it begins to type " Taking vitals... you are stable prsioner, time to select your new lifeform.\n')
        if choice == 'D' or choice == 'd':
            player1.speed += 1
            print('\nYou run circles around the cell, you make many circles because its not very big but after a while you begin to sweat, you can feel your heart rate speeding up. you run until youre severly out of breath. you stop and rest in front of the screen and the screen responds "Taking vitals... You are stable prisoner, It is time to select your new lifeform.')
        reset_choice()
        print("Lets start with your species. I can put you into a custom body of any race you would like using my controlled mutation procedures. you will be put under \nanesthesia for this procedure. The races you can choose from are as follows:\nHuman - The metropolitan race, standing at about 5'8 and weighing about 140 pounds. they are the jack of all trades, medium-low in all categories, but\nthey have a tendency to succeed where they shouldn't.\nLhugan - A reptilian race covered in scales standing at an impressive 6'6 and weighing about 250 pounds. they have a high endurance, medium strength, low speed, and low intelligence. They are able to run in 4 legs for a short distance at great speed, but are often very unlucky.\nCarchor - A feline race that resemble humans in size and build, weighing lighter at only 120 pounds they are covered in fur from head to toe and have\nlarge ears and a tail. they have a high speed medium-high intelligence, medium endurance, and a low strength, but they're claws make excellent weapons and\nthey can seen well in the dark. \nSaela - taller than humans standing at 7' the tallest of all races due to this they weigh 200 pounds, but are still quite thin,\nother than height the bottom of their ears is long and pointed. It is rumored that they have some magical ability, but no proof has ever been found. they\nhave a high Intelligence, medium Speed low Strength and low Endurance. \nFinally you may chose to be a Nornonion, the shortest and most heavy set of the races, standing at 4'10 and weighing about 150 pounds, they have long hair\nand beards, and an affinity to craft things. They have a high strength, medium endurance, low speed, and low intelligence.")
        while player1.race == 'unknown':
            player1.race = (input('\nPlease say the name of the race you would like to be.\n')).capitalize()
            if player1.race == 'Human':
                player1.endurance += 2
                player1.intelligence += 2
                player1.luck += 5
                player1.speed += 2
                player1.strength += 2
            elif player1.race == 'Lhugan':
                player1.endurance += 5
                player1.intelligence += 1
                player1.luck += 1
                player1.speed += 2
                player1.strength += 4
            elif player1.race == 'Carchor':
                player1.endurance += 1
                player1.intelligence += 4
                player1.luck += 3
                player1.speed += 5
                player1.strength += 1
            elif player1.race == 'Saela':
                player1.endurance += 1
                player1.intelligence += 5
                player1.luck += 3
                player1.speed += 3
                player1.strength += 1
            elif player1.race == 'Nornonion':
                player1.endurance += 4
                player1.intelligence += 1
                player1.luck += 2
                player1.speed += 1
                player1.strength += 5


run()
'''
continue the story, add a punch the screen option for the lolz, decide different races/species, code in insanity,
:
species
speed-SP intelligence-I strength-St endurance- E luck-L
1-low 2-medium-low 3-medium 4- medium-high 5-high
Human - medium-low SpIStE high L, Lhugan - low I medium Sp medium St high E low L, Carchor - medium-high I high Sp low St low E medium L,
Saela - high I medium Sp low St low E medium L, Nornonion - low I  low Sp High S medium E medium L 
:
insanity
great - I buff E buff, good small I buff, okay none, bad random song lyrics small I debuff, insane communist manifesto random song lyrics I debuff E debuff
'''
