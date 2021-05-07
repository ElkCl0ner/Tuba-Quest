init python:

    class InventoryItem:
        def __init__(self, img, name, value):
            self.img = img
            self.name = name
            self.value = value

    class QuestItem(InventoryItem):
        def __init__(self, img, name):
            InventoryItem.__init__(self, img, name, value = 0)

    class Equippable(InventoryItem):
        def __init__(self, img, name, value, slot):
            InventoryItem.__init__(self, img, name, value)
            self.slot = slot
            self.isEquipped = False

        def equip(self):
            # Item already equipped
            if self.isEquipped:
                return

            # Equip weapoon
            if self.slot == "weapon":
                p.dmg += self.dmg

            # Equip wearable
            else:
                p.defense += self.defense

            # Update self.isEquipped
            self.isEquipped = True

            # Update Player.equipment
            p.equipment[selected_item.slot] = selected_item

        def unequip(self):
            # Item not equipped
            if not self.isEquipped:
                return

            # Unequip weapon
            if self.slot == "weapon":
                p.dmg -= self.dmg

            # Unequip wearable
            else:
                p.defense -= self.defense

            # Update self.isEquipped
            self.isEquipped = False

            # Update Player.equipment
            p.equipment[selected_item.slot] = None

    class Weapon(Equippable):
        def __init__(self, img, name, value, dmg):
            Equippable.__init__(self, img, name, value, slot = "weapon")
            self.dmg = dmg

    class Helmet(Equippable):
        def __init__(self, img, name, value, defense):
            Equippable.__init__(self, img, name, value, slot = "helmet")
            self.defense = defense

    class Armor(Equippable):
        def __init__(self, img, name, value, defense):
            Equippable.__init__(self, img, name, value, slot = "armor")
            self.defense = defense

    class Shield(Equippable):
        def __init__(self, img, name, value, defense):
            Equippable.__init__(self, img, name, value, slot = "shield")
            self.defense = defense

    def changeEquip(p, equipment):
        '''Make sure that the player unequips their currently equipped item before equipping a new one.'''

        slot = equipment.slot

        # Unequip
        if p.equipment[slot]:
            p.equipment[slot].unequip()

        # Equip
        equipment.equip()
