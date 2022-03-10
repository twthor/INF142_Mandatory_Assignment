from copyreg import pickle
from rich import print
from rich.prompt import Prompt
from rich.table import Table
import pickle

from champlistloader import load_some_champs
from core import Champion, Match, Shape, Team


def print_available_champs(champions: dict[Champion]) -> Table:

    # Create a table containing available champions
    available_champs = Table(title='Available champions')

    # Add the columns Name, probability of rock, probability of paper and
    # probability of scissors
    available_champs.add_column("Name", style="cyan", no_wrap=True)
    available_champs.add_column("prob(:raised_fist-emoji:)", justify="center")
    available_champs.add_column("prob(:raised_hand-emoji:)", justify="center")
    available_champs.add_column("prob(:victory_hand-emoji:)", justify="center")

    # Populate the table
    for champion in champions.values():
        available_champs.add_row(*champion.str_tuple)

    return available_champs


def input_champion(prompt: str,
                   color: str,
                   champions: dict[Champion],
                   player1: list[str],
                   player2: list[str]) -> None:

    # Prompt the player to choose a champion and provide the reason why
    # certain champion cannot be selected
    while True:
        match Prompt.ask(f'[{color}]{prompt}'):
            case name if name not in champions:
                return (f'The champion {name} is not available. Try again.')
            case name if name in player1:
                return (f'{name} is already in your team. Try again.')
            case name if name in player2:
                return(f'{name} is in the enemy team. Try again.')
            case _:
                player1.append(name)
                break

def valid_champion(userInput: str,
                   champions: dict[Champion],
                   player1: list[str],
                   player2: list[str]) -> None:

    # Prompt the player to choose a champion and provide the reason why
    # certain champion cannot be selected. Returns userinput if champion is valid.
    while True:
        if userInput not in champions:
            return (f'The champion {userInput} is not available. Try again.')
        if userInput in player1:
            return (f'{userInput} is already in your team. Try again.')
        if userInput in player2:
            return(f'{userInput} is in the enemy team. Try again.')
        else:
            return userInput

def print_match_summary(match: Match) -> None:

    EMOJI = {
        Shape.ROCK: ':raised_fist-emoji:',
        Shape.PAPER: ':raised_hand-emoji:',
        Shape.SCISSORS: ':victory_hand-emoji:'
    }

    list = []
    # For each round print a table with the results
    for index, round in enumerate(match.rounds):

        # Create a table containing the results of the round
        round_summary = Table(title=f'Round {index+1}')

        # Add columns for each team
        round_summary.add_column("Red",
                                 style="red",
                                 no_wrap=True)
        round_summary.add_column("Blue",
                                 style="blue",
                                 no_wrap=True)

        # Populate the table
        for key in round:
            red, blue = key.split(', ')
            round_summary.add_row(f'{red} {EMOJI[round[key].red]}',
                                  f'{blue} {EMOJI[round[key].blue]}')
        
        list.append(round_summary)
        # return round_summary
    # Print the score
    red_score, blue_score = match.score
    print(f'Red: {red_score}\n'
          f'Blue: {blue_score}')
    list.append(red_score)
    list.append(blue_score)
    list.append(team_score(red_score, blue_score))
    print(list)
    return list

def team_score(red_score, blue_score):
    # Print the winner
    if red_score > blue_score:
        return('\n[red]Red victory! :grin:')
    elif red_score < blue_score:
        return('\n[blue]Blue victory! :grin:')
    else:
        return('\nDraw :expressionless:')


def welcomeMessage():
    return('\n'
          'Welcome to [bold yellow]Team Local Tactics[/bold yellow]!'
          '\n'
          'Each player choose a champion each time.'
          '\n')

def match(player1, player2):
    champions = load_some_champs()
    match = Match(
        Team([champions[name] for name in player1]),
        Team([champions[name] for name in player2])
    )
    match.play()
    return print_match_summary(match)


def main() -> None:

    print('\n'
          'Welcome to [bold yellow]Team Local Tactics[/bold yellow]!'
          '\n'
          'Each player choose a champion each time.'
          '\n')

    champions = load_some_champs()
    print_available_champs(champions)
    print('\n')

    player1 = []
    player2 = []

    # Champion selection
    for _ in range(2):
        input_champion('Player 1', 'red', champions, player1, player2)
        input_champion('Player 2', 'blue', champions, player2, player1)

    print('\n')

    # Match
    match = Match(
        Team([champions[name] for name in player1]),
        Team([champions[name] for name in player2])
    )
    match.play()

    # Print a summary
    print_match_summary(match)


if __name__ == '__main__':
    main()