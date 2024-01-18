class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})
        print(f'Task "{task}" added to the to-do list.')

    def mark_as_done(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["done"] = True
            print(f'Task "{self.tasks[task_index]["task"]}" marked as done.')
        else:
            print("Invalid task index.")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            deleted_task = self.tasks.pop(task_index)
            print(f'Task "{deleted_task["task"]}" deleted from the to-do list.')
        else:
            print("Invalid task index.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("To-Do List:")
            for i, task in enumerate(self.tasks):
                status = "Done" if task["done"] else "Not Done"
                print(f'{i + 1}. {task["task"]} - {status}')


def main():
    to_do_list = ToDoList()

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Mark Task as Done")
        print("3. Delete Task")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            task = input("Enter the task: ")
            to_do_list.add_task(task)
        elif choice == "2":
            to_do_list.display_tasks()
            task_index = int(input("Enter the task index to mark as done: ")) - 1
            to_do_list.mark_as_done(task_index)
        elif choice == "3":
            to_do_list.display_tasks()
            task_index = int(input("Enter the task index to delete: ")) - 1
            to_do_list.delete_task(task_index)
        elif choice == "4":
            to_do_list.display_tasks()
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
