init python:

    class Enemy:

        def __init__(self, img, name, hp, dmg, defense, loot_table, reward, xp):
            '''Initiate the enemy class instance.
            img: sprite of enemy
            name: name to be displayed
            hp : current hp
            dmg: attack damage
            defense: defense value
            loot_table: the loot table with items and probabilities of drops
            reward: money reward for defeating enemy
            xp: xp reward for defeating enemy'''
            self.img = img
            self.name = name
            self.hp = hp
            self.dmg = dmg
            self.defense = defense
            self.loot_table = loot_table
            self.reward = reward
            self.xp = xp

        def atk(self):
            '''Get a random attack damage value depending on a random attack style.'''
            out = []        # output var [style, dmg]
            global styles

            # Get random attack style
            this_style = renpy.random.randint(0, 2)
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
            '''Deduct from the enemy's hp the amount of damage of the attack minus the enemy's defense.'''
            trueDmg = amount - self.defense
            if trueDmg > 0:
                self.hp -= trueDmg
            else:
                return 0

            return trueDmg

        def isDead(self):
            '''Return True if enemy is dead.'''
            if self.hp <= 0:
                return True
            else:
                return False
