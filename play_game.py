from game import Game


class PlayGame:
    PLAYED_BY = []

    def __repr__(self):
        return f"Played by: {[player.name for player in PlayGame.PLAYED_BY]}"

    def winner(self):
        highest_score = 0
        winners = []
        for player in PlayGame.PLAYED_BY:
            score = player.result["correct"]
            if score > highest_score:
                highest_score = score
                winners = [player.name]
            elif score == highest_score:
                winners.append(player.name)

        if winners:
            print(f"The winner(s): {', '.join(winners)} with {highest_score} correct answers!")
        else:
            print("No players have played yet.")

    def add_player(self):
        add_player = int(input("How many players?: "))
        for _ in range(add_player):
            player_name = input("What's your name?: ")
            PlayGame.PLAYED_BY.append(Game(player_name))

    def play(self):
        self.add_player()
        for player in PlayGame.PLAYED_BY:
            player.play()
        self.winner()


# Example usage
if __name__ == '__main__':
    game_session = PlayGame()
    game_session.play()
