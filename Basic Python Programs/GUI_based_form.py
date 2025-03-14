import tkinter as tk
from tkinter import messagebox

def show_custom_dialog():
    messagebox.showinfo("Note", "Tech Zephyr banner reveal @ 12pm!")
    
def submit_form():
    username = username_entry.get()
    password = password_entry.get()
    selected_gender = gender_var.get()
    selected_branch = [branch[i] for i, branch_var in enumerate(branch_vars) if branch_var.get()]
    selected_year = [year[j] for j, year_var in enumerate(year_vars) if year_var.get()]
    selected_interest = [interest[k] for k, interest_var in enumerate(interest_vars) if interest_var.get()]
     
    print(f"Username: {username}")
    print(f"Password: {password}")
    print(f"Gender: {selected_gender}")
    print(f"Branch: {', '.join(selected_branch)}")
    print(f"Year: {', '.join(selected_year)}")
    print(f"Interest: {', '.join(selected_interest)}")
   
# Create main window
root = tk.Tk()
root.title("Tech Zephyr Volunteering")

# Create and place widgets in the window

# Labels
tk.Label(root, text="User Name:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
tk.Label(root, text="Gender:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
tk.Label(root, text="Branch:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
tk.Label(root, text="Year:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
tk.Label(root, text="Interest:").grid(row=5, column=0, padx=10, pady=5, sticky="e")

# Entry Widgets
username_entry = tk.Entry(root)
password_entry = tk.Entry(root, show='*')

# Radio Buttons
gender_var = tk.StringVar()
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").grid(row=2, column=1, pady=5)
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").grid(row=2, column=2, pady=5)
tk.Radiobutton(root, text="Others", variable=gender_var, value="Others").grid(row=2, column=3, pady=5)

# Checkboxes
branch = ["Compueter Engg.", "CSE (AIML)", "CSE (DS)", "CSE (IoT & CSBT)", "Electronics Engg.", "Mechanical Engg."]
branch_vars = [tk.BooleanVar() for _ in range(len(branch))]
for i, brch in enumerate(branch):
    tk.Checkbutton(root, text=brch, variable=branch_vars[i]).grid(row=3, column=i+1, pady=5)

year = ["FE", "SE", "TE", "BE"]
year_vars = [tk.BooleanVar() for _ in range(len(year))]
for j, yr in enumerate(year):
    tk.Checkbutton(root, text=yr, variable=year_vars[j]).grid(row=4, column=j+1, pady=5)

interest = ["Sports Team", "Creative Team", "Technical Team", "Musical Team"]
interest_vars = [tk.BooleanVar() for _ in range(len(interest))]
for k, intr in enumerate(interest):
    tk.Checkbutton(root, text=intr, variable=interest_vars[k]).grid(row=5, column=k+1, pady=5)

# Button to show custom dialog
tk.Button(root, text="Click here for news", command=show_custom_dialog).grid(row=6, column=0, columnspan=3, pady=10)

#submit form
tk.Button(root, text="Submit", command=submit_form).grid(row=7, column=0, columnspan=3, pady=20)

# Place Entry widgets
username_entry.grid(row=0, column=1, columnspan=2, pady=5)
password_entry.grid(row=1, column=1, columnspan=2, pady=5)

# Run the GUI
root.mainloop()
