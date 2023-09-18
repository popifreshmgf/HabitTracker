from project import HabitTracker

def test_create_habit():
    habit_tracker = HabitTracker()
    habit_tracker.create_habit()
    assert len(habit_tracker.habitos) == 1

def test_tick_habit():
    habit_tracker = HabitTracker()
    habit_tracker.create_habit()
    habit_tracker.tick_habit()
    assert habit_tracker.habitos[0]["CHECK"] == "[✓]"

def test_delete_habit():
    habit_tracker = HabitTracker()
    habit_tracker.create_habit()
    habit_tracker.delete_habit()
    assert len(habit_tracker.habitos) == 0




if __name__ == "__main__":
    import pytest
    pytest.main()
