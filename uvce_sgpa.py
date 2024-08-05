import tkinter as tk
from tkinter import messagebox

def calculate_sgpa():
    try:
        # Initialize subject dictionary based on cycle
        subjects = {}
        weights = {}
        
        if cycle_var.get() == "P Cycle":
            subjects = {
                "Media": (int(entries['Media'][0].get()), int(entries['Media'][1].get())),
                "Maths": (int(entries['Maths'][0].get()), int(entries['Maths'][1].get())),
                "Electrical": (int(entries['Electrical'][0].get()), int(entries['Electrical'][1].get())),
                "Physics": (int(entries['Physics'][0].get()), int(entries['Physics'][1].get())),
                "Physics Lab": (int(entries['Physics Lab'][0].get()), int(entries['Physics Lab'][1].get())),
                "Electrical Lab": (int(entries['Electrical Lab'][0].get()), int(entries['Electrical Lab'][1].get())),
                "Graphics": (int(entries['Graphics'][0].get()), int(entries['Graphics'][1].get())),
                "Mechanics": (int(entries['Mechanics'][0].get()), int(entries['Mechanics'][1].get())),
                "English": (int(entries['English'][0].get()), int(entries['English'][1].get()))
            }

            weights = {
                "Media": 1,
                "Maths": 3,
                "Electrical": 3,
                "Physics": 3,
                "Physics Lab": 1,
                "Electrical Lab": 1,
                "Graphics": 3,
                "Mechanics": 3,
                "English": 2
            }

        elif cycle_var.get() == "C Cycle":
            subjects = {
                "Dti": (int(entries['Dti'][0].get()), int(entries['Dti'][1].get())),
                "Maths": (int(entries['Maths'][0].get()), int(entries['Maths'][1].get())),
                "Mes": (int(entries['Mes'][0].get()), int(entries['Mes'][1].get())),
                "Chemistry": (int(entries['Chemistry'][0].get()), int(entries['Chemistry'][1].get())),
                "Chemistry Lab": (int(entries['Chemistry Lab'][0].get()), int(entries['Chemistry Lab'][1].get())),
                "PPS Lab": (int(entries['PPS Lab'][0].get()), int(entries['PPS Lab'][1].get())),
                "POE": (int(entries['POE'][0].get()), int(entries['POE'][1].get())),
                "Workshop": (int(entries['Workshop'][0].get()), int(entries['Workshop'][1].get())),
                "PPS": (int(entries['PPS'][0].get()), int(entries['PPS'][1].get()))
            }

            weights = {
                "Dti": 1,
                "Maths": 3,
                "Mes": 3,
                "Chemistry": 3,
                "Chemistry Lab": 1,
                "PPS Lab": 1,
                "PPS": 3,
                "POE": 3,
                "Workshop": 2
            }
        else:
            messagebox.showerror("Cycle Error", "Please select a cycle!")
            return

        total_points = 0
        total_weight = 0
        fail_subjects = []

        # Iterate through the subjects to calculate total points and weight
        for subject, (int_marks, sem) in subjects.items():
            if int_marks > 50 or sem > 100:
                raise ValueError(f"Invalid marks entered for {subject}. Please check the inputs.")

            # Calculate total marks
            total_marks = int_marks + (sem // 2)

            # Calculate points based on total marks
            if sem < 40:
                fail_subjects.append(subject)
                points = 0
            elif 90 <= total_marks <= 100:
                points = 10
            elif 80 <= total_marks < 90:
                points = 9
            elif 70 <= total_marks < 80:
                points = 8
            elif 60 <= total_marks < 70:
                points = 7
            elif 50 <= total_marks < 60:
                points = 6
            elif 40 <= total_marks < 50:
                points = 5
            else:
                points = 0

            # Calculate weighted points
            weight = weights[subject]
            total_points += points * weight
            total_weight += weight

        # Calculate SGPA
        sgpa = total_points / total_weight
        fail_message = "\n".join(f"Failed in {subject}" for subject in fail_subjects)
        messagebox.showinfo("SGPA Calculator", f"Your SGPA is {sgpa:.2f}\n{fail_message if fail_subjects else ''}")

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

def create_subject_row(parent, row, subject):
    tk.Label(parent, text=subject).grid(row=row, column=0, padx=5, pady=5)
    int_entry = tk.Entry(parent, width=5)
    int_entry.grid(row=row, column=1, padx=5, pady=5)
    sem_entry = tk.Entry(parent, width=5)
    sem_entry.grid(row=row, column=2, padx=5, pady=5)
    return int_entry, sem_entry

def update_subjects(*args):
    # Clear the frame for new subject rows
    for widget in frame.winfo_children():
        widget.destroy()

    tk.Label(frame, text="Subject").grid(row=0, column=0, padx=5, pady=5)
    tk.Label(frame, text="Internal Marks").grid(row=0, column=1, padx=5, pady=5)
    tk.Label(frame, text="Approximate Marks in Sem").grid(row=0, column=2, padx=5, pady=5)

    global entries
    entries = {}

    # Dynamically create subject entries based on the selected cycle
    if cycle_var.get() == "P Cycle":
        entries['Media'] = create_subject_row(frame, 1, "Media")
        entries['Maths'] = create_subject_row(frame, 2, "Maths")
        entries['Electrical'] = create_subject_row(frame, 3, "Electrical")
        entries['Physics'] = create_subject_row(frame, 4, "Physics")
        entries['Physics Lab'] = create_subject_row(frame, 5, "Physics Lab")
        entries['Electrical Lab'] = create_subject_row(frame, 6, "Electrical Lab")
        entries['Graphics'] = create_subject_row(frame, 7, "Graphics")
        entries['Mechanics'] = create_subject_row(frame, 8, "Mechanics")
        entries['English'] = create_subject_row(frame, 9, "English")

    elif cycle_var.get() == "C Cycle":
        entries['Dti'] = create_subject_row(frame, 1, "Dti")
        entries['Maths'] = create_subject_row(frame, 2, "Maths")
        entries['Mes'] = create_subject_row(frame, 3, "Mes")
        entries['Chemistry'] = create_subject_row(frame, 4, "Chemistry")
        entries['Chemistry Lab'] = create_subject_row(frame, 5, "Chemistry Lab")
        entries['PPS Lab'] = create_subject_row(frame, 6, "PPS Lab")
        entries['POE'] = create_subject_row(frame, 7, "POE")
        entries['Workshop'] = create_subject_row(frame, 8, "Workshop")
        entries['PPS'] = create_subject_row(frame, 9, "PPS")

# Create the main application window
app = tk.Tk()
app.title("UVCE SGPA Calculator")

# Create cycle selection radio buttons
tk.Label(app, text="Select Cycle:").grid(row=0, column=0, padx=5, pady=5)

cycle_var = tk.StringVar()
cycle_var.trace("w", update_subjects)  # Trigger update when selection changes
tk.Radiobutton(app, text="P Cycle", variable=cycle_var, value="P Cycle").grid(row=0, column=1, padx=5, pady=5)
tk.Radiobutton(app, text="C Cycle", variable=cycle_var, value="C Cycle").grid(row=0, column=2, padx=5, pady=5)

# Frame for subject entries
frame = tk.Frame(app)
frame.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

# Initial call to setup the subject rows
update_subjects()

# Calculate SGPA button
tk.Button(app, text="Calculate SGPA", command=calculate_sgpa).grid(row=2, column=0, columnspan=3, padx=5, pady=5)

# Run the application
app.mainloop()
