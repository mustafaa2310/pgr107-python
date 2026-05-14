import os
import random

class WordGuessGame:
    def __init__(self, word_file):
        self.word_file = word_file
        self.word = self.get_random_word()
        self.guessed_letters = set()
        self.wrong_guesses = 0
        self.max_wrong = len(self.word)

    def get_random_word(self):
        with open(self.word_file, "r") as file:
            words = file.readlines()
        words = [word.strip() for word in words]
        return random.choice(words)

    def display_word(self):
        return ' '.join([letter if letter in self.guessed_letters else '_' for letter in self.word])

    def play(self):
        print("Welcome to the Word Guessing Game!")
        print(self.display_word())

        while self.wrong_guesses < self.max_wrong:
            guess = input("Guess a letter: ").lower()

            if guess in self.guessed_letters:
                print("You already guessed that letter.")
                continue

            self.guessed_letters.add(guess)

            if guess in self.word:
                print("Correct!")
            else:
                self.wrong_guesses += 1
                print(f"Wrong! You have {self.max_wrong - self.wrong_guesses} tries left.")

            print(self.display_word())

            if all(letter in self.guessed_letters for letter in self.word):
                print("Congratulations! You guessed the word!")
                return

        print(f"Game over. The word was: {self.word}")

if __name__ == "__main__":
   base_dir = os.path.dirname(os.path.abspath(__file__))
word_file = os.path.join(base_dir, "words.txt")

game = WordGuessGame(word_file)
game.play()
