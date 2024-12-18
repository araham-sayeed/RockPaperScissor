import tkinter as tk
import random

# Initialize the Tkinter window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x400")

# Variables to track scores
player_count = 0
computer_count = 0

# Labels to display the score
score_label = tk.Label(root, text=f"Your Score: {player_count} | Computer Score: {computer_count}", font=("Helvetica", 14))
score_label.pack(pady=20)

# Label to show the choices
choice_label = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Helvetica", 12))
choice_label.pack(pady=10)

# Function to handle player's choice and update the score
def play_game(player_choice):
    global player_count, computer_count
    
    l1 = [1, 2, 3]
    computer_choice = random.choice(l1)

    # Display the player's and computer's choices
    player_choice_text = ["Rock", "Scissors", "Paper"]
    computer_choice_text = player_choice_text[computer_choice - 1]

    # Update the label with choices
    choice_label.config(text=f"You chose: {player_choice_text[player_choice - 1]} | Computer chose: {computer_choice_text}")

    # Check the outcome
    if player_choice == computer_choice:
        result = "Draw ---> 0 points"
    elif (player_choice == 1 and computer_choice == 2) or (player_choice == 2 and computer_choice == 3) or (player_choice == 3 and computer_choice == 1):
        result = "1 point for you"
        player_count += 1
    else:
        result = "1 point for computer"
        computer_count += 1

    # Update score and result message
    score_label.config(text=f"Your Score: {player_count} | Computer Score: {computer_count}")
    result_label.config(text=result)

    # Check if anyone has won
    if player_count == 10:
        result_label.config(text="!!!!!!Congratulations, you won!!!!!!")
        disable_buttons()
    elif computer_count == 10:
        result_label.config(text="Try better next time.")
        disable_buttons()

# Function to disable buttons when someone wins
def disable_buttons():
    rock_button.config(state="disabled")
    paper_button.config(state="disabled")
    scissors_button.config(state="disabled")

# Buttons for player to choose Rock, Paper, or Scissors
rock_button = tk.Button(root, text="Rock", width=10, height=2, command=lambda: play_game(1))
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", width=10, height=2, command=lambda: play_game(3))
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", width=10, height=2, command=lambda: play_game(2))
scissors_button.pack(pady=5)

# Label to display the result of each round
result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=20)

# Start the Tkinter main loop
root.mainloop()
