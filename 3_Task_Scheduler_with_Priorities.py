import heapq
import json

tasks = []

def add_task():
    name = input("Task name: ")
    priority = int(input("Priority (1-10): "))
    deadline = input("Deadline (YYYY-MM-DD): ")
    heapq.heappush(tasks, (priority, name, deadline))
    print("Task added.")

def view_tasks():
    print("\n--- Pending Tasks ---")
    for task in sorted(tasks):
        print(f"Priority {task[0]}: {task[1]} - Due {task[2]}")

def mark_done():
    if tasks:
        done = heapq.heappop(tasks)
        print(f"Task completed: {done[1]}")
    else:
        print("No tasks left.")

def main():
    while True:
        print("\n--- Task Scheduler ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_done()
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()