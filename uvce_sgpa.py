import tkinter as tk
from tkinter import messagebox

def calculate_sgpa():
    try:
        subjects = {
            "Media": (int(media_int.get()), int(media_sem.get())),
            "Maths": (int(maths_int.get()), int(maths_sem.get())),
            "Electrical": (int(electrical_int.get()), int(electrical_sem.get())),
            "Physics": (int(physics_int.get()), int(physics_sem.get())),
            "Physics Lab": (int(physics_lab_int.get()), int(physics_lab_sem.get())),
            "Electrical Lab": (int(electrical_lab_int.get()), int(electrical_lab_sem.get())),
            "Graphics": (int(graphics_int.get()), int(graphics_sem.get())),
            "Mechanics": (int(mechanics_int.get()), int(mechanics_sem.get())),
            "English": (int(english_int.get()), int(english_sem.get()))
        }

        total_points = 0
        total_weight = 0
        fail_subjects = []

        for subject, (int_marks, sem) in subjects.items():
            if int_marks > 50 or sem > 100:
                raise ValueError(f"Invalid marks entered for {subject}. Please check the inputs.")

            total_marks = int_marks + (sem // 2)

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
                points = 5
            elif 40 <= total_marks < 50:
                points = 5
            else:
                points = 0

            weight = {
                "Media": 1,
                "Maths": 3,
                "Electrical": 3,
                "Physics": 3,
                "Physics Lab": 1,
                "Electrical Lab": 1,
                "Graphics": 3,
                "Mechanics": 3,
                "English": 2
            }[subject]

            total_points += points * weight
            total_weight += weight

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

app = tk.Tk()
app.title("UVCE Percentage Calculator")

tk.Label(app, text="Select Cycle:").grid(row=0, column=0, padx=5, pady=5)

cycle_var = tk.StringVar()
tk.Radiobutton(app, text="P Cycle", variable=cycle_var, value="P Cycle").grid(row=0, column=1, padx=5, pady=5)
tk.Radiobutton(app, text="C Cycle", variable=cycle_var, value="C Cycle").grid(row=0, column=2, padx=5, pady=5)

frame = tk.Frame(app)
frame.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

tk.Label(frame, text="Subject").grid(row=0, column=0, padx=5, pady=5)
tk.Label(frame, text="Internal Marks").grid(row=0, column=1, padx=5, pady=5)
tk.Label(frame, text="Approximate Marks in Sem").grid(row=0, column=2, padx=5, pady=5)

media_int, media_sem = create_subject_row(frame, 1, "Media")
maths_int, maths_sem = create_subject_row(frame, 2, "Maths")
electrical_int, electrical_sem = create_subject_row(frame, 3, "Electrical")
physics_int, physics_sem = create_subject_row(frame, 4, "Physics")
physics_lab_int, physics_lab_sem = create_subject_row(frame, 5, "Physics Lab")
electrical_lab_int, electrical_lab_sem = create_subject_row(frame, 6, "Electrical Lab")
graphics_int, graphics_sem = create_subject_row(frame, 7, "Graphics")
mechanics_int, mechanics_sem = create_subject_row(frame, 8, "Mechanics")
english_int, english_sem = create_subject_row(frame, 9, "English")

tk.Button(app, text="Calculate SGPA", command=calculate_sgpa).grid(row=2, column=0, columnspan=3, padx=5, pady=5)

app.mainloop()
