from comp_tom_bench.engine import OllamaInferenceEngine, LMStudioInferenceEngine
from comp_tom_bench.player import Player
from comp_tom_bench.game import Game

# Declare constants
PROMPT_TYPE = 'nocot'

def main():
    # Initialize inference engines
    lmstudio_model_name = 'lmstudio-community/Phi-3.5-mini-instruct-GGUF/Phi-3.5-mini-instruct-Q8_0.gguf'  # Ensure this matches the model name in LMStudio
    lmstudio_engine = LMStudioInferenceEngine(lmstudio_model_name)

    ollama_model_name = 'mistral-nemo:12b'  # Ensure this matches the model name in Ollama
    ollama_engine = OllamaInferenceEngine(ollama_model_name)

    #openai_api_key = ''  # Replace with your actual API key
    #openai_engine = OpenAIInferenceEngine(openai_api_key)

    # Create players
    players = []
    # First 8 players use Ollama
    for i in range(8):
        player_name = f"Player_{i+1}"
        prompt_type = PROMPT_TYPE
        player = Player(player_name, ollama_engine, prompt_type)
        players.append(player)

    # Next 8 players use OpenAI
    for i in range(8, 16):
        player_name = f"Player_{i+1}"
        prompt_type = PROMPT_TYPE
        player = Player(player_name, lmstudio_engine, prompt_type)
        players.append(player)

    # Initialize and play the game
    game = Game(players)
    game.play()

    # Save outputs in a structured format
    game_data = {
        'players': [player.name for player in players],
        'turns': game.turn_data,
        'scores': {player.name: player.scores for player in players},
        'total_scores': {player.name: player.total_score for player in players},
    }

    # Save to JSON file
    import json
    with open('game_data.json', 'w') as f:
        json.dump(game_data, f, indent=4)

    # Print final scores
    print("\nFinal Scores:")
    for player in players:
        print(f"{player.name}: {player.total_score}")

if __name__ == '__main__':
    main()
