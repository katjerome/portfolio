import tkinter as tk
from tkinter import messagebox
from employee_reg import EmployeeRegistry

class EmployeeGUI:
    def __init__(self, root):
        self.registry = EmployeeRegistry()
        self.root = root
        self.root.title("Employee Registry")

        # Create and place widgets
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        tk.Label(self.root, text="Employee Registry", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)

        # Buttons
        tk.Button(self.root, text="View All Employees", command=self.view_all_employees).grid(row=1, column=0, pady=5)
        tk.Button(self.root, text="Add Employee", command=self.add_employee).grid(row=1, column=1, pady=5)
        tk.Button(self.root, text="View Employee by ID", command=self.view_employee_by_id).grid(row=2, column=0, pady=5)
        tk.Button(self.root, text="Edit Employee", command=self.edit_employee).grid(row=2, column=1, pady=5)
        tk.Button(self.root, text="Remove Employee", command=self.remove_employee).grid(row=3, column=0, pady=5)
        tk.Button(self.root, text="Exit", command=self.root.quit).grid(row=3, column=1, pady=5)

    def view_all_employees(self):
        employees = self.registry.view_all_employees()
        messagebox.showinfo("All Employees", employees)

    def add_employee(self):
        def submit():
            first_name = entry_first_name.get()
            last_name = entry_last_name.get()
            id_number = entry_id_number.get()
            result = self.registry.add_employee(first_name, last_name, id_number)
            messagebox.showinfo("Result", result)
            add_window.destroy()

        add_window = tk.Toplevel(self.root)
        add_window.title("Add Employee")

        tk.Label(add_window, text="First Name:").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(add_window, text="Last Name:").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(add_window, text="ID Number:").grid(row=2, column=0, padx=10, pady=5)

        entry_first_name = tk.Entry(add_window)
        entry_last_name = tk.Entry(add_window)
        entry_id_number = tk.Entry(add_window)

        entry_first_name.grid(row=0, column=1, padx=10, pady=5)
        entry_last_name.grid(row=1, column=1, padx=10, pady=5)
        entry_id_number.grid(row=2, column=1, padx=10, pady=5)

        tk.Button(add_window, text="Submit", command=submit).grid(row=3, column=0, columnspan=2, pady=10)

    def view_employee_by_id(self):
        def search():
            id_number = entry_id_number.get()
            result = self.registry.view_employee_by_id(id_number)
            messagebox.showinfo("Employee Details", result)
            search_window.destroy()

        search_window = tk.Toplevel(self.root)
        search_window.title("View Employee by ID")

        tk.Label(search_window, text="ID Number:").grid(row=0, column=0, padx=10, pady=5)
        entry_id_number = tk.Entry(search_window)
        entry_id_number.grid(row=0, column=1, padx=10, pady=5)

        tk.Button(search_window, text="Search", command=search).grid(row=1, column=0, columnspan=2, pady=10)

    def edit_employee(self):
        def submit():
            employee_name = entry_name.get()
            new_id_number = entry_new_id.get()
            result = self.registry.edit_employee(employee_name, new_id_number)
            messagebox.showinfo("Result", result)
            edit_window.destroy()

        edit_window = tk.Toplevel(self.root)
        edit_window.title("Edit Employee")

        tk.Label(edit_window, text="Employee Name:").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(edit_window, text="New ID Number:").grid(row=1, column=0, padx=10, pady=5)

        entry_name = tk.Entry(edit_window)
        entry_new_id = tk.Entry(edit_window)

        entry_name.grid(row=0, column=1, padx=10, pady=5)
        entry_new_id.grid(row=1, column=1, padx=10, pady=5)

        tk.Button(edit_window, text="Submit", command=submit).grid(row=2, column=0, columnspan=2, pady=10)

    def remove_employee(self):
        def submit():
            employee_name = entry_name.get()
            result = self.registry.remove_employee(employee_name)
            messagebox.showinfo("Result", result)
            remove_window.destroy()

        remove_window = tk.Toplevel(self.root)
        remove_window.title("Remove Employee")

        tk.Label(remove_window, text="Employee Name:").grid(row=0, column=0, padx=10, pady=5)
        entry_name = tk.Entry(remove_window)
        entry_name.grid(row=0, column=1, padx=10, pady=5)

        tk.Button(remove_window, text="Submit", command=submit).grid(row=1, column=0, columnspan=2, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeGUI(root)
    root.mainloop()