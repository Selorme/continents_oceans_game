# Continents and Oceans Game

This Python project is a learning game that helps users memorize the names and locations of continents and oceans on a world map. The user is prompted to enter names of continents and oceans, and their correct guesses are displayed on the map. If they choose to exit, the program provides a list of places they missed to help with further learning.

## Features

- **Interactive Gameplay**: Users are asked to name continents and oceans. Correct answers are shown on a world map using turtle graphics.
- **Progress Tracking**: The game keeps track of correct guesses and displays the total number of places guessed correctly.
- **CSV Integration**: Stores the coordinates of the continents and oceans in a CSV file, allowing users to compare what they missed after they exit.
- **Learning Assistance**: Upon exiting, the program generates a CSV file (`continents_and_oceans_to_learn.csv`) with places the user didn't guess.

## Requirements

- **Python 3.x**
- **Pandas** for handling CSV files
- **Turtle** for graphics and display

## How It Works

1. **Display World Map**:  
   The program uses a `.gif` image of the world map to display the game background.
   
2. **Prompt for User Input**:  
   The user is asked to enter the name of a continent or ocean. If they guess correctly, the name is displayed at the appropriate coordinates on the map.

3. **Exit Option**:  
   If the user types "Exit", the game ends and generates a list of the places they didn't guess in a new CSV file.

4. **Tracking Progress**:  
   The number of correct guesses is tracked and displayed in the title bar of the game window.

## How to Play

1. **Run the Game**:  
   Start the game by running the Python script. The game window will display a world map, and the user will be prompted to enter names of continents or oceans.

2. **Input Names**:  
   Type the name of a continent or ocean in the input box. If it's correct, the name will be written at its location on the map.

3. **Exit the Game**:  
   Type "Exit" to stop the game. A CSV file will be created containing the names of the places you didn't guess.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Selorme/continents_oceans_game.git
   cd continents-oceans-game
   ```

2. **Install Dependencies**:
   Install the required libraries using pip:
   ```bash
   pip install pandas
   ```

3. **Add the World Map Image**:  
   Ensure you have the `world_map.gif` image in the same directory as the script. This image will be used as the background map for the game.

4. **Run the Script**:
   Run the game with the following command:
   ```bash
   python main.py
   ```

## CSV Files

- `continents_and_oceans.csv`: Contains the names and coordinates of the continents and oceans.
- `continents_and_oceans_to_learn.csv`: Generated when the user exits the game, listing the places they didn't guess.

## Example Output

```text
Guess the names of continents and oceans on the map!
Correctly guessed 5/12 places:
- North America
- Pacific Ocean
- Europe
```

## Future Enhancements

- Add more detailed error handling for invalid inputs.
- Expand the game to include additional geographical features like seas or specific countries.
- Implement a scoring system or a time limit to increase the challenge.

## License

This project is licensed under the MIT License.