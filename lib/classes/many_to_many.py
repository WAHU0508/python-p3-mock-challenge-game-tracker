class Game:
    def __init__(self, title):
        self.title = title
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise TypeError("The title should be of str type.")
        if not len(value) > 0:
            raise ValueError("The title should have more than 0 characters.")
        if hasattr(self, '_title'):
            raise AttributeError("The game title cannot be changed.")
        self._title = value

    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        return list({result.player for result in self.results()})

    def average_score(self, player):
        total_score = sum(result.score for result in self.results())
        return total_score / len(self.results())

class Player:
    all = []
    def __init__(self, username):
        self.username = username
        Player.all.append(self)
    @property
    def username(self):
        return self._username
    @username.setter
    def username(self, value):
        if not isinstance(value, str):
            raise TypeError("The player username should be of str type.")
        if not 2 <= len(value) <= 16:
            raise ValueError("The username should have characters between 2 and 16.")
        self._username = value
    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        return list({result.game for result in self.results()})

    def played_game(self, game):
        if game in self.games_played():
            return True
        else:
            return False

    def num_times_played(self, game):
        games = list(result.game for result in self.results())
        return games.count(game)
    @classmethod
    def highest_scored(cls, game):
        players_scores = [(player, game.average_score(player)) for player in cls.all if player in game.players()]
        if not players_scores:
            return None
        highest_scoring_player = max(players_scores, key=lambda x : x[1])
        return highest_scoring_player[0]
class Result:
    all = []
    def __init__(self, player, game, score):
        if not isinstance(player, Player):
            raise TypeError("player must be an instance of Player class.")
        if not isinstance(game, Game):
            raise TypeError("game must be an instance of Game class.")
        self._player = player
        self._game = game
        self.score = score
        """Keep track of all inatances of result"""
        Result.all.append(self)
    @property
    def player(self):
        return self._player
    @property
    def game(self):
        return self._game
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
           raise TypeError("The score must be an integer.")
        if not 1 <= value <= 5000:
            print("The score must be between 1 and 5000.")
        if hasattr(self, '_score'):
            raise AttributeError("The score cannot be changed.")
        self._score = value

game = Game("Skribbl.io")
player_1 = Player('Saaammmm')
player_2 = Player('ActuallyTopher')
Result(player_1, game, 2000)
Result(player_1, game, 1)
Result(player_2, game, 1900)
Result(player_2, game, 10)
print(Player.highest_scored(game))