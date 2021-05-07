define king = Character("Tuba King")
define queen = Character("Tuba Queen")
define mess = Character("Queen's Messenger")
define wiza = Character("Tuba Wizard")
define appr = Character("Tuba Apprentices")
define hgun = Character("Heavy Tuba Gunner")
define fenc = Character("Corrupted Violin Fencer")
define fenc2 = Character("Violent Violin Duelist")
define knight = Character("Tuba Knight")
define mgun = Character("Mini Tuba Gunners")
define merc = Character("Merchant")
define bandit = Character("Tuba bandit")
define guard = Character("Tuba guards")
define m = Character("Maestro")
define v = Character("Villager")
define t = Character("Tutorial")

init 3 python:

    # Player instance
    p = Player()

    # Testing
    # p.inv[diamond_sword] = 1
    # p.inv[shield] = 1
    # p.hp = 20
    p.potions = [2, 0, 0]

    # Important variables
    act = -2
    styles = ["light attack", "normal attack", "heavy attack"]
    potionPrices = [10, 25, 50]

    # Less important variables
    finding = 0
    reward = 0
    levelUp = False
    atk = ["normal attack", 0]
    selected_item = None
    selected_potion = 0
    shopping = False
    current_shop = st_test
    et_now = None
    roll = 0
    current_music = None
    questing = False
    miniQuestsStatuses = [0, 0, 0]
    questsStatuses = [0, 0, 0, 0]

# The game starts here.

label start:

    # Force reset
    python:

        # Equipment
        for equipment in p.equipment.values():
            if equipment:
                equipment.unequip()

        # Player instance
        p = Player()

        # Testing
        # p.inv[diamond_sword] = 1
        # p.inv[shield] = 1
        # p.hp = 20
        p.potions = [2, 0, 0]

        # Important variables
        act = -2
        styles = ["light attack", "normal attack", "heavy attack"]
        potionPrices = [10, 25, 50]

        # Less important variables
        finding = 0
        reward = 0
        levelUp = False
        atk = ["normal attack", 0]
        selected_item = None
        selected_potion = 0
        shopping = False
        current_shop = st_test
        et_now = None
        roll = 0
        current_music = None
        questing = False
        miniQuestsStatuses = [0, 0, 0]
        questsStatuses = [0, 0, 0, 0]

    scene bg forest

    play music prologue loop

    "Once upon a time, there lay 4 kingdoms."
    "The kingdom of Strings."
    "The kingdom of Woodwind."
    "The kingdom of Percussion."
    "And the kingdom of Brass."
    "For long they lived in harmony, until one day the kingdom of Brass declared
     war on all the land, devouring whatever lay in its greedy path for power."
    "To this day, the land of the Orchestria remains dominated by the
    near-undefeatable kingdom of brass and its delusional monarch, King Tuba II."
    "And yet, hope remains."
    "A small orchestral group, consisting of rebel Brass warriors, and a few surviving members of the old orchestra, take up their arms and decide to wage a final war against the Kingdom."
    "Though heavily outnumbered and lacking resources, they must prove their worth and skill if they are to bring down the reign of the Tuba king and his Brass kingdom."
    "They will face the elusive Tuba Wizard, a mage undefeated in his conducting skill"
    "The Heavy Tuba Gunner, a juggernaut whose destructive power and sheer durability remains second to none"
    "Finally, behind several ranks and waves of Tuba Knights, the legendary guard of the Tuba King himself."
    show messenger R
    v "Hey you, finally awake!"
    m "Where… am I?"
    v "We found you under the bridge, riddled with wounds. Do you recall anything?"
    m "I… have no recollection of anything… I don’t… know."
    v "Perhaps, you got hit on the head, the memory will come back, don’t worry. Do you-"
    v "AMBUSH AHEAD!"
    hide messenger R
    show bandit

    play music battle loop

    bandit "Huh! Another test subject!"
    hide bandit
    jump start_fight_tuto


label tuto1:

    play music prologue loop

    # Heal player after fight
    $p.hp = p.maxHP

    $act = -1
    show messenger L
    v "Nice tune there! I see that you have a lot of experience! You should consider enlisting in the Orchestria of Insurrection. You can enlist in our village right ahead."
    m "(Why does this name sound so familiar…)"

    play music merchant loop

    scene bg shop

    merc "Hello Maestro! Welcome to the town of HoneyBrass! How can I help you?"
    t "Click on item to select. Click buy to buy the item. Click return to return to Town."

    $shopping = True
    call screen shop_screen

label tuto2:

    play music prologue loop

    $act = 1
    show messenger R
    "After coming out of the shop, a villager is awaiting you."
    v "Hey adventurer, did you know that the bandits you killed were Tuba Wizard’s lackeys?"
    v "They are tasked to kidnap other instruments in order to fulfill his experiments."
    v "Now that you have killed them, they will try to take their revenge."
    m "And what do you want by telling me this?"
    hide messenger R
    show messenger L
    v "I have seen your skills and to be honest, few can match your musical talent. Hence, I would like your help with a task, consider it a commission of a sort…"
    m "What is the commission?"
    v "It consists of a rescue mission. As I have said earlier on, a few villagers have been kidnapped recently and I think I have found their headquarters."
    v "I would like  you to investigate that location and try to at least save 4 villagers."
    m "I better get paid for this!"
    hide messenger L
    show messenger R
    v "Of course! The whole village will generously reward you for this."

    scene bg town

    t "Begin tutorial for Inventory, Explore, Proceed to Quest."
    t "Click on item in Inventory to select and equip them."
    t "Click on Explore to fight monsters, gain gold, gain experience, and even equipment."
    t "Click on Proceed to Quest to continue with the story. You better be prepared."
    t "Psst: Stack a lot of potions. You will need them."

    jump goto_town

label miniQuest1:

    play music battle loop

    scene bg forest
    "You proceed to the location Villager indicated for you. As expected, you discover there are many wizard apprentices patrolling the area. You try to sneak into the building…"
    appr "INTRUDER!!!"
    scene bg lab
    jump start_fight_miniQuest1

label miniQuest1a:

    play music act1 loop

    "After the musical face-off, you proceed into the building, searching for the kidnapped villagers as you stumble into the laboratory. You discover the villagers, although battered, they seem alive and kicking…"
    scene bg town
    show messenger L
    v "Ah, Maestro! You’ve returned with the saved villagers."
    m "Yes I have and I would like my reward."
    v "Maestro where are the other villagers?"
    m "You told me to save 4 villagers from the headquarters."
    v "I said save at least 4 villagers from the bandit camp."
    m "Well I saved 4 villagers."
    hide messenger L
    show messenger R
    v "Maestro, there were 14 villagers of HoneyBrass abducted, you are telling me you only saved 4 of them?"
    m "EHEH!"
    v "WHAT DO YOU MEAN EHEH!"
    m "Well excuse me if anyone is at fault here, it is you for not being specific enough with your quest. You told me to save 4 villagers which I did. Now give me my reward."
    hide messenger R
    show messenger L
    v "Fine! I have another task for you. Now that you have ruined Tuba Wizard’s plan, he is most likely going to try finding you."
    v "However, we will try to get the upper hand by going to HIS arcane tower first. Keep in mind that Tuba Wizard is a masterful magic-user from The Brass Kingdom."
    v "He is also known as the Brass Magician. Brother to the Tuba Knight and Heavy Tuba Gunner, Tuba wizard fought in the Music War and made his name well known in The Brass Kingdom."
    hide messenger R
    show messenger L
    v "His reputation made him quite a celebrity in The Brass Kingdom and stories about how he handled the Brass magic during wartime are legendary."
    m "Alright, you better pay me even more for this."
    jump goto_town

label quest1:

    play music wizard loop

    scene bg arcane tower
    wiza "I have expected your arrival adventurer. To have ruined my plans, you shall suffer my wrath! WITNESS MY GREAT UNDERTAKING!"
    m "You seem a bit familiar."
    wiza "Don’t even try to talk your way out, your only fate is death."
    jump start_fight_quest1

label quest1a:

    play music act1 loop

    "A portal appears suddenly, expecting an enemy, you ready your instrument. However, a woman in an elegant dress appears and behind her, follows villager."
    show messenger L
    v "Well done Maestro! You have proven yourself worthy to be the hero of BrassWood! Let me present to you her Majesty Queen Tuba!"
    hide messenger L
    show queen
    queen "Hello Maestro, I am Queen Tuba, the Queen of the Brass Kingdom. I have been monitoring you through my messenger, villager for a while and I must admit that your musical talent is truly unrivaled."
    m "I am no hero, nor do I care about your true identities. I finished my task and I am awaiting my rewards."
    queen "No rush Maestro, I am here for your rewards as well as future cooperation. My husband, King Tuba has become mad with power after being corrupted and I wish an end to the bloodshed he caused."
    queen "Hence, I want your help. I will give you quests through my messenger and for every quest you complete, I will of course reward you generously!"
    queen "If you manage to help me end this bloodshed I will even give you a title and a land. What do you think?"
    show messenger R
    hide queen
    mess "With your fame, you will also enjoy a better reputation and life!"
    m "Hmmm… as long as there are rewards I am open for commissions."
    hide messenger R
    show queen
    queen "Thank you, you will hear news from my messenger soon!"
    "Queen Tuba teleports away and her messenger guides you back to the village..."
    pause

    scene bg forest
    "A month has passed, indulging in your fame and wealth, you have done nothing."
    "Your name, however, has spread far enough to catch the ear of the Heavy Tuba Gunner, the bounty hunter feared by all."
    "From ear to ear, he learned that you have killed his brother, the Tuba Wizard. Now his wrath is upon you."
    scene bg town
    show messenger R
    mess "Maestro, please hear me out! The Queen needs your help."
    m "What do you want this time?"
    mess "The Heavy Tuba Gunner learned about the death of the Tuba Wizard and he is now hunting for your head."
    m "And?"
    mess "He has captured the insurrection’s military bunker. He threatens that if you don’t go to him in the next month, he will kill all the innocent people there!"
    m "K"
    show messenger R
    hide messenger L
    mess "What do you mean “K”? Don’t you have a heart, don’t you pity them?"
    mess "Ok. I know!"
    show messenger L
    hide messenger R
    mess "Dear Maestro, would you like to accept this humble messenger’s quest. You will be handsomely rewarded."
    m "You had my curiosity, but now, you have my attention!"
    mess "This quest consists of two parts. First, please save the insurrection’s army in the Heavy Tuba Gunner’s dungeon."
    m "Don’t forget the reward."
    hide messenger L
    $act = 2
    jump goto_town

label miniQuest2:

    play music battle loop

    scene bg forest
    "You proceed to the appointed location. From far away, you can see tubas torturing, shaming, and destroying the insurrection’s army."
    "You approach carefully thinking about a plan to safely free all those prisoners, safe for you ofcourse."
    scene bg prison
    "As you crawl slowly inside the facility, you suddenly hear: INTRUDER ALERT!!!"
    jump start_fight_miniQuest2

label miniQuest2a:

    play music act2 loop

    "While fighting against the enemies, you ended up in some kind of control room."
    "You see a big red button and without hesitation and without any knowledge of what it does, you press it with all your might."
    "An even bigger alarm sounds through the dungeon, all the prison doors open, you just freed the militia."
    "Fighting with them, you successfully escape with most of the group still alive."
    pause
    show messenger R
    mess "O my god Maestro, you did it. You rescued the army of insurrection. Here! The first part of your payment, you will need it."
    "The messenger hands you some gold."
    m "What do you mean?"
    mess "Have you forgotten the second part of our contract?"
    hide messenger R
    show messenger L
    mess "Maestro, I hereby declare you to kill the Heavy Tuba Gunner. If you do that an even bigger reward will be presented to you by the Queen."
    m "“sigh”. Fine."
    hide messenger L
    jump goto_town

label quest2:

    play music heavyGunner loop

    scene bg prison
    show heavy gunner
    "As you proceed to Heavy Tuba Gunner’s encampment, you hear sounds expressing intense rage…"
    "There stood Heavy Tuba Gunner, armed to the teeth and ready to avenge his brother."
    hide heavy gunner
    jump start_fight_quest2

label quest2a:

    play music act2 loop

    "Although the fight was difficult, you remain victorius. Dragging your wounded body, you return to town."
    scene bg town
    mess "As expected! You return victorious Maestro, here is your reward."
    pause
    "Bathing in your gold and glory, you lost yourself in lust and sloth."
    "For three month you have done nothing, yet every night, you have an ominous premonition."
    "You can’t grasp what it is but you have a feeling it is about your past."
    show messenger R
    mess "Maestro, have you heard about the Corrupted Violin Fencer."
    m "What do you want this time?"
    m "(Why does he sound familiar?)"
    mess "He had been wandering around the kingdom of Brass killing all the soldiers of insurgence."
    mess "Although he was once a good comrade, now we have no choice but to put him down."
    m "And what does it have to do with me?"
    mess "“Sign”"
    hide messenger L
    show messenger R
    mess "(Monotonous voice) Dear Maestro, would you like to accept a quest from this lowly messenger of the queen. You will be humbly rewarded."
    m "Let’s sit down and talk about your problem."
    mess "Please take down the Corrupted Violin Fencer, he was last seen around the River of Reminiscence."
    hide messenger R
    $act = 3
    jump goto_town

label miniQuest3:

    play music battle loop

    scene bg river
    "While hunting some lackys of the king around the river, you, suddenly, feel a chill down your spine."
    "That familiar yet cold presence, there is no mistake. It is him. You follow his trail and prepare to ambush him, but he turns around and lands the first hit."
    jump start_fight_miniQuest3

label miniQuest3a:

    play music act3 loop

    "The Violent Violet Duelist was too strong, but for some reason, he didn’t end your life right there. You took this opportunity and fled for your life."
    pause
    show messenger R
    mess "Hey Maestro, I see you are back. Looking at your state, I presume you failed."
    m "You didn’t tell me he has a second form!"
    mess "EHEH!"
    m "(Has a flashback) …"
    mess "Here take this, maybe this will be any help to your fight."
    "You have received one gold."
    $p.money += 1
    mess "One gold of pity."
    hide messenger R
    jump goto_town

label quest3:

    play music fencer loop

    scene bg river
    jump start_fight_quest3

label quest3a:

    play music act3 loop

    scene bg river
    "You look upon the soundless body of what was once a friend. Memorie gushes in."
    "You remember the last battle you had with your comrades."
    "You remember the adventures with your precious friend."
    "You remember your hatred towards this tyranny."
    "You remember the dead body of your family in the hand of the brass legion."
    "You now have a goal, a vendetta to settle."
    pause
    "With your memory back and a vendetta to settle, you travel towards the Brass Kingdom, vanquishing any foes that dare block your way."
    "With the aid of the Tuba Queen and his messenger, you manage to avoid most obstacles and reach the castle with much difficulty."
    show messenger L
    mess "The time is upon us, you have reached the gate of Brass Castle."
    mess "Behind it lies the throne of Tuba King II and the residence of Her Majesty Tuba Queen."
    mess "However, the castle is heavily guarded and it will be an impossible task for you alone to engage the whole Brass Army."
    mess "Hence, at night, right before the guards switch, you will disguise as me and seek an audience with her Majesty where you will travel to the throne room to fight the Tuba King II."
    m "Very well, as long as I get to kill him."
    hide messenger L
    $act = 4
    jump goto_town

label quest4:

    play music knight loop

    scene bg throne room 1
    "With a plan, you successfully infiltrate the castle and reach the throne room."
    "While King Tuba II does not seem to be alone, there are not many guards beside him either."
    "Accustomed to fighting overnumbered, you charge into the room in order to avenge your former comrades!"
    show knight
    knight "WHO GOES THERE!"
    "(You remembered stealth is optional.)"
    hide knight
    jump start_fight_quest4

label quest4a:

    play music king loop

    show knight
    knight "Your Majesty… I... failed you. Brothers… I am joining you…"
    hide knight
    show king 1
    king "Foolish child... it seems your little rebellion was more of a threat than I realized. My congratulations."
    m "Your reign of terror ends here, King."
    king "Terror? You know nothing of terror, boy. Before the empire, Orchestria was plagued with endless war, endless suffering. Through unification, I brought peace. Peace to all of Orchestria."
    m "And those who would not submit to your ‘peace’, you destroyed."
    hide king 1
    jump start_fight_quest4a

label quest4b:

    play music king2 loop

    show king 1
    king "I could say the same to you, Maestro. How many Tubonians have you slain on your warpath?"
    king "How many innocents lie dead, starved in their own homes because of a war of your creation?"
    m "That's different."
    king "Is it? Or are you too afraid to admit you’ve become what you seek to destroy?"
    m "I’m not like you, king."
    m "When we are finished the four kingdoms will stand strong once more. Woodwind will reclaim their home."
    m "The percussion parliament will be reinstated, and the people will speak for themselves once more."
    m "String will renounce your laws and live freely. And Brass will be rid of their tyrant king."
    king "And thus, all our problems are wiped away, yes?"
    king "You are a naive fool, Maestro, if you think your peace will last more than a decade."
    king "Before long, the nations will be at each other's throats once more, and all you have sacrificed will have been for nothing."
    m "We’ll just have to see, king."
    hide king 1
    jump start_fight_quest4b

label quest4c:

    play music epilogue loop

    show king 1
    king "Congratulations, Maestro...I'm dying...Thank the stars, I'm not going to see what will happen to Orchestria."
    m "A golden era awaits us."
    king "You're deluded. Only through unification, you can reach true peace...other kingdoms are going to abuse their power, their goal is not peace."
    king "You too."
    m "No, we won’t."
    king "Your rebellion dies with you, I’ll make sure of that."
    king "Play your final tune, Maestro. Your song ends here."
    m "Freedom from my people and from citizens of my allies!"
    king "The only thing I took from your friends is the power they had."
    king "To ensure that no one will ever take peace from Orchestria again...but it doesn't matter now."
    king "You returned their power to them...now my people are doomed."
    m "Your citizens have nothing to do with your decisions."
    king "Remember my words...you will see with your own eyes, how my people are going to suffer, how fast corruption will grow in the ranks..."
    king "let that sight remind you of...this day...of the opportunity you had to prevent all of this. The era of discord awaits Orchestria..."
    "The King dies."
    hide king 1
    pause
    show queen
    queen "Congratulations Maestro, you have saved the Kingdom of Brass and Orchestria! On behalf of the Kingdom of Brass, I thank you."
    hide queen
    "In the stillness of the aftermath, all that is heard is the distant wind, you should feel victory and satisfaction, however all that you feel is an empty void…"
    "As if nothing has been solved… The King told you about corruption, however was he… not the corrupted one?"
    "Through your conversation with him, you knew he was not mad… but if he was not, could he not see his own tyranny?"
    "Or was there more…"
    pause
    "3 days later..."
    show queen
    queen "Maestro, you have done much good in your life and for saving Orchestria from the tyranny of the old Tuba King II, you saved my Kingdom too… "
    queen "Hence, I would like to knight you and give you the title of Duke for your accomplishments!"
    menu:
        "Accept the title and become a duke.":
            jump option1
        "(Something is wrong… the corruption!) No, you are not fit to rule this Kingdom!":
            jump option2
    hide queen

label option1:

    scene bg town
    "Queen Tuba gains the absolute control of the Kingdom, while you enjoy your life leisurely in your own Dukedom."
    "Is she ruling the Kingdom fairly or is she like the old Tuba King, spreading tyranny everywhere…"
    "You do not know or care as you drown in your own fame and riches..."
    $MainMenu(confirm=False)()

label option2:

    $questsStatuses[3] += 1
    play music queen loop

    scene throne room 2
    show queen
    queen "And you think you are more fit?! Ahahahaha… men are all the same! To think you would defy me!"
    m "I was wondering why after killing the King, I could still feel the corruption. He was corrupted, but he was not the source… you were!"
    queen "You know nothing! This power… is absolute! None can rival it and no one shall stop my thirst and desire for the throne!"
    m "Ha… so all this was your design!"
    hide queen
    call screen inventory_screen

label option2a:

    play music queen2 loop

    scene bg throne room 2
    show queen
    queen "YOU FOOL! That was not even my final form!"
    m "OK"
    queen "You shall witness my ultimate form! This is absolute power!"
    m "OK"
    queen "Suffer my wrath!"
    m "OK"
    hide queen
    jump start_fight_option2a

label option2b:

    play music epilogue loop

    show queen 2
    queen "How is this possible? How..."
    m "I have the power of God and anime by my side! That is why!"
    queen "AAAAARRRRGH!!"
    hide queen
    scene bg throne room 1
    "With the defeat of Queen Tuba, the corruption is no more and you become the King. Peace came back to Orchestria and people rejoiced under your reign while it lasted."
    "History later records you as a generous and righteous King who eliminated the corruption of the land and blessed the people with prosperity."
    pause
    $MainMenu(confirm=False)()
