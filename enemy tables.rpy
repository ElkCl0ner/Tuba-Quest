init 3 python:

    # format: ((img, name, hp, dmg, defense, loot_table, reward, xp), (), ...)

    et_test = (
    ("zombie", "Zombie", 100, 20, 5, lt_test, 10, 7),
    ("skeleton", "Skeleton", 120, 25, 3, lt_test, 13, 9)
    )

    et_1 = (
    ("guard", "Tuba Guard", 105, 15, 15, lt_1, 20, 7),
    ("gunner", "Tuba Gunner", 75, 10, 8, lt_1, 10, 4),
    ("bandit", "Tuba Bandit", 60, 15, 5, lt_1, 8, 2),
    ("apprentice", "Tuba Apprentice", 50, 18, 2, lt_1, 11, 3)
    )

    et_2 = (
    ("guard", "Tuba Guard", 210, 45, 70, lt_2, 50, 12),
    ("gunner", "Tuba Gunner", 120, 35, 65, lt_2, 35, 9),
    ("bandit", "Tuba Bandit", 100, 30, 45, lt_2, 30, 7),
    ("apprentice", "Tuba Apprentice", 90, 45, 40, lt_2, 40, 8)
    )

    et_3 = (
    ("guard", "Tuba Guard", 320, 90, 150, lt_3, 100, 23),
    ("gunner", "Tuba Gunner", 210, 65, 110, lt_3, 70, 18),
    ("bandit", "Tuba Bandit", 190, 60, 100, lt_3, 50, 14),
    ("apprentice", "Tuba Apprentice", 170, 75, 90, lt_3, 80, 15)
    )

    et_4 = (
    ("guard", "Tuba Guard", 520, 150, 300, lt_4, 175, 40),
    ("gunner", "Tuba Gunner", 410, 120, 275, lt_4, 100, 25),
    ("apprentice", "Tuba Apprentice", 380, 130, 190, lt_4, 120, 17)
    )
