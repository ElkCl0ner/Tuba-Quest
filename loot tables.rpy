init 2 python:

    # format: ((placeholder), (<amount>, <item>), (), ...) : <weight>

    # Test loot table
    lt_test = {
    ((0, None), (1, diamond_sword)) : 3,
    ((0, None), (2, diamond_helmet)) : 2,
    ((0, None), (3, diamond_armor)) : 1,
    ((0, None), (4, shield)) : 4
    }

    # Prologue
    lt_0 = {
    ((0, None), (1, sennheiser_mouthpiece)) : 250,
    ((0, None), (1, sennheiser_bell)) : 250,
    ((0, None), (1, sennheiser_tube)) : 250,
    ((0, None), (1, sennheiser_valve)) : 250,
    ((0, None), (1, diamond_sword)) : 1
    }

    # Act 1
    lt_1 = {
    ((0, None), (1, sennheiser_mouthpiece)) : 7,
    ((0, None), (1, sennheiser_bell)) : 7,
    ((0, None), (1, sennheiser_tube)) : 7,
    ((0, None), (1, sennheiser_valve)) : 7,
    ((0, None), (1, steinway_mouthpiece)) : 15,
    ((0, None), (1, steinway_bell)) : 15,
    ((0, None), (1, steinway_tube)) : 15,
    ((0, None), (1, steinway_valve)) : 15
    }

    # Act 1 boss
    lt_1_boss = {
    ((0, None), (1, steinway_mouthpiece)) : 15,
    ((0, None), (1, steinway_bell)) : 15,
    ((0, None), (1, steinway_tube)) : 15,
    ((0, None), (1, steinway_valve)) : 15,
    ((0, None), (1, fender_mouthpiece)) : 10,
    ((0, None), (1, fender_bell)) : 10,
    ((0, None), (1, fender_tube)) : 10,
    ((0, None), (1, fender_valve)) : 10
    }

    # Act 2
    lt_2 = {
    ((0, None), (1, steinway_mouthpiece)) : 7,
    ((0, None), (1, steinway_bell)) : 7,
    ((0, None), (1, steinway_tube)) : 7,
    ((0, None), (1, steinway_valve)) : 7,
    ((0, None), (1, fender_mouthpiece)) : 15,
    ((0, None), (1, fender_bell)) : 15,
    ((0, None), (1, fender_tube)) : 15,
    ((0, None), (1, fender_valve)) : 15
    }

    # Act 2 boss
    lt_2_boss = {
    ((0, None), (1, fender_mouthpiece)) : 15,
    ((0, None), (1, fender_bell)) : 15,
    ((0, None), (1, fender_tube)) : 15,
    ((0, None), (1, fender_valve)) : 15,
    ((0, None), (1, yamaha_mouthpiece)) : 10,
    ((0, None), (1, yamaha_bell)) : 10,
    ((0, None), (1, yamaha_tube)) : 10,
    ((0, None), (1, yamaha_valve)) : 10
    }

    # Act 3
    lt_3 = {
    ((0, None), (1, fender_mouthpiece)) : 7,
    ((0, None), (1, fender_bell)) : 7,
    ((0, None), (1, fender_tube)) : 7,
    ((0, None), (1, fender_valve)) : 7,
    ((0, None), (1, yamaha_mouthpiece)) : 15,
    ((0, None), (1, yamaha_bell)) : 15,
    ((0, None), (1, yamaha_tube)) : 15,
    ((0, None), (1, yamaha_valve)) : 15
    }

    # Act 3 boss
    lt_3_boss = {
    ((0, None), (1, yamaha_mouthpiece)) : 15,
    ((0, None), (1, yamaha_bell)) : 15,
    ((0, None), (1, yamaha_tube)) : 15,
    ((0, None), (1, yamaha_valve)) : 15,
    ((0, None), (1, shure_mouthpiece)) : 10,
    ((0, None), (1, shure_bell)) : 10,
    ((0, None), (1, shure_tube)) : 10,
    ((0, None), (1, shure_valve)) : 10
    }

    # Act 4
    lt_4 = {
    ((0, None), (1, yamaha_mouthpiece)) : 5,
    ((0, None), (1, yamaha_bell)) : 5,
    ((0, None), (1, yamaha_tube)) : 5,
    ((0, None), (1, yamaha_valve)) : 5,
    ((0, None), (1, shure_mouthpiece)) : 20,
    ((0, None), (1, shure_bell)) : 20,
    ((0, None), (1, shure_tube)) : 20,
    ((0, None), (1, shure_valve)) : 20
    }

    # Act 4 boss (King)
    lt_4_boss = {
    ((0, None), (1, shure_mouthpiece)) : 15,
    ((0, None), (1, shure_bell)) : 15,
    ((0, None), (1, shure_tube)) : 15,
    ((0, None), (1, shure_valve)) : 15,
    ((0, None), (1, divine_mouthpiece)) : 10,
    ((0, None), (1, divine_bell)) : 10,
    ((0, None), (1, divine_tube)) : 10,
    ((0, None), (1, divine_valve)) : 10
    }
