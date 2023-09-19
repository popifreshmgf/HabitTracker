# Habit Tracker
#### Video Demo: [Watch Video Demo](https://www.youtube.com/watch?v=t6UcJyNCfd4)

#### Description:
The Habit Tracker is a Python script designed to help users monitor and manage their habits effectively. It provides a simple yet efficient way to create, track, and save progress on various habits, aiding individuals in reaching their goals and fostering a sense of accomplishment.

This Python script implements a straightforward habit tracking system. Users can easily create new habits, monitor their progress, and store the information in a JSON file for future reference. It promotes accountability and motivation by enabling users to tick off completed habits and delete those that are no longer relevant.

## Design Choices
- **Tabulate Library:** The use of the `tabulate` library for displaying habits in a tabular format enhances readability and user experience. It presents information in a structured manner, making it easier for users to view and manage their habits.
- **JSON Storage:** Storing habit data in a JSON file allows for easy persistence and retrieval of habits across multiple sessions. JSON is a lightweight, human-readable format, making it ideal for storing structured data related to habits.

## Usage

To utilize the Habit Tracker, simply run the `main()` function. This will initiate the program and guide you through the following actions:

- **V (View Habits):** Display all existing habits along with their respective statuses.
- **C (Create a Habit):** Create a new habit and add it to the tracker.
- **T (Tick a Habit):** Mark a habit as completed once achieved.
- **U (UnTick a Habit):** Unmark a completed habit.
- **B (Delete a Habit):** Remove a habit that is no longer needed.
- **S (To Exit):** Save the current habits to a file and exit the application.

## Contributing
We welcome contributions to enhance the functionality, usability, and features of the Habit Tracker. Feel free to submit issues, fork the repository, and create pull requests.

## Example

Here's an example of how you might use the Habit Tracker:

```plaintext
ID  Habit     CHECK
--  --------  -----
1   Exercise  [ ]

Habit with ID 1 has been ticked.

ID  Habit     CHECK
--  --------  -----
1   Exercise  [✓]




$ pip install tabulate

$ python project.py

$ pytest test_project.py
$ pytest -s

