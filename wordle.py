"""
WORDLE GAME - Python Implementation
==================================

A clone of the popular word guessing game Wordle.
- Guess a 5-letter word in 6 tries
- Green: Correct letter in correct position
- Yellow: Correct letter in wrong position  
- Gray: Letter not in the word

How to play:
1. Enter a 5-letter word guess
2. Look at the color feedback
3. Use clues to make your next guess
4. Win by guessing the word in 6 tries or less!
"""

import random
import os
from typing import List, Tuple

class WordleGame:
    def __init__(self):
        # Common 5-letter words for the game
        self.word_list = [
            "ABOUT", "ABOVE", "ABUSE", "ACTOR", "ACUTE", "ADMIT", "ADOPT", "ADULT", "AFTER", "AGAIN",
            "AGENT", "AGREE", "AHEAD", "ALARM", "ALBUM", "ALERT", "ALIEN", "ALIGN", "ALIKE", "ALIVE",
            "ALLOW", "ALONE", "ALONG", "ALTER", "ANGEL", "ANGER", "ANGLE", "ANGRY", "APART", "APPLE",
            "APPLY", "ARENA", "ARGUE", "ARISE", "ARMED", "ARMOR", "ARRAY", "ARROW", "ASIDE", "ASSET",
            "AUDIO", "AUDIT", "AVOID", "AWAKE", "AWARD", "AWARE", "BADLY", "BAKER", "BASES", "BASIC",
            "BEACH", "BEGAN", "BEGIN", "BEING", "BELOW", "BENCH", "BILLY", "BIRTH", "BLACK", "BLAME",
            "BLANK", "BLAST", "BLIND", "BLOCK", "BLOOD", "BOARD", "BOAST", "BOATS", "BOBBY", "BONDS",
            "BONUS", "BOOST", "BOOTH", "BOUND", "BRAIN", "BRAND", "BRASS", "BRAVE", "BREAD", "BREAK",
            "BREED", "BRIEF", "BRING", "BROAD", "BROKE", "BROWN", "BUILD", "BUILT", "BUYER", "CABLE",
            "CALIF", "CARRY", "CATCH", "CAUSE", "CHAIN", "CHAIR", "CHAOS", "CHARM", "CHART", "CHASE",
            "CHEAP", "CHECK", "CHEST", "CHIEF", "CHILD", "CHINA", "CHOSE", "CIVIL", "CLAIM", "CLASS",
            "CLEAN", "CLEAR", "CLICK", "CLIMB", "CLOCK", "CLOSE", "CLOUD", "COACH", "COAST", "COULD",
            "COUNT", "COURT", "COVER", "CRAFT", "CRASH", "CRAZY", "CREAM", "CRIME", "CROSS", "CROWD",
            "CROWN", "CRUDE", "CURVE", "CYCLE", "DAILY", "DAMAGE", "DANCE", "DATED", "DEALT", "DEATH",
            "DEBUT", "DELAY", "DEPTH", "DOING", "DOUBT", "DOZEN", "DRAFT", "DRAMA", "DRANK", "DRAWN",
            "DREAM", "DRESS", "DRILL", "DRINK", "DRIVE", "DROVE", "DYING", "EAGER", "EARLY", "EARTH",
            "EIGHT", "ELITE", "EMPTY", "ENEMY", "ENJOY", "ENTER", "ENTRY", "EQUAL", "ERROR", "EVENT",
            "EVERY", "EXACT", "EXIST", "EXTRA", "FAITH", "FALSE", "FAULT", "FIBER", "FIELD", "FIFTH",
            "FIFTY", "FIGHT", "FINAL", "FIRST", "FIXED", "FLASH", "FLEET", "FLOOR", "FLUID", "FOCUS",
            "FORCE", "FORTH", "FORTY", "FORUM", "FOUND", "FRAME", "FRANK", "FRAUD", "FRESH", "FRONT",
            "FRUIT", "FULLY", "FUNNY", "GIANT", "GIVEN", "GLASS", "GLOBE", "GOING", "GRACE", "GRADE",
            "GRAND", "GRANT", "GRASS", "GRAVE", "GREAT", "GREEN", "GROSS", "GROUP", "GROWN", "GUARD",
            "GUESS", "GUEST", "GUIDE", "HAPPY", "HARRY", "HEART", "HEAVY", "HENCE", "HENRY", "HORSE",
            "HOTEL", "HOUSE", "HUMAN", "IDEAL", "IMAGE", "INDEX", "INNER", "INPUT", "ISSUE", "JAPAN",
            "JIMMY", "JOINT", "JONES", "JUDGE", "KNOWN", "LABEL", "LARGE", "LASER", "LATER", "LAUGH",
            "LAYER", "LEARN", "LEASE", "LEAST", "LEAVE", "LEGAL", "LEVEL", "LEWIS", "LIGHT", "LIMIT",
            "LINKS", "LIVES", "LOCAL", "LOOSE", "LOWER", "LUCKY", "LUNCH", "LYING", "MAGIC", "MAJOR",
            "MAKER", "MARCH", "MARIA", "MATCH", "MAYBE", "MAYOR", "MEANT", "MEDIA", "METAL", "MIGHT",
            "MINOR", "MINUS", "MIXED", "MODEL", "MONEY", "MONTH", "MORAL", "MOTOR", "MOUNT", "MOUSE",
            "MOUTH", "MOVED", "MOVIE", "MUSIC", "NEEDS", "NEVER", "NEWLY", "NIGHT", "NOISE", "NORTH",
            "NOTED", "NOVEL", "NURSE", "OCCUR", "OCEAN", "OFFER", "OFTEN", "ORDER", "OTHER", "OUGHT",
            "PAINT", "PANEL", "PAPER", "PARTY", "PEACE", "PETER", "PHASE", "PHONE", "PHOTO", "PIANO",
            "PIECE", "PILOT", "PITCH", "PLACE", "PLAIN", "PLANE", "PLANT", "PLATE", "POINT", "POUND",
            "POWER", "PRESS", "PRICE", "PRIDE", "PRIME", "PRINT", "PRIOR", "PRIZE", "PROOF", "PROUD",
            "PROVE", "QUEEN", "QUICK", "QUIET", "QUITE", "RADIO", "RAISE", "RANGE", "RAPID", "RATIO",
            "REACH", "READY", "REALM", "REBEL", "REFER", "RELAX", "REPAY", "REPLY", "RIGHT", "RIGID",
            "RIVAL", "RIVER", "ROBIN", "ROGER", "ROMAN", "ROUGH", "ROUND", "ROUTE", "ROYAL", "RURAL",
            "SCALE", "SCENE", "SCOPE", "SCORE", "SENSE", "SERVE", "SETUP", "SEVEN", "SHALL", "SHAPE",
            "SHARE", "SHARP", "SHEET", "SHELF", "SHELL", "SHIFT", "SHINE", "SHIRT", "SHOCK", "SHOOT",
            "SHORT", "SHOWN", "SIDES", "SIGHT", "SILLY", "SINCE", "SIXTH", "SIXTY", "SIZED", "SKILL",
            "SLEEP", "SLIDE", "SMALL", "SMART", "SMILE", "SMITH", "SMOKE", "SOLID", "SOLVE", "SORRY",
            "SOUND", "SOUTH", "SPACE", "SPARE", "SPEAK", "SPEED", "SPEND", "SPENT", "SPLIT", "SPOKE",
            "SPORT", "STAFF", "STAGE", "STAKE", "STAND", "START", "STATE", "STEAM", "STEEL", "STEEP",
            "STEER", "STICK", "STILL", "STOCK", "STONE", "STOOD", "STORE", "STORM", "STORY", "STRIP",
            "STUCK", "STUDY", "STUFF", "STYLE", "SUGAR", "SUITE", "SUPER", "SWEET", "TABLE", "TAKEN",
            "TASTE", "TAXES", "TEACH", "TEAMS", "TEETH", "TERRY", "TEXAS", "THANK", "THEFT", "THEIR",
            "THEME", "THERE", "THESE", "THICK", "THING", "THINK", "THIRD", "THOSE", "THREE", "THREW",
            "THROW", "THUMB", "THUS", "TIGHT", "TIMES", "TINY", "TITLE", "TODAY", "TOPIC", "TOTAL",
            "TOUCH", "TOUGH", "TOWER", "TRACK", "TRADE", "TRAIL", "TRAIN", "TREAT", "TREND", "TRIAL",
            "TRIBE", "TRICK", "TRIED", "TRIES", "TRIP", "TRUCK", "TRULY", "TRUNK", "TRUST", "TRUTH",
            "TWICE", "UNCLE", "UNDER", "UNDUE", "UNION", "UNITY", "UNTIL", "UPPER", "UPSET", "URBAN",
            "USAGE", "USUAL", "VALUE", "VIDEO", "VIRUS", "VISIT", "VITAL", "VOCAL", "VOICE", "WASTE",
            "WATCH", "WATER", "WHEEL", "WHERE", "WHICH", "WHILE", "WHITE", "WHOLE", "WHOSE", "WOMAN",
            "WOMEN", "WORLD", "WORRY", "WORSE", "WORST", "WORTH", "WOULD", "WRITE", "WRONG", "WROTE",
            "YOUNG", "YOUTH"
        ]
        
        # Valid words for guessing (includes target words plus common 5-letter words)
        self.valid_words = set(word.upper() for word in self.word_list)
        
        # Game state
        self.target_word = ""
        self.guesses = []
        self.max_guesses = 6
        self.game_over = False
        self.won = False
        
        # Color codes for terminal output
        self.colors = {
            'green': '\033[42m\033[30m',    # Green background, black text
            'yellow': '\033[43m\033[30m',   # Yellow background, black text  
            'gray': '\033[100m\033[37m',    # Gray background, white text
            'reset': '\033[0m',             # Reset color
            'bold': '\033[1m',              # Bold text
            'cyan': '\033[96m',             # Cyan text
        }

    def start_new_game(self):
        """Start a new Wordle game"""
        self.target_word = random.choice(self.word_list).upper()
        self.guesses = []
        self.game_over = False
        self.won = False
        print(f"\n{self.colors['bold']}{self.colors['cyan']}🎯 WORDLE GAME STARTED! 🎯{self.colors['reset']}")
        print("Guess the 5-letter word in 6 tries or less!")
        print("🟩 = Correct letter, correct position")
        print("🟨 = Correct letter, wrong position") 
        print("⬛ = Letter not in word")
        print("-" * 50)

    def is_valid_word(self, word: str) -> bool:
        """Check if the guessed word is valid"""
        return len(word) == 5 and word.upper() in self.valid_words

    def evaluate_guess(self, guess: str) -> List[Tuple[str, str]]:
        """
        Evaluate a guess and return color feedback
        Returns list of (letter, color) tuples
        """
        guess = guess.upper()
        target = self.target_word
        result = []
        
        # Track letter counts in target word
        target_counts = {}
        for letter in target:
            target_counts[letter] = target_counts.get(letter, 0) + 1
        
        # First pass: mark exact matches (green)
        guess_status = [''] * 5
        for i in range(5):
            if guess[i] == target[i]:
                guess_status[i] = 'green'
                target_counts[guess[i]] -= 1
        
        # Second pass: mark partial matches (yellow) and misses (gray)
        for i in range(5):
            if guess_status[i] == '':  # Not already marked as green
                if guess[i] in target_counts and target_counts[guess[i]] > 0:
                    guess_status[i] = 'yellow'
                    target_counts[guess[i]] -= 1
                else:
                    guess_status[i] = 'gray'
        
        # Create result with letters and colors
        for i in range(5):
            result.append((guess[i], guess_status[i]))
        
        return result

    def display_guess(self, guess_result: List[Tuple[str, str]]):
        """Display a guess with color formatting"""
        display_line = ""
        for letter, color in guess_result:
            display_line += f"{self.colors[color]} {letter} {self.colors['reset']}"
        print(display_line)

    def display_board(self):
        """Display the current game board"""
        print(f"\n{self.colors['bold']}WORDLE - Attempt {len(self.guesses)}/{self.max_guesses}{self.colors['reset']}")
        print("-" * 25)
        
        for guess_result in self.guesses:
            self.display_guess(guess_result)
        
        # Show empty rows
        for _ in range(self.max_guesses - len(self.guesses)):
            print("⬜ ⬜ ⬜ ⬜ ⬜")
        
        print("-" * 25)

    def make_guess(self, guess: str) -> bool:
        """
        Process a player's guess
        Returns True if guess was valid and processed
        """
        guess = guess.strip().upper()
        
        # Validate guess
        if len(guess) != 5:
            print("❌ Please enter exactly 5 letters!")
            return False
        
        if not guess.isalpha():
            print("❌ Please enter only letters!")
            return False
        
        if not self.is_valid_word(guess):
            print("❌ Not a valid 5-letter word!")
            return False
        
        # Process the guess
        guess_result = self.evaluate_guess(guess)
        self.guesses.append(guess_result)
        
        # Check if won
        if guess == self.target_word:
            self.won = True
            self.game_over = True
        
        # Check if out of guesses
        elif len(self.guesses) >= self.max_guesses:
            self.game_over = True
        
        return True

    def display_result(self):
        """Display the final game result"""
        self.display_board()
        
        if self.won:
            attempts = len(self.guesses)
            print(f"\n🎉 {self.colors['bold']}{self.colors['green']}CONGRATULATIONS!{self.colors['reset']} 🎉")
            print(f"You guessed '{self.target_word}' in {attempts} attempt{'s' if attempts != 1 else ''}!")
            
            # Score message based on attempts
            if attempts == 1:
                print("🏆 INCREDIBLE! Hole in one!")
            elif attempts <= 2:
                print("🌟 AMAZING! Fantastic guess!")
            elif attempts <= 4:
                print("👏 GREAT JOB! Well done!")
            else:
                print("✅ NICE WORK! You got it!")
        else:
            print(f"\n💔 {self.colors['bold']}GAME OVER!{self.colors['reset']} 💔")
            print(f"The word was: {self.colors['bold']}{self.target_word}{self.colors['reset']}")
            print("Better luck next time!")

    def get_alphabet_status(self) -> dict:
        """Get the status of each letter in the alphabet"""
        status = {}
        
        for guess_result in self.guesses:
            for letter, color in guess_result:
                if letter not in status:
                    status[letter] = color
                elif color == 'green':  # Green overrides yellow/gray
                    status[letter] = 'green'
                elif color == 'yellow' and status[letter] != 'green':  # Yellow overrides gray
                    status[letter] = 'yellow'
        
        return status

    def display_alphabet(self):
        """Display alphabet with color coding"""
        alphabet_status = self.get_alphabet_status()
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
        print(f"\n{self.colors['bold']}ALPHABET STATUS:{self.colors['reset']}")
        
        for i, letter in enumerate(alphabet):
            if letter in alphabet_status:
                color = alphabet_status[letter]
                print(f"{self.colors[color]} {letter} {self.colors['reset']}", end="")
            else:
                print(f" {letter} ", end="")
            
            # New line after every 13 letters
            if i == 12:
                print()
        
        print()  # Final newline

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    """Main game loop"""
    game = WordleGame()
    
    print("🎯 WELCOME TO WORDLE! 🎯")
    print("=" * 50)
    
    while True:
        # Start new game
        game.start_new_game()
        
        # Main game loop
        while not game.game_over:
            game.display_board()
            game.display_alphabet()
            
            # Get player guess
            guess = input(f"\n{game.colors['cyan']}Enter your guess (5 letters): {game.colors['reset']}").strip()
            
            # Handle special commands
            if guess.lower() in ['quit', 'exit', 'q']:
                print("Thanks for playing! 👋")
                return
            
            # Process the guess
            if game.make_guess(guess):
                clear_screen()
        
        # Display final result
        game.display_result()
        
        # Ask if player wants to play again
        while True:
            play_again = input(f"\n{game.colors['cyan']}Play again? (y/n): {game.colors['reset']}").strip().lower()
            if play_again in ['y', 'yes']:
                clear_screen()
                break
            elif play_again in ['n', 'no']:
                print("Thanks for playing Wordle! 👋")
                return
            else:
                print("Please enter 'y' for yes or 'n' for no.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nThanks for playing! 👋")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Please try running the game again.")