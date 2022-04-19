# U.S.-States-Quiz-Game
A quiz game that tests users on naming all 50 states in the U.S. The player only inputs the states name (regardless of case sensitivity) and it'll appear on the map.

## Modules Used:
- **pandas**: read .csv and manipulate and extract desired data
- **turtle**: create screen and prompts. Also used to display states name on the map.
- **os**: find the file directory of the .csv and image.

## Functions
- **find_file(filename)**: searches directory for the file with the filename as an argument
- **open_file()**: opens the file and uses find_file(filename) function to return data in DataFrame object type
- **setup_screen()**: creates the canvas using turtle module
- **create_state_prompt(answered)**: as the name suggests, this creates an input prompt for the user to type in the answer. "answered" is a list of states that have already been answered.
- **print_state(state)**: this will write the answered state onto the map image. 
- **check_answer(user_answer, answered_list)**: checks the user's answer within a list of states extracted from the DataFrame that holds .csv data. Also checks whether that answer is already answered in the "answered list". If not answered and answer is in the listed states, the state name is printed and the answer is added into the answered_list.
