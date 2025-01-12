import os
import time

import pygame

# Initialize pygame mixer
pygame.init()
pygame.mixer.init()

# Load audio file
sound = pygame.mixer.Sound('audio.wav')

# Start the audio in paused state
sound.play()
pygame.mixer.pause()

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    """Pause the audio playback."""
    pygame.mixer.pause()

def play():
    """Unpause the audio and keep playing until interrupted."""
    pygame.mixer.unpause()
    while True:
        stop_playback = input("Press 2 anytime to pause playback and go back to the menu: ")
        if stop_playback == '2':
            pause()
            return  # Exit play() and return to the main menu
        else:
            continue

def main_menu():
    """Display the main menu and handle user input."""
    while True:
        clear_screen()
        print("\n🎵 MyPOD Music Player ")
        time.sleep(1)
        print("Press 1 to Play")
        print("Press 2 to Exit")
        print("Press anything else to see the menu again.")

        # Take user input
        user_input = input("\nEnter your choice: ")

        if user_input == '1':
            print("\nPlaying some proper tunes!")
            play()
        elif user_input == '2':
            print("\nExiting the player. Goodbye!")
            break
        else:
            print("\nInvalid choice. Returning to the menu...")
            time.sleep(1)

# Launch the main menu
main_menu()
