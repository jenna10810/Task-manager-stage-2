# Task-manager-stage-2

## Stage 2
In this project, the previous _"project manager"_ task had less features and in this program, more features have been added. Functions are added to simplify the code and to add functionality.

## Actual code
The code has been modified to have functions. Some notable features included, is the ability to tell the user that they have tried to register a user that already exists, the tasks all have numbers by which they can be identified and thus modified - including the due date, to whom the task is assigned and whether the task is complete.
The _admin_ user also has the option to generate reports, these reports include _task_overview.txt_ as well as _user_overview_. 
The _task_overview.txt_ file contains:
* the total number of tasks that have been generated and tracked using _task_manager.py_
* the total number of completed tasks
* the total number of uncompleted tasks
* the total number of tasks that haven't been completed and that are overdue
* the percentage of tasks that are incomplete
* the percentage of tasks that are overdue

The _user_overview.txt_ file contains:
* the total number of registered users
* the total number of tasks that have been generated 
* for each user it also desribes:
  * the total number of tasks assigned to the user
  * what percentage of the total number of tasks have been assigned to the user
  * what percentage of tasks assigned to the user have been completed
  * what percentage of tasks assigned to the user must still be completed
  * what percentage of tasks assigned to the user have not yet been completed and are overdue
