# Hangman

Welcome to the Hangman game implemented in Python! This Hangman game allows players to guess the name of a movie from three different genres: Action, Horror, and Comedy. The player has a limited number of guesses to figure out the movie title, with each incorrect guess resulting in a progression of the hangman drawing. The game continues until the player either guesses the word correctly or exhausts all guesses.

![Responsive Mockup](https://github.com/ellisrobertsx/hangman/blob/main/assets/images/hangman.png)

## Contents
- [Home Page](#Home-page)
- [Game Page](#Quiz-page)
- [Planning Stage](#Planning-Stage)
- [Guess The Action Movie](#Guess-the-Action-Movie)
- [Guess The Horror Movie](#Guess-the-Horror-Movie)
- [Guess The Comedy Movie](#Guess-the-Comedy-Movie)
- [Testing](#Testing)
- [Bugs Fixed](#bugs-fixed)
- [Credits](#credits)
- [Deployment](#Deployment)

### Home Page 
[Back to contents](#Contents)

The home page is the starting point of the game where users are prompted to select a game mode. The user can choose from three genres: Action, Horror, or Comedy by pressing the corresponding keys ('A' for Action, 'B' for Horror, 'C' for Comedy).

### Game Page 
[Back to contents](#Contents)

Once a game mode is selected, the game starts and the player is taken to the game page. Here, the hangman game is displayed with underscores representing the letters in the movie title and slashes (/) indicating spaces between words. The player guesses letters until the word is completed or the hangman drawing is fully displayed.

### Planning Stage 
[Back to contents](#Contents)

- Genre Selection: Create lists of movie titles for each genre.
- Game Logic: Implement the hangman game mechanics including guess validation, updating the display for correct/incorrect  
  guesses, and determining the win/loss condition.
- User Interface: Design the interface for displaying the game state and handling user input.
- Replay Option: Allow the player to choose whether to play again after each game.

### Guess The Action Movie 
[Back to contents](#Contents)

![Responsive Mockup](https://github.com/ellisrobertsx/hangman/blob/main/assets/images/hangman1.png)
When the player selects the Action genre, the game will randomly pick a movie from the action_list. The player then guesses letters to figure out the title of the action movie.

### Guess The Horror Movie 
[Back to contents](#Contents)

![Responsive Mockup](https://github.com/ellisrobertsx/hangman/blob/main/assets/images/hangman1.png)
When the player selects the Horror genre, the game will randomly pick a movie from the horror_list. The player then guesses letters to figure out the title of the horror movie.

### Guess The Comedy Movie 
[Back to contents](#Contents)

![Responsive Mockup](https://github.com/ellisrobertsx/hangman/blob/main/assets/images/hangman1.png)
When the player selects the Comedy genre, the game will randomly pick a movie from the comedy_list. The player then guesses letters to figure out the title of the comedy movie.

### Testing 
[Back to contents](#Contents)

- Ensuring that the game displays the correct number of underscores and slashes for the chosen movie title.
- Validating user input to accept only single alphabetic characters.
- Checking the game logic for handling correct and incorrect guesses.
- Ensuring the replay functionality returns the user to the genre selection or exits the game as desired.
- Passed the code through a PEP8 linter and confirmed there are no errors 
- Tested in my local terminal and the Code Insitute Heroku terminal 

### Bugs Fixed 
[Back to contents](#Contents)

- Trailing Whitespace: Removed unnecessary trailing whitespace to adhere to PEP 8 standards.
- Function Definitions: Ensured proper spacing before function definitions to improve code readability and maintainability.

### Credits
[Back to contents](#Contents)

- Code Insitute
- Wikipedia
- Fellow Slack Users 
- Chat GPT
- W3 Users 
- Youtube 

### Deployment
[Back to contents](#Contents)

This project was deployed using Code Insitute's mock terminal for Heroku
- Fork or Clone the repository 
- Created a new Heroku app
- Set the builpacks to Python and NodeJS in that order 
- Link the Heroku app to repository 
- Click on Deploy 

