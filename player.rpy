init python:

    class Player:
        def __init__(self, hp = 50, maxHP = 50, dmg = 10, defense = 0, money = 0, xp = 0):
            '''Initiate the player instance. Set player stats, inventory and equipment.'''

            self.hp = hp
            self.maxHP = maxHP
            self.dmg = dmg
            self.defense = defense
            self.money = money
            self.xp = xp
            self.lvl = int(-3 + (self.xp + 9) ** (0.5))
            self.equipment = {
            "weapon" : None,
            "helmet" : None,
            "armor" : None,
            "shield" : None
            }
            self.potions = [0, 0, 0]
            self.potency = [30, 100, 250]
            self.sizes = ["small", "medium", "large"]
            self.inv = {}

        def give(self, item):
            '''Store a given item to the player's inventory.'''

            # Item already owned
            if item in self.inv:
                self.inv[item] += 1

            # New item in inventory
            else:
                self.inv[item] = 1

        def remove(self, item):
            '''Remove a given item from the player's inventory.'''

            # Check item is indeed in the player's inventory
            if item in self.inv:

                # Only 1 of the item
                if self.inv[item] <= 1:
                    item.unequip()          # unequip item
                    self.inv.pop(item)

                # Multiple copies of the item
                else:
                    self.inv[item] -= 1

        def buy(self, item):
            '''Allows the player to buy an item from a shop.'''

            # Check if player has enough money
            if self.money >= item.value:
                self.give(item)
                self.money -= item.value

        def buyPotion(self, potion):
            '''Allows the player to buy potions.'''

            # Check if player has enough money
            if self.money >= potionPrices[potion]:
                self.potions[potion] += 1
                self.money -= potionPrices[potion]

        def sell(self, item):
            '''Allows the player to sell an item at a shop.'''

            self.remove(item)
            self.money += int(0.5 * item.value)       # Sell at 50% of value

        def heal(self, amount):
            '''Heals the player by a certain amount without going past maxHP.'''

            self.hp += amount

            # Check if hp > maxHP
            if self.hp > self.maxHP:
                self.hp = self.maxHP

        def consume(self, potion):
            '''Allows the player to consume a potion and gain HP.'''

            # Dont allow the player to consume potions at max hp
            if self.hp == self.maxHP:
                return

            if self.potions[potion] > 0:
                self.heal(self.potency[potion])
                self.potions[potion] -= 1

        def levelUp(self):
            '''Check if the player levels up and boost player's stats if level up.'''

            # Calculate level considering player xp
            level = int(-3 + (self.xp + 9) ** (0.5))

            # Check for level up
            if self.lvl < level:
                self.lvl += 1
                self.maxHP += 20
                self.hp = self.maxHP
                return True

            return False

        def giveXP(self, amount):
            '''Give a certain amount of xp to the player and check if the player levels up.'''

            self.xp += amount
            return self.levelUp()

        def atk(self, this_style):
            '''Return an attack damage value depending on player's dmg and an attack style.'''
            out = []        # output var [style, dmg]
            global styles

            # Get attack style
            out.append(styles[this_style])

            # Get random attack dmg depending on style
            # Light attack (90, 85-95%)
            if this_style == 0:
                lo = int(.85 * self.dmg)
                hi = int(.95 * self.dmg)

            # Normal attack (100, 75-125%)
            elif this_style == 1:
                lo = int(.75 * self.dmg)
                hi = int(1.25 * self.dmg)

            # Heavy attack (95, 30-160%)
            else:
                lo = int(.3 * self.dmg)
                hi = int(1.6 * self.dmg)

            out.append(renpy.random.randint(lo, hi))

            return out

        def takeDmg(self, amount):
            '''Deduct from the player's hp the amount of damage of the attack minus the player's defense.'''
            trueDmg = amount - self.defense
            if trueDmg > 0:
                self.hp -= trueDmg
            else:
                return 0

            return trueDmg

        def isDead(self):
            '''Return True if player is dead.'''
            if self.hp <= 0:
                return True
            else:
                return False
