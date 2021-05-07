menu test_town:

    "Inventory":
        call screen inventory_screen

    "Shop":
        $shopping = True
        call screen shop_screen

    "Test fight":
        jump start_fight_test

    "Stop":
        return

menu town1:

    "Inventory":
        $selected_item = None
        call screen inventory_screen

    "Shop":

        # Music
        play music merchant loop

        $selected_item = None
        $shopping = True
        call screen shop_screen

    "Explore":
        jump explore

    "Proceed to Quest":
        $questing = True
        jump goto_quest

label goto_quest:

    if act == 1:

        if miniQuestsStatuses[0] == 0:      # mini quest
            $miniQuestsStatuses[0] = 1
            jump miniQuest1

        else:               # real quest
            $questsStatuses[0] = 1
            jump quest1

    elif act == 2:

        if miniQuestsStatuses[1] == 0:      # mini quest
            $miniQuestsStatuses[1] = 1
            jump miniQuest2

        else:               # real quest
            $questsStatuses[1] = 1
            jump quest2

    elif act == 3:

        if miniQuestsStatuses[2] == 0:      # mini quest
            $miniQuestsStatuses[2] = 1
            jump miniQuest3

        else:               # real quest
            $questsStatuses[2] = 1
            jump quest3

    elif act == 4:

        if questsStatuses[3] == 0:          # Start quest 4
            $questsStatuses[3] = 1
            jump quest4

        else:               # Fight queen
            jump start_fight_option2

label explore:

    scene bg forest

    play music battle loop

    $roll = renpy.random.randint(0, 100)

    # Large potion
    if roll < 2:
        "You found a large potion!"
        $p.potions[2] += 1

    # Medium Potion
    elif roll < 5:
        "You found a medium potion!"
        $p.potions[1] += 1

    # Small potion
    elif roll < 10:
        "You found a small potion!"
        $p.potions[0] += 1

    # Money
    elif roll < 15:
        $finding = renpy.random.randint(0, 10 * (act ** 2))
        "You found $[finding]!"
        $p.money += finding

    # Fight
    else:
        jump start_fight

label goto_town:

    if questing:

        if act == 1:

            if miniQuestsStatuses[0] < 4:       # Mini quest repeat fight 3 times
                jump start_fight_miniQuest1

            else:               # Mini quest 1 done

                if questsStatuses[0] == 0:      # End mini quest 1
                    $questing = False
                    jump miniQuest1a

                elif questsStatuses[0] < 2:     # Quest 1
                    jump quest1

                else:               # End quest 1
                    $questing = False
                    jump quest1a

        elif act == 2:

            if miniQuestsStatuses[1] < 3:       # repeat fight 2 times
                jump start_fight_miniQuest2

            else:               # Mini quest 2 done

                if questsStatuses[1] == 0:      # End mini quest 2
                    $questing = False
                    jump miniQuest2a

                elif questsStatuses[1] < 2:     # Quest 2
                    jump quest2

                else:               # End quest 2
                    $questing = False
                    jump quest2a

        elif act == 3:

            if miniQuestsStatuses[2] < 2:       # Fight only once
                jump start_fight_miniQuest3

            else:               # Mini quest 3 done

                if questsStatuses[2] == 0:      # End mini quest 3
                    $questing = False
                    jump miniQuest3a

                elif questsStatuses[2] < 2:     # Quest 3
                    jump quest3

                else:               # End quest 3
                    $questing = False
                    jump quest3a

        elif act == 4:

            if questsStatuses[3] == 2:      # Fight king 1
                jump quest4a

            elif questsStatuses[3] == 3:      # Fight king 2
                jump quest4b

            elif questsStatuses[3] == 4:      # End quest 4 go to options
                jump quest4c

            elif questsStatuses[3] == 5:      # Fight queen 1
                jump start_fight_option2

            elif questsStatuses[3] == 6:      # Fight Queen 2
                jump option2a

            elif questsStatuses[3] == 7:      # Second ending
                $questing = False
                jump option2b

    else:           # Not questing

        show bg town

        if act == -2:
            jump tuto1

        elif act == -1:
            jump tuto2

        elif act == 0:
            jump test_town

        else:

            # Music
            $current_music = renpy.music.get_playing()

            if act == 1:
                if current_music != "music/act1.mp3":
                    play music act1 loop
            elif act == 2:
                if current_music != "music/act2.mp3":
                    play music act2 loop
            elif act == 3:
                if current_music != "music/act3.mp3":
                    play music act3 loop
            elif act == 4:
                if current_music != "music/epilogue.mp3":
                    play music epilogue loop

            jump town1
