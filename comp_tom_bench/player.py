import re
import random

class Player:
    def __init__(self, name, inference_engine, prompt_type='cot'):
        self.name = name
        self.inference_engine = inference_engine
        self.prompt_type = prompt_type  # 'cot' or 'nocot'
        self.total_score = 0
        self.bet_history = []
        self.choice_history = []
        self.scores = []

    def build_bet_prompt(self, previous_choices):
        previous_choices_str = ', '.join(map(str, previous_choices)) if previous_choices else 'None'
        if self.prompt_type == 'cot':
            prompt = f"""You are playing a game with the following rules:
- There are 16 possible numbers (0 to 15).
- Each player publicly bets on a number they think will be most chosen.
- Before betting, you can see the previous choices made by all players in past turns.

Previous choices: {previous_choices_str}

Think about which number you want to bet on.

Provide your bet as a single number without any brackets or additional text, in the following format:

Bet: number

Provide a brief reasoning for your decision."""
        else:
            prompt = f"""You are playing a game. Choose a bet from numbers 0 to 15.

Previous choices: {previous_choices_str}

Provide your bet as a single number without any brackets or additional text, in the following format:

Bet: number
"""
        return prompt

    def parse_bet_response(self, response):
        lines = response.strip().split('\n')
        bet = None
        for line in lines:
            if 'bet' in line.lower():
                bet_match = re.search(r'\d+', line)
                if bet_match:
                    bet = int(bet_match.group())
                    break
        if bet is None:
            bet = random.randint(0, 15)
            print(f"Warning: Could not parse bet from response. Defaulting to {bet}. Response was:\n{response}")
        return bet

    def build_choice_prompt(self, public_bets):
        public_bets_str = ', '.join(f"{k}: {v}" for k, v in public_bets.items())
        if self.prompt_type == 'cot':
            prompt = f"""You are playing a game with the following rules:
- There are 16 possible numbers (0 to 15).
- Each player has publicly bet on a number.
- Now, you privately choose a number.

Given the following public bets from other players: {public_bets_str}

Think about which number you want to choose.

Provide your choice as a single number without any brackets or additional text, in the following format:

Choice: number

Provide a brief reasoning for your decision."""
        else:
            prompt = f"""You are playing a game. Choose a number from 0 to 15.

Given the following public bets from other players: {public_bets_str}

Provide your choice as a single number without any brackets or additional text, in the following format:

Choice: number
"""
        return prompt

    def parse_choice_response(self, response):
        lines = response.strip().split('\n')
        choice = None
        for line in lines:
            if 'choice' in line.lower() or 'choose' in line.lower():
                choice_match = re.search(r'\d+', line)
                if choice_match:
                    choice = int(choice_match.group())
                    break
        if choice is None:
            choice = random.randint(0, 15)
            print(f"Warning: Could not parse choice from response. Defaulting to {choice}. Response was:\n{response}")
        return choice