"""Rules for one independent Rock, Paper, Scissors round."""


def determine_winner(player: str, computer: str) -> str:
    """Return 'win', 'lose', or 'tie' for two valid lowercase moves."""
    if player == computer:
        return "tie"
    winning_pairs = {("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")}
    if (player, computer) in winning_pairs:
        return "win"
    return "lose"
