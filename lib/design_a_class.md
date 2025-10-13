# TodoList Class Design

## 1. Describe the Problem

**User Story 1:**

> As a user  
> So that I can keep track of my tasks  
> I want a program that I can add todo tasks to and see a list of them.

**User Story 2:**

> As a user  
> So that I can focus on tasks to complete  
> I want to mark tasks as complete and have them disappear from the list.

**Clarifying Notes:**
- The program should allow adding tasks.
- The user can list current tasks (only incomplete ones).
- The user can mark a task as complete by specifying its name.
- Once marked as complete, a task no longer appears in the list.

---

## 2. Design the Class Interface

```python
class TodoList:
    # User-facing properties:
    #   tasks: list of dictionaries like {'task': str, 'complete': bool}

    def __init__(self):
        # Side-effects:
        #   Initializes an empty list of tasks
        pass

    def add(self, task):
        # Parameters:
        #   task: string representing the task to be added
        # Side-effects:
        #   Adds the task to the list as incomplete
        pass

    def list(self):
        # Returns:
        #   List of strings: all tasks that are not marked complete
        pass

    def mark_complete(self, task):
        # Parameters:
        #   task: string representing the task to mark as complete
        # Side-effects:
        #   Marks the matching task as complete
        # Raises:
        #   ValueError if task is not found
        pass
```

## 3. Create Examples as Tests

```python

"""
When no tasks are added
#list returns an empty list
"""
todo = TodoList()
todo.list()  # => []

"""
When one task is added
#list returns a list with that task
"""
todo = TodoList()
todo.add("Buy milk")
todo.list()  # => ["Buy milk"]

"""
When multiple tasks are added
#list returns them in the order added
"""
todo = TodoList()
todo.add("Buy milk")
todo.add("Walk the dog")
todo.add("Do homework")
todo.list()  # => ["Buy milk", "Walk the dog", "Do homework"]

"""
When one task is marked complete
#list excludes that task
"""
todo = TodoList()
todo.add("Buy milk")
todo.add("Walk the dog")
todo.mark_complete("Buy milk")
todo.list()  # => ["Walk the dog"]

"""
When multiple tasks are marked complete
#list returns only the remaining incomplete ones
"""
todo = TodoList()
todo.add("Buy milk")
todo.add("Walk the dog")
todo.add("Do homework")
todo.mark_complete("Walk the dog")
todo.mark_complete("Do homework")
todo.list()  # => ["Buy milk"]

"""
When trying to complete a task that doesn’t exist
#mark_complete raises a ValueError with the message
"""
todo = TodoList()
todo.add("Buy milk")
todo.mark_complete("Go to gym")  # => raises ValueError("Task not found: Go to gym")

"""
When the same task is added twice
#list returns both instances
"""
todo = TodoList()
todo.add("Buy milk")
todo.add("Buy milk")
todo.list()  # => ["Buy milk", "Buy milk"]

"""
When one of two duplicate tasks is marked complete
#list still includes the other one
"""
todo = TodoList()
todo.add("Buy milk")
todo.add("Buy milk")
todo.mark_complete("Buy milk")
todo.list()  # => ["Buy milk"]

"""
When both duplicate tasks are marked complete
#list returns an empty list
"""
todo = TodoList()
todo.add("Buy milk")
todo.add("Buy milk")
todo.mark_complete("Buy milk")
todo.mark_complete("Buy milk")
todo.list()  # => []

"""
When a task is an empty string
#list includes the empty task
"""
todo = TodoList()
todo.add("")
todo.list()  # => [""]

"""
When an empty string task is marked complete
#list no longer includes it
"""
todo = TodoList()
todo.add("")
todo.mark_complete("")
todo.list()  # => []

"""
When a task includes special characters
#mark_complete still removes it correctly
"""
todo = TodoList()
todo.add("Clean @home #urgent!")
todo.mark_complete("Clean @home #urgent!")
todo.list()  # => []

"""
When one task is marked complete
#list still shows the other
"""
todo = TodoList()
todo.add("Task 1")
todo.add("Task 2")
todo.mark_complete("Task 1")
todo.list()  # => ["Task 2"]

"""
When the same task is marked complete twice
#second attempt raises ValueError
"""
todo = TodoList()
todo.add("Task 1")
todo.mark_complete("Task 1")
todo.mark_complete("Task 1")  # => raises ValueError("Task not found: Task 1")

```
## 4. Implement the behaviour

```python

import pytest
from your_module_name import TodoList  # Replace with the actual module name

# ---------- Initial State ----------

def test_list_returns_empty_when_no_tasks_added():
    todo = TodoList()
    assert todo.list() == []

# ---------- Adding Tasks ----------

def test_list_returns_single_task_after_adding_one():
    todo = TodoList()
    todo.add("Buy milk")
    assert todo.list() == ["Buy milk"]

def test_list_returns_tasks_in_order_added():
    todo = TodoList()
    todo.add("Buy milk")
    todo.add("Walk the dog")
    todo.add("Do homework")
    assert todo.list() == ["Buy milk", "Walk the dog", "Do homework"]

# ---------- Marking Tasks Complete ----------

def test_mark_complete_removes_task_from_list():
    todo = TodoList()
    todo.add("Buy milk")
    todo.add("Walk the dog")
    todo.mark_complete("Buy milk")
    assert todo.list() == ["Walk the dog"]

def test_mark_complete_multiple_tasks():
    todo = TodoList()
    todo.add("Buy milk")
    todo.add("Walk the dog")
    todo.add("Do homework")
    todo.mark_complete("Walk the dog")
    todo.mark_complete("Do homework")
    assert todo.list() == ["Buy milk"]


def test_mark_complete_raises_error_if_task_not_found():
    todo = TodoList()
    todo.add("Buy milk")
    with pytest.raises(ValueError, match="Task not found: Go to gym"):
        todo.mark_complete("Go to gym")

def test_adding_duplicate_tasks_keeps_both():
    todo = TodoList()
    todo.add("Buy milk")
    todo.add("Buy milk")
    assert todo.list() == ["Buy milk", "Buy milk"]

def test_marking_one_of_duplicate_tasks_marks_first_one_only():
    todo = TodoList()
    todo.add("Buy milk")
    todo.add("Buy milk")
    todo.mark_complete("Buy milk")
    assert todo.list() == ["Buy milk"]

def test_all_duplicate_tasks_can_be_marked_complete_individually():
    todo = TodoList()
    todo.add("Buy milk")
    todo.add("Buy milk")
    todo.mark_complete("Buy milk")
    todo.mark_complete("Buy milk")
    assert todo.list() == []

def test_add_empty_string_task():
    todo = TodoList()
    todo.add("")
    assert todo.list() == [""]

def test_mark_complete_on_empty_string_task():
    todo = TodoList()
    todo.add("")
    todo.mark_complete("")
    assert todo.list() == []

def test_add_and_complete_task_with_special_characters():
    todo = TodoList()
    todo.add("Clean @home #urgent!")
    todo.mark_complete("Clean @home #urgent!")
    assert todo.list() == []

def test_mark_complete_does_not_remove_other_tasks():
    todo = TodoList()
    todo.add("Task 1")
    todo.add("Task 2")
    todo.mark_complete("Task 1")
    assert "Task 2" in todo.list()

def test_mark_complete_twice_raises_error_on_second_time():
    todo = TodoList()
    todo.add("Task 1")
    todo.mark_complete("Task 1")
    with pytest.raises(ValueError, match="Task not found: Task 1"):
        todo.mark_complete("Task 1")


```