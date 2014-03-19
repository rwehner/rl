import unittest
import os
import glob

import highscore

class testHighscoreNewPlayers(unittest.TestCase):
    def setUp(self):
        highscore.fn = 'v:\workspace\Python2_Homework04\src\scoreboard_fixture.shlf'
        self.fixture_player = 'Mario'
        self.fixture_score_high = 300
        
    def tearDown(self):
        fixture_files = glob.glob(highscore.fn + '*')
        for fn in fixture_files:
            os.remove(fn)
        
    def test_new_user_returns_score(self):
        """If the user does not exist, their current score should be returned"""
        observed = highscore.highscore(self.fixture_player, self.fixture_score_high)
        self.assertEquals(observed, self.fixture_score_high)
        
        
class testHighscoreExistingPlayers(unittest.TestCase):        
    def setUp(self):
        highscore.fn = 'v:\workspace\Python2_Homework04\src\scoreboard_fixture.shlf'
        self.fixture_player1 = 'Mario'
        self.fixture_score_high1 = 300
        self.fixture_score_low1 = highscore.highscore(self.fixture_player1, self.fixture_score_high1)
        self.fixture_player2 = 'Luigi'
        self.fixture_score_high2 = 100
        self.fixture_score_low2 = highscore.highscore(self.fixture_player2, self.fixture_score_high2)
        
    def tearDown(self):
        fixture_files = glob.glob(highscore.fn + '*')
        for fn in fixture_files:
            os.remove(fn)
    
    def test_existing_player_returns_stored_score(self):
        """when the current score is lower, the stored score should be returned"""
        self.fixture_score_low1 = self.fixture_score_high1 - 10    
        observed = highscore.highscore(self.fixture_player1, self.fixture_score_low1)
        self.assertEquals(observed, self.fixture_score_high1)
        
    def test_always_return_higest_score(self):
        for num in range(100, 400, 100):
            self.fixture_score_high1 += num 
            observed = highscore.highscore(self.fixture_player1, self.fixture_score_high1)
            self.assertEquals(observed, self.fixture_score_high1)
        
    def test_multiple_players_return_own_results(self):
        """Each play should return only it's results"""
        observed = highscore.highscore(self.fixture_player1, self.fixture_score_high1)
        self.assertAlmostEquals(observed, self.fixture_score_high1)
        observed = highscore.highscore(self.fixture_player2, self.fixture_score_high2)
        self.assertAlmostEquals(observed, self.fixture_score_high2)

    def test_existing_player_with_new_high_score(self):    
        self.fixture_score_high1 += 10
        observed = highscore.highscore(self.fixture_player1, self.fixture_score_high1)
        self.assertEquals(observed, self.fixture_score_high1)
        
if __name__ == "__main__":
    unittest.main()
        