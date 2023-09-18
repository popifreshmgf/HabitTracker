import json
from tabulate import tabulate

class HabitTracker:
    def __init__(self):
        self.habits = []
        self.habit_count = 0

    def main(self):
        self.load_habits_from_file()

        while True:
            action = self.get_user_action()
            if action == "V":
                self.display_habits()
            elif action == "C":
                self.create_habit()
            elif action == "T":
                self.tick_habit()
            elif action == "U":
                self.des_tick_habit()
            elif action == "D":
                self.delete_habit()
            elif action == "S":
                self.save_habits_to_file()
                break
            
                
            else:
                print("Invalid key, try again")

    def get_user_action(self):
        instructions = [
            {"Key": "V", "Usage": "View Habits"},
            {"Key": "C", "Usage": "Create a Habit"},
            {"Key": "T", "Usage": "Tick a Habit"},
            {"Key": "U", "Usage": "To UnTick"},
            {"Key": "D", "Usage": "Delete a Habit"},
            {"Key": "S", "Usage": "To Exit"}
            
        ]
        while True:
            print(tabulate(instructions, headers="keys", tablefmt="heavy_outline"))
            action = input("What would you like to do?").upper()
            if action in ["V", "C", "T", "D", "S",'U']:
                return action
            else:
                print("Invalid key, try again")

    def load_habits_from_file(self, file_path="habits.json"):
        try:
            with open(file_path, "r") as file:
                self.habits = json.load(file)
        except FileNotFoundError:
            self.habits = []
        self.habit_count = max((habit.get("ID", 0) for habit in self.habits), default=0)

    def save_habits_to_file(self, file_path="habits.json"):
        try:
            with open(file_path, "w") as file:
                json.dump(self.habits, file)
        except IOError as e:
            print("Error saving to JSON:", str(e))

    def display_habits(self):
        print(tabulate(self.habits, headers="keys", tablefmt="heavy_outline"))

    def create_habit(self):
        habit = input("What Habit do you want to Create: ")
        checkbox = "[ ]"
        max_id = max((habit.get("ID", 0) for habit in self.habits), default=0)
        habit_id = max_id + 1
        self.habits.append({"ID": habit_id, "Habit": habit, "CHECK": checkbox})

    def tick_habit(self):
        self.display_habits()
        index = int(input("Which habit do you want to tick? Enter the ID: "))
        for habit in self.habits:
            if habit["ID"] == index:
                habit["CHECK"] = "[✓]"
                break
        else:
            print("Invalid ID, try again")

    def des_tick_habit(self):
        self.display_habits()
        index = int(input("Which habit do you want to Untick? Enter the ID: "))
        for habit in self.habits:
            if habit["ID"] == index:
                habit["CHECK"] = "[ ]"
                break
        else:
            print("Invalid ID, try again")

    def delete_habit(self):
        self.display_habits()
        ids = [habit["ID"] for habit in self.habits]

        while True:
            try:
                habit_id = int(input("Which Habit do you want to delete from the list? Enter the ID:"))
                if habit_id in ids:
                    break
                else:
                    print("Invalid ID, try again")
            except ValueError:
                print("Invalid input, try again.")

        for i, habit in enumerate(self.habits):
            if habit["ID"] == habit_id:
                del self.habits[i]
                break

        for i, habit in enumerate(self.habits, start=1):
            habit["ID"] = i

        print("Habit with ID", habit_id, "has been deleted.")

if __name__ == "__main__":
    habit_tracker = HabitTracker()
    habit_tracker.main()
