import requests
from datetime import datetime, timedelta

# Asana API Configuration
ASANA_ACCESS_TOKEN = "2/1208817288820892/1208826845073213:0c3ac9710b98934cfbfad8450081b11b"
WORKSPACE_ID = "1208826928586202"
HEADERS = {
    "Authorization": f"Bearer {ASANA_ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

# Define Priority Levels and Due Dates
PRIORITY_DUE_DAYS = {
    "Low": 14,
    "Mid": 7,
    "High": 2
}

# Function to calculate due date based on priority
def calculate_due_date(priority_level):
    """
    Calculate the due date for a task based on its priority level.
    """
    return (datetime.now() + timedelta(days=PRIORITY_DUE_DAYS[priority_level])).strftime("%Y-%m-%d")

# Function to assign a due date to a task
def assign_due_date(task_id, due_date):
    """
    Assign a specific due date to a task.
    """
    url = f"https://app.asana.com/api/1.0/tasks/{task_id}"
    payload = {
        "data": {
            "due_on": due_date
        }
    }
    response = requests.put(url, headers=HEADERS, json=payload)
    if response.status_code == 200:
        print(f"Task {task_id} updated with due date: {due_date}")
    else:
        print(f"Failed to update task {task_id}: {response.text}")

# Function to extend due dates for tasks in 'In Progress'
def extend_due_dates_in_progress(high_priority_task_id, project_id):
    """
    Extend the due dates of all tasks in the 'In Progress' section, except the high-priority task.
    """
    url = f"https://app.asana.com/api/1.0/projects/{project_id}/tasks?opt_fields=id,due_on,assignee_status"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        tasks = response.json().get("data", [])
        for task in tasks:
            task_id = task.get("id")
            due_on = task.get("due_on")
            assignee_status = task.get("assignee_status")

            # Skip the high-priority task
            if task_id == high_priority_task_id:
                continue

            # Ensure the task is in progress and has a due date
            if not due_on or assignee_status != "in_progress":
                print(f"Skipping task {task_id} - No due date or not in progress.")
                continue

            try:
                current_due_date = datetime.strptime(due_on, "%Y-%m-%d")
                new_due_date = (current_due_date + timedelta(days=2)).strftime("%Y-%m-%d")
                assign_due_date(task_id, new_due_date)
            except ValueError:
                print(f"Invalid due date format for task {task_id}: {due_on}")
    else:
        print(f"Failed to fetch tasks in project {project_id}: {response.text}")

# Function to verify the validity of a project ID
def verify_project_id(project_id):
    """
    Verify whether the provided project ID is valid.
    """
    url = f"https://app.asana.com/api/1.0/projects/{project_id}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        print(f"Project ID {project_id} is invalid: {response.text}")
        return False
    return True

# Main function to handle task updates
def handle_task_update(task_id, priority_level, project_id):
    """
    Main function to handle task updates:
    1. Assigns a due date based on priority.
    2. Extends due dates of other tasks in progress if priority is high.
    """
    # Assign due date based on priority
    due_date = calculate_due_date(priority_level)
    assign_due_date(task_id, due_date)

    # If priority is High, extend due dates for other tasks in progress
    if priority_level == "High":
        extend_due_dates_in_progress(task_id, project_id)

# Entry point
if __name__ == "__main__":
    TASK_ID = "1208826928587395"
    PRIORITY_LEVEL = "Low"  # Change to Low, Mid, or High as needed
    PROJECT_ID = "1208826931765461"
    handle_task_update(TASK_ID, PRIORITY_LEVEL,PROJECT_ID)
