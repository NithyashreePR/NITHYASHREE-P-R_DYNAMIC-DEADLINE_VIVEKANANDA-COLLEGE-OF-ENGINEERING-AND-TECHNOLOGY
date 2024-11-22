Here’s a `README.md` file template that provides clear instructions for evaluators to run the code along with example inputs.



 Dynamic Deadline Automation using Asana API

 Overview
This project automates due date assignment and updates in Asana tasks based on their priority levels and status changes. Specifically:
1. Assigns a due date to tasks automatically based on priority levels:  
    Low: 14 days  
    Mid: 7 days  
    High: 2 days  
2. Automatically extends due dates for other "In Progress" tasks when a High Priority task is moved to In Progress.  



 Prerequisites

1. Python Installation:  
   Ensure Python 3.7 or later is installed on your system.  
   [Download Python](https://www.python.org/downloads/)

2. Install Dependencies:  
   Install required libraries using the following command:  
   ```bash
   pip install requests
   ```

3. Asana API Token:  
    Generate an Asana API token by logging into Asana and navigating to your account settings under the Apps tab.  
    Update the `ASANA_ACCESS_TOKEN` in the script with your token.

4. Project and Task IDs:  
    Identify a valid Asana Project ID and Task IDs within your workspace.  
    Update the script with appropriate `TASK_ID` and `PROJECT_ID`.



 Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/YourRepoName/DynamicDeadlineAutomation.git
   cd DynamicDeadlineAutomation
   ```

2. Install dependencies:
   ```bash
   pip install r requirements.txt
   ```

3. Update the `ASANA_ACCESS_TOKEN`, `TASK_ID`, and `PROJECT_ID` in the script with your Asana credentials and IDs.

4. Run the script:
   ```bash
   python dynamic_deadline.py
   ```



 Usage Instructions
1. Initial Due Date Assignment  
    The script will assign a due date based on task priority:
      `Low`: 14 days from the current date.
      `Mid`: 7 days from the current date.
      `High`: 2 days from the current date.

2. High Priority Task Movement  
    If a High Priority task is moved to In Progress:
      All other tasks in In Progress will have their due dates extended by 2 days.



 Example Input
In the script:
 Replace the placeholders with real values:
  ```python
  TASK_ID = "your_task_id_here"   Example: "1208826928587395"
  PROJECT_ID = "your_project_id_here"   Example: "1208826931765461"
  PRIORITY_LEVEL = "High"   Options: Low, Mid, High
  ```



 Expected Output
 The script will output updates for task due dates in the console. For example:
  ```plaintext
  Task 1208826928587395 updated with due date: 20241124
  Task 1208826928581234 updated with due date: 20241126
  ```



 Troubleshooting
1. Invalid Project ID:  
   Ensure the `PROJECT_ID` exists in your Asana workspace. Use the verify project function in the script to confirm its validity.

2. API Token Errors:  
   Ensure your API token is valid and has sufficient permissions for the workspace.



 Author
Akash  
[GitHub Profile](https://github.com/YourGitHubProfile)  

Feel free to reach out via GitHub Issues for questions or feedback!
