class Game:
    def __init__(self, players, num_turns=5):
        self.players = players
        self.num_turns = num_turns
        self.turn_data = []
        self.previous_choices = []

    def play(self):
        for turn in range(self.num_turns):
            print(f"Turn {turn+1}")
            public_bets = {}
            # Collect bets
            for player in self.players:
                bet_prompt = player.build_bet_prompt(self.previous_choices)
                bet_response = player.inference_engine.generate_response(bet_prompt)
                print(f"{player.name} Bet Response:\n{bet_response}\n")
                bet = player.parse_bet_response(bet_response)
                player.bet_history.append(bet)
                public_bets[player.name] = bet

            # Collect choices
            choices = {}
            for player in self.players:
                choice_prompt = player.build_choice_prompt(public_bets)
                choice_response = player.inference_engine.generate_response(choice_prompt)
                print(f"{player.name} Choice Response:\n{choice_response}\n")
                choice = player.parse_choice_response(choice_response)
                player.choice_history.append(choice)
                choices[player.name] = choice

            # Update previous choices
            self.previous_choices.extend(choices.values())

            # Calculate scores
            choice_counts = {}
            for choice in choices.values():
                choice_counts[choice] = choice_counts.get(choice, 0) + 1

            for player in self.players:
                # Score for choice
                player_choice = choices[player.name]
                num_same_choice = choice_counts[player_choice]
                choice_score = num_same_choice - 1

                # Score for bet
                player_bet = player.bet_history[-1]
                bet_count = choice_counts.get(player_bet, 0)
                bet_score = 0.5 * bet_count

                # Total score for the turn
                total_score = choice_score + bet_score
                player.total_score += total_score
                player.scores.append(total_score)

            # Save turn data
            turn_info = {
                'turn': turn + 1,
                'bets': public_bets.copy(),
                'choices': choices.copy(),
                'choice_counts': choice_counts.copy(),
            }
            self.turn_data.append(turn_info)