style slot:
    background Frame("slot.png", 0, 0)
    minimum(130, 130)
    maximum(130, 130)
    xalign 0.5

screen drink_potion_screen:
    style_prefix "drink_potion"

    frame:
        padding (40, 40)
        xalign 0.5
        yalign 0.5

        vbox:

            # Prevent drinking potion if player at max HP
            if p.hp == p.maxHP:
                label "You are already at max HP."
                textbutton "Return" xalign 0.5 action Hide("drink_potion_screen")

            # Ask for confirmation before consuming
            else:
                spacing 40
                $pSize = p.sizes[selected_potion]
                $pPot = p.potency[selected_potion]
                label "Do you want to consume a [pSize] potion to regain [pPot] HP?"
                hbox:
                    xalign 0.5
                    spacing 120
                    textbutton "Yes" action [Function(p.consume, selected_potion), Hide("drink_potion_screen")]
                    textbutton "No" action Hide("drink_potion_screen")

screen inventory_screen:
    style_prefix "inventory"

    # Reset selected item for Item stats
    # $SetVariable("selected_item", None)

    # Background
    add "inventory background"

    hbox:

        spacing 20

        # Player stats and equipment #
        vbox:
            xmaximum 300
            spacing 10

            # Player stats
            frame:
                vbox:
                    label "Player stats" xalign 0.5
                    label "HP: [p.hp]/[p.maxHP]"
                    label "Attack: [p.dmg]"
                    label "Defense: [p.defense]"
                    label "Money: [p.money]"
                    label "Level: [p.lvl] ([p.xp])"

            # Player equipment
            # Weapon
            frame:
                style "slot"
                if p.equipment["weapon"]:
                    add p.equipment["weapon"].img xalign 0.5 yalign 0.5
                else:
                    label "weapon" xalign 0.5 yalign 0.5 text_size 24

            # Helmet
            frame:
                style "slot"
                if p.equipment["helmet"]:
                    add p.equipment["helmet"].img xalign 0.5 yalign 0.5
                else:
                    label "Helmet" xalign 0.5 yalign 0.5 text_size 24

            # Armor
            frame:
                style "slot"
                if p.equipment["armor"]:
                    add p.equipment["armor"].img xalign 0.5 yalign 0.5
                else:
                    label "Armor" xalign 0.5 yalign 0.5 text_size 24

            # Shield
            frame:
                style "slot"
                if p.equipment["shield"]:
                    add p.equipment["shield"].img xalign 0.5 yalign 0.5
                else:
                    label "shield" xalign 0.5 yalign 0.5 text_size 24

            # Consummable potions
            frame:
                vbox:
                    label "Potions" xalign 0.5
                    textbutton "Small: [p.potions[0]]" action [SetVariable("selected_potion", 0), Show("drink_potion_screen")]
                    textbutton "Medium: [p.potions[1]]" action [SetVariable("selected_potion", 1), Show("drink_potion_screen")]
                    textbutton "Large: [p.potions[2]]" action [SetVariable("selected_potion", 2), Show("drink_potion_screen")]

        # Inventory grid #
        grid 8 5:

            yalign 0.5
            spacing 10

            # Display inventory items
            for item, qty in p.inv.items():
                frame:
                    style "slot"
                    imagebutton idle item.img xalign 0.5 yalign 0.5 action SetVariable("selected_item", item)
                    label "[qty]" xalign 1. yalign 1.

            # Fill empty slots
            for _ in range(len(p.inv), 40):
                frame:
                    style "slot"

        # Item stats #
        vbox:

            spacing 20
            xmaximum 300

            label "Selected Item" xalign 0.5

            if selected_item:

                # Image
                frame:
                    style "slot" xalign 0.5
                    add selected_item.img xalign 0.5 yalign 0.5

                # Name
                label "Name: [selected_item.name]" xalign 0.5

                # Label item value
                label "Value: $[selected_item.value]" xalign 0.5

                # Equip/unequip
                if isinstance(selected_item, Equippable):

                    # Weapon dmg
                    if isinstance(selected_item, Weapon):
                        label "Attack: [selected_item.dmg]" xalign 0.5

                    # Armor defense
                    else:
                        label "Defense: [selected_item.defense]" xalign 0.5

                    if selected_item.isEquipped:
                        textbutton "Unequip" xalign 0.5 action Function(selected_item.unequip)
                    else:
                        textbutton "Equip" xalign 0.5 action Function(changeEquip, p, selected_item)

                # Sell (if shopping)
                if shopping:
                    textbutton "Sell" xalign 0.5 action [Function(p.sell, selected_item), SetVariable("selected_item", None)]

    # Return button to shop
    if shopping == True:
        textbutton "Leave":
            action [SetVariable("shopping", False), Hide("drink_potion_screen"), Hide("inventory_screen"), Call("goto_town")]
            xalign 0.3
            yalign 0.95

        textbutton "Shop":
            action [SetVariable("selected_item", None), Hide("drink_potion_screen"), Hide("inventory_screen"), Show("shop_screen")]
            xalign 0.7
            yalign 0.95

    # Return button to town
    else:
        textbutton "Return":
            action [Hide("drink_potion_screen"), Hide("inventory_screen"), Call("goto_town")]
            xalign 0.5
            yalign 0.95
