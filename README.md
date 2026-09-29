# To-Do-List
A simple to-do list that runs in the terminal. You can add tasks, mark them as done, remove them, and see what is left to do. It is written in plain Python and needs no extra libraries, so it is a good project for beginners.

## Features

- Add a new task
- Remove a task
- Mark a task as completed
- Show all tasks
- Show only completed tasks
- Show only pending tasks

## Requirements

- Python 3.6 or newer

To check if Python is installed, run:



## How to Run


2. Run the program:

   ```bash
   python todo.py
   ```

   On some systems you may need to use `python3` instead of `python`.

## How to Use

When the program starts, you will see this menu:

```
******* TO-DO LIST MENU *******
1. Add task
2. Remove task
3. Mark task as completed
4. Show all tasks
5. Show completed tasks
6. Show pending tasks
0. Exit
Choose an option:
```

Type the number of the option you want and press **Enter**.

| Option | What it does |
|--------|--------------|
| 1 | Asks for a task name and adds it to your list |
| 2 | Shows your tasks, then asks which task number to remove |
| 3 | Shows your tasks, then asks which task number to mark as done |
| 4 | Shows every task with its status (Done or Pending) |
| 5 | Shows only the tasks you have finished |
| 6 | Shows only the tasks you still need to do |
| 0 | Exits the program |

## Example

```
Choose an option: 1
Enter task name: Buy groceries
Task "Buy groceries" added.

Choose an option: 4

 All Tasks 
1. Buy groceries [Pending]

Choose an option: 3
 All Tasks 
1. Buy groceries [Pending]

Enter task number to mark as completed: 1
Task "Buy groceries" marked as completed.
```

## How It Works

- Tasks are stored in a Python list called `tasks`.
- Each task is a dictionary with two values: the task `name` and whether it is `done` (True or False).
- The program uses a loop to keep showing the menu until you choose `0` to exit.

## Good to Know

- Tasks are saved only while the program is running. When you exit, the list is cleared.
- Empty task names are not allowed.
- If you type an invalid number or letter, the program shows a message and lets you try again.

## Ideas for Future Improvements

- Save tasks to a file so they are not lost when the program closes
- Add due dates or priority levels
- Allow editing an existing task
- Build a simple graphical interface



