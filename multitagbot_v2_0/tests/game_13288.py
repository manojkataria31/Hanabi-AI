from enums import Color, Value
from testing.game_testing import GameSimulatorTesting
from multitagbot_v2_0.bot import Bot


class Game13288(GameSimulatorTesting):
    '''
    Turn 55 - B2 wasn't clued but deduced as a 2, removed the ability to play
    matching lowest playable value if not clued
    '''
    def test_turn_1(self):
        # Deck size 40, Bob, Clues 7, Score 0
        self.load_game(r'games\13288.json', position=1, turn=1, botcls=Bot)
        self.send_action()
        self.connection.assert_clue_value(0, Value.V1)

    def test_turn_3(self):
        # Deck size 39, Bob, Clues 6, Score 1
        self.load_game(r'games\13288.json', position=1, turn=3, botcls=Bot)
        self.send_action()
        self.connection.assert_card_discarded_hand(0)

    def test_turn_5(self):
        # Deck size 37, Bob, Clues 7, Score 2
        self.load_game(r'games\13288.json', position=1, turn=5, botcls=Bot)
        self.send_action()
        self.connection.assert_card_discarded_hand(0)

    def test_turn_7(self):
        # Deck size 36, Bob, Clues 7, Score 2
        self.load_game(r'games\13288.json', position=1, turn=7, botcls=Bot)
        self.send_action()
        self.connection.assert_clue_value(0, Value.V3)

    def test_turn_9(self):
        # Deck size 36, Bob, Clues 5, Score 2
        self.load_game(r'games\13288.json', position=1, turn=9, botcls=Bot)
        self.send_action()
        self.connection.assert_card_played_hand(1)

    def test_turn_11(self):
        # Deck size 35, Bob, Clues 4, Score 3
        self.load_game(r'games\13288.json', position=1, turn=11, botcls=Bot)
        self.send_action()
        self.connection.assert_card_played_hand(4)

    def test_turn_13(self):
        # Deck size 33, Bob, Clues 5, Score 3
        self.load_game(r'games\13288.json', position=1, turn=13, botcls=Bot)
        self.send_action()
        #self.connection.assert_card_played_hand(0)
        #self.connection.assert_clue_value(0, Value.V5)
        self.connection.assert_clue_color(0, Color.Green)

    def test_turn_15(self):
        # Deck size 31, Bob, Clues 6, Score 4
        self.load_game(r'games\13288.json', position=1, turn=15, botcls=Bot)
        self.send_action()
        self.connection.assert_clue_color(0, Color.Green)

    def test_turn_17(self):
        # Deck size 30, Bob, Clues 5, Score 5
        self.load_game(r'games\13288.json', position=1, turn=17, botcls=Bot)
        self.send_action()
        self.connection.assert_clue_value(0, Value.V1)

    def test_turn_19(self):
        # Deck size 29, Bob, Clues 4, Score 6
        self.load_game(r'games\13288.json', position=1, turn=19, botcls=Bot)
        self.send_action()
        self.connection.assert_card_discarded_hand(0)

    def test_turn_21(self):
        # Deck size 28, Bob, Clues 4, Score 6
        self.load_game(r'games\13288.json', position=1, turn=21, botcls=Bot)
        self.send_action()
        self.connection.assert_card_played_hand(0)

    def test_turn_23(self):
        # Deck size 27, Bob, Clues 3, Score 7
        self.load_game(r'games\13288.json', position=1, turn=23, botcls=Bot)
        self.send_action()
        self.connection.assert_card_played_hand(2)

    def test_turn_25(self):
        # Deck size 26, Bob, Clues 2, Score 8
        self.load_game(r'games\13288.json', position=1, turn=25, botcls=Bot)
        self.send_action()
        self.connection.assert_card_played_hand(4)

    def test_turn_27(self):
        # Deck size 25, Bob, Clues 1, Score 9
        self.load_game(r'games\13288.json', position=1, turn=27, botcls=Bot)
        self.send_action()
        self.connection.assert_card_played_hand(4)

    def test_turn_29(self):
        # Deck size 24, Bob, Clues 0, Score 10
        self.load_game(r'games\13288.json', position=1, turn=29, botcls=Bot)
        self.send_action()
        self.connection.assert_card_played_hand(0)

    def test_turn_31(self):
        # Deck size 22, Bob, Clues 0, Score 12
        self.load_game(r'games\13288.json', position=1, turn=31, botcls=Bot)
        self.send_action()
        self.connection.assert_card_played_hand(0)

    def test_turn_33(self):
        # Deck size 20, Bob, Clues 1, Score 13
        self.load_game(r'games\13288.json', position=1, turn=33, botcls=Bot)
        self.send_action()
        self.connection.assert_clue_value(0, Value.V4)

    def test_turn_35(self):
        # Deck size 19, Bob, Clues 1, Score 13
        self.load_game(r'games\13288.json', position=1, turn=35, botcls=Bot)
        self.send_action()
        self.connection.assert_card_played_hand(0)

    def test_turn_37(self):
        # Deck size 17, Bob, Clues 3, Score 14
        self.load_game(r'games\13288.json', position=1, turn=37, botcls=Bot)
        self.send_action()
        self.connection.assert_card_discarded_hand(0)

    def test_turn_39(self):
        # Deck size 15, Bob, Clues 5, Score 14
        self.load_game(r'games\13288.json', position=1, turn=39, botcls=Bot)
        self.send_action()
        self.connection.assert_clue_color(0, Color.Purple)

    def test_turn_41(self):
        # Deck size 14, Bob, Clues 4, Score 15
        self.load_game(r'games\13288.json', position=1, turn=41, botcls=Bot)
        self.send_action()
        self.connection.assert_card_discarded_hand(0)

    def test_turn_43(self):
        # Deck size 12, Bob, Clues 6, Score 15
        self.load_game(r'games\13288.json', position=1, turn=43, botcls=Bot)
        self.send_action()
        self.connection.assert_clue_color(0, Color.Yellow)

    def test_turn_45(self):
        # Deck size 11, Bob, Clues 6, Score 15
        self.load_game(r'games\13288.json', position=1, turn=45, botcls=Bot)
        self.send_action()
        self.connection.assert_clue_color(0, Color.Green)

    def test_turn_47(self):
        # Deck size 10, Bob, Clues 6, Score 16
        self.load_game(r'games\13288.json', position=1, turn=47, botcls=Bot)
        self.send_action()
        self.connection.assert_clue_value(0, Value.V3)

    def test_turn_49(self):
        # Deck size 10, Bob, Clues 4, Score 16
        self.load_game(r'games\13288.json', position=1, turn=49, botcls=Bot)
        self.send_action()
        self.connection.assert_card_discarded_hand(0)

    def test_turn_51(self):
        # Deck size 9, Bob, Clues 4, Score 16
        self.load_game(r'games\13288.json', position=1, turn=51, botcls=Bot)
        self.send_action()
        self.connection.assert_card_played_hand(4)

    def test_turn_53(self):
        # Deck size 8, Bob, Clues 4, Score 17
        self.load_game(r'games\13288.json', position=1, turn=53, botcls=Bot)
        self.send_action()
        self.connection.assert_card_discarded_hand(4)

    def test_turn_55(self):
        # Deck size 7, Bob, Clues 4, Score 17
        self.load_game(r'games\13288.json', position=1, turn=55, botcls=Bot)
        self.send_action()
        #self.connection.assert_card_played_hand(0)
        self.connection.assert_card_discarded_hand(2)

    def test_turn_57(self):
        # Deck size 6, Bob, Clues 3, Score 17
        self.load_game(r'games\13288.json', position=1, turn=57, botcls=Bot)
        self.send_action()
        self.connection.assert_card_discarded_hand(1)

    def test_turn_59(self):
        # Deck size 5, Bob, Clues 3, Score 17
        self.load_game(r'games\13288.json', position=1, turn=59, botcls=Bot)
        self.send_action()
        self.connection.assert_card_discarded_hand(4)

    def test_turn_61(self):
        # Deck size 3, Bob, Clues 5, Score 17
        self.load_game(r'games\13288.json', position=1, turn=61, botcls=Bot)
        self.send_action()
        self.connection.assert_clue_color(0, Color.Red)

    def test_turn_63(self):
        # Deck size 2, Bob, Clues 4, Score 18
        self.load_game(r'games\13288.json', position=1, turn=63, botcls=Bot)
        self.send_action()
        self.connection.assert_card_discarded_hand(0)

    def test_turn_65(self):
        # Deck size 0, Bob, Clues 5, Score 19
        self.load_game(r'games\13288.json', position=1, turn=65, botcls=Bot)
        self.send_action()
        self.connection.assert_card_played_hand(1)

