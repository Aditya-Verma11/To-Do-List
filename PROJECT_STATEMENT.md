# Project Statement: To-Do List Program

## Problem Statement

Many people forget tasks because they keep them only in their heads or on loose pieces of paper. This makes it hard to know what is finished and what is still left to do. Beginners who are learning Python also need a small, practical project to practice basic programming ideas.

This project solves both problems. It gives users a simple way to manage daily tasks in the terminal, and it shows how core Python concepts work in a real program.

## Scope of Project

### In Scope

- A command-line (terminal) program written in Python
- Adding new tasks
- Removing tasks
- Marking tasks as completed
- Viewing all tasks, completed tasks, or pending tasks
- Basic input checking (empty task names, wrong numbers, invalid menu choices)
- Tasks are stored in memory while the program is running

### Out of Scope

- Saving tasks to a file or database (tasks are lost when the program closes)
- Graphical user interface (buttons, windows)
- User accounts or logins
- Due dates, reminders, or priority levels
- Syncing across devices or online access

## Target Users

- **Beginner Python learners** who want a small project to read, run, and improve
- **Students** who need a simple way to list their daily study tasks
- **Anyone who likes the terminal** and wants a quick, lightweight task list with no installation beyond Python
- **Teachers and mentors** who need an easy example to explain lists, dictionaries, functions, and loops

## High-Level Features

| Feature | Description |
|---------|-------------|
| Add Task | Enter a task name and add it to the list |
| Remove Task | Choose a task by its number and delete it |
| Mark as Completed | Choose a task by its number and mark it as done |
| View All Tasks | See every task along with its status (Done or Pending) |
| View Completed Tasks | See only the tasks that are finished |
| View Pending Tasks | See only the tasks that are still to do |
| Menu-Based Navigation | A simple numbered menu that runs until the user chooses to exit |
| Input Validation | Friendly messages for empty names, invalid numbers, and wrong menu choices |
