screen shop_screen:
    style_prefix "shop"

    # Reset selected item for Item stats
    # $SetVariable("selected_item", None)

    # Background
    # add "inventory background"
    add "bg shop"

    # Get current shop
    if act == 1:
        $current_shop = st_1
    elif act == 2:
        $current_shop = st_2
    elif act == 3:
        $current_shop = st_3
    elif act == 4:
        $current_shop = st_4
    elif act == -1:
        $current_shop = st_tuto
    else:
        $current_shop = st_test

    hbox:

        spacing 20
        xalign 0.98
        yalign 0.2

        vbox:

            # Shop grid #
            grid 4 5:

                spacing 10

                # Display all available items in shop
                for item in current_shop:
                    frame:
                        style "slot"
                        imagebutton idle item.img xalign 0.5 yalign 0.5 action SetVariable("selected_item", item)

                # Fill empty slots
                for _ in range(len(current_shop), 20):
                    frame:
                        style "slot"

            # Potions #
            # Small
            textbutton "Buy small potion ([p.potions[0]]): $[potionPrices[0]]" xalign 0.5 action Function(p.buyPotion, 0)

            # Medium
            textbutton "Buy medium potion ([p.potions[1]]): $[potionPrices[1]]" xalign 0.5 action Function(p.buyPotion, 1)

            # Large
            textbutton "Buy large potion ([p.potions[2]]): $[potionPrices[2]]" xalign 0.5 action Function(p.buyPotion, 2)

        # Item stats #
        vbox:

            spacing 20
            xmaximum 300

            label "Selected Item" xalign 0.5

            if selected_item:
                frame:
                    style "slot" xalign 0.5
                    add selected_item.img xalign 0.5 yalign 0.5

                # Name
                label "Name: [selected_item.name]" xalign 0.5

                # Value
                label "Value: $[selected_item.value]" xalign 0.5

                # Equippable
                if isinstance(selected_item, Equippable):

                    # Weapon Dmg
                    if isinstance(selected_item, Weapon):
                        label "Attack: [selected_item.dmg]" xalign 0.5

                    # Armor defense
                    else:
                        label "Defense: [selected_item.defense]" xalign 0.5

                # Buy button
                textbutton "Buy":
                    action Function(p.buy, selected_item)
                    xalign 0.5

    # Display current money
    label "Money: [p.money]":
        xalign 0.2
        yalign 0.95

    # Inventory button
    textbutton "Inventory":
        action [SetVariable("selected_item", None), Hide("shop_screen"), Show("inventory_screen")]
        xalign 0.5
        yalign 0.95

    # Return button
    textbutton "Return":
        action [SetVariable("shopping", False), Hide("shop_screen"), Call("goto_town")]
        xalign 0.8
        yalign 0.95
