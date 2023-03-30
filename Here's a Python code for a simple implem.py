Here's a Python code for a simple implementation of the rock-paper-scissors game:
```python
import random

def roshambo(player_choice):
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    print('You chose:', player_choice)
    print('The computer chose:', computer_choice)

    if player_choice == computer_choice:
        return 'It\'s a tie!'
    elif player_choice == 'rock':
        if computer_choice == 'paper':
            return 'You lose!'
        else:
            return 'You win!'
    elif player_choice == 'paper':
        if computer_choice == 'scissors':
            return 'You lose!'
        else:
            return 'You win!'
    elif player_choice == 'scissors':
        if computer_choice == 'rock':
            return 'You lose!'
        else:
            return 'You win!'
    else:
        return 'Invalid choice!'

# Example usage:
print(roshambo('rock'))
print(roshambo('paper'))
print(roshambo('scissors'))
```