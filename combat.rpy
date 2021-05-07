screen combat:
    style_prefix "combat"

    # Enemy sprite
    add e.img xalign 0.7

    # Player HP
    frame:
        padding (40, 40)
        xalign 0
        yalign 0.7

        label "Maestro HP: [p.hp]"

    # Enemy HP
    frame:

        padding (40, 40)
        xalign 1.
        yalign 0.3

        vbox:
            spacing 20
            label "[e.name]" xalign 0.5
            label "HP: [e.hp]" xalign 0.5

label start_fight_test:

    # Create random enemy
    $enemyStats = renpy.random.choice(et_test)
    $e = Enemy(enemyStats[0], enemyStats[1], enemyStats[2], enemyStats[3], enemyStats[4], enemyStats[5], enemyStats[6], enemyStats[7])

    # Show combat screen
    show screen combat

    # Start fight
    jump fighting

label start_fight_tuto:

    # Create bandit enemy
    $e = Enemy("bandit", "Bandit", 20, 5, 0, lt_0, 25, 3)

    # Show combat screen
    show screen combat

    # Start fight
    jump fighting

label start_fight_miniQuest1:

    # Create mini boss
    $e = Enemy("apprentice", "Aprentice Wizard", 100, 15, 15, lt_1, 20, 10)

    # Show combat screen
    show screen combat

    # Start fight
    jump fighting

label start_fight_quest1:

    # Create boss
    $e = Enemy("wizard", "Tuba Wizard", 400, 30, 15, lt_1_boss, 100, 20)

    # Show combat screen
    show screen combat

    # Start fight
    jump fighting

label start_fight_miniQuest2:

    # Create mini boss
    $e = Enemy("gunner", "Tuba Gunner", 350, 35, 50, lt_2, 60, 12)

    # Show combat screen
    show screen combat

    # Start fight
    jump fighting

label start_fight_quest2:

    # Create boss
    $e = Enemy("heavy gunner", "Heavy Gunner", 1000, 40, 60, lt_2_boss, 200, 25)

    # Show combat screen
    show screen combat

    # Start fight
    jump fighting

label start_fight_miniQuest3:

    # Create mini boss
    $e = Enemy("fencer 1", "Violin Fencer", 1750, 85, 95, lt_3, 250, 23)

    # Show combat screen
    show screen combat

    # Start fight
    jump fighting

label start_fight_quest3:

    # Create boss
    $e = Enemy("fencer 2", "Violin Fencer", 1300, 110, 115, lt_3_boss, 0, 32)

    # Show combat screen
    show screen combat

    # Start fight
    jump fighting

label start_fight_quest4:

    # Create mini boss
    $e = Enemy("knight", "Tuba Knight", 2000, 100, 250, lt_4_boss, 300, 30)

    # Show combat screen
    show screen combat

    # Start fight
    jump fighting

label start_fight_quest4a:

    # Create boss
    $e = Enemy("king 1", "Tuba King", 3000, 120, 200, lt_4_boss, 350, 40)

    # Show combat screen
    show screen combat

    # Start fight
    jump fighting

label start_fight_quest4b:

    # Create boss
    $e = Enemy("king 2", "Tuba King", 2999, 180, 180, lt_4_boss, 500, 45)

    # Show combat screen
    show screen combat

    # Start fight
    jump fighting

label start_fight_option2:

    # Create boss
    $e = Enemy("queen", "Tuba Queen", 5000, 200, 150, lt_4_boss, 0, 100)

    # Show combat screen
    show screen combat

    # Start fight
    jump fighting

label start_fight_option2a:

    # Create boss
    $e = Enemy("queen 2", "Tuba Queen", 666, 220, 390, lt_4_boss, 100000, 10000)

    # Show combat screen
    show screen combat

    # Start fight
    jump fighting

label start_fight:

    # Get enemy table
    if act == 1:
        $et_now = et_1
    elif act == 2:
        $et_now = et_2
    elif act == 3:
        $et_now = et_3
    elif act == 4:
        $et_now = et_4
    else:
        $et_now = et_test

    # Create random enemy
    $enemyStats = renpy.random.choice(et_now)
    $e = Enemy(enemyStats[0], enemyStats[1], enemyStats[2], enemyStats[3], enemyStats[4], enemyStats[5], enemyStats[6], enemyStats[7])

    # Show combat screen
    show screen combat

    # Start fight
    jump fighting

menu fighting:

    "Light Attack":
        $atk = p.atk(0)
        jump player_turn

    "Normal Attack":
        $atk = p.atk(1)
        jump player_turn

    "Heavy Attack":
        $atk = p.atk(2)
        jump player_turn

    "Potions":
        menu:
            "Drink small potion ([p.potions[0]])":
                $p.consume(0)
                jump fighting

            "Drink medium potion ([p.potions[1]])":
                $p.consume(1)
                jump fighting

            "Drink large potion ([p.potions[2]])":
                $p.consume(2)
                jump fighting

            "Cancel":
                jump fighting

    "Run Away":

        # Reset current quest (if active)
        $questing = False

        if miniQuestsStatuses[0] != 4:
            $miniQuestsStatuses[0] = 0

        elif miniQuestsStatuses[1] != 3:
            $miniQuestsStatuses[1] = 0

        elif miniQuestsStatuses[2] != 2:
            $miniQuestsStatuses[2] = 0

        elif questsStatuses[3] < 6:
            $questsStatuses[3] = 0

        hide screen combat
        jump goto_town

label player_turn:

    # Deal damage to enemy
    $trueDmg = e.takeDmg(atk[1])
    "You used [atk[0]] and dealt [trueDmg] damage!"

    # Check for enemy death
    if e.isDead():
        "You have defeated [e.name]!"
        hide screen combat

        # Quest advance (if quest)
        if questing:

            if act == 1:
                if miniQuestsStatuses[0] < 4:
                    $miniQuestsStatuses[0] += 1
                else:
                    $questsStatuses[0] += 1

            elif act == 2:
                if miniQuestsStatuses[1] < 3:
                    $miniQuestsStatuses[1] += 1
                else:
                    $questsStatuses[1] += 1

            elif act == 3:
                if miniQuestsStatuses[2] < 2:
                    $miniQuestsStatuses[2] += 1
                else:
                    $questsStatuses[2] += 1

            elif act == 4:
                $questsStatuses[3] += 1

        # Reward
        # Money (80-120%)
        $lo = int(.8 * e.reward)
        $hi = int(1.2 * e.reward)
        $reward = renpy.random.randint(lo, hi)
        $p.money += reward

        "You have gained $[reward]."

        # XP (80-120%)
        $lo = int(.8 * e.xp)
        $hi = int(1.2 * e.xp)
        $xp = renpy.random.randint(lo, hi)
        $levelUp = p.giveXP(xp)

        "You have gained [xp] xp."
        if levelUp:
            "You have leveled up!"

        # Loot
        python:
            roll = renpy.random.randint(0, 100)

            if roll > 80:          # No loot (80%)
                # Calculate total weight
                total_weight = 0
                for weight in e.loot_table.values():
                    total_weight += weight

                roll = renpy.random.randint(1, total_weight)

                # Roll loot
                look = 0
                for loot, weight in e.loot_table.items():
                    look += weight
                    if roll <= look:
                        break

                # Put loot in player's inventory
                for amount, item in loot[1:]:
                    for _ in range(amount):
                        p.give(item)

                    narrator("You found: {} x {}.".format(amount, item.name))

        # Go back to town
        jump goto_town

    # Not dead, enemy's turn
    jump enemy_turn

label enemy_turn:

    # Deal damage to player
    $atk = e.atk()
    $trueDmg = p.takeDmg(atk[1])
    "[e.name] used [atk[0]] and dealt [trueDmg] damage!"

    # Check for player death
    if p.isDead():
        "You are dead."
        $MainMenu(confirm=False)()
        # hide screen combat
        # jump goto_town

    # Not dead, continue fight
    jump fighting
