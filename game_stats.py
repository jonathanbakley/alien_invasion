class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start Alien Invasion in inactive state.
        self.game_active = False

        # High score which should not be reset
        # Get high score from file or set to 0
        try:
            with open("high_score.txt", "r+") as file_object:
                high_score = file_object.read()

            if not high_score:
                self.high_score = 0
            else:
                self.high_score = int(high_score)
        except FileNotFoundError:
            self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
