# -UVCE-SGPA-Calculator
A basic Python application for U.V.C.E. students to calculate SGPA from internal and expected external marks. Currently for 1st-year P Cycle students, in the building phase.



---

# **UVCE SGPA Calculator**

## **Overview**

**UVCE SGPA Calculator** is a simple Python application designed specifically for U.V.C.E. (University Visvesvaraya College of Engineering) 1st-year P Cycle students. This tool calculates the Semester Grade Point Average (SGPA) based on internal marks and expected external marks. The application is currently in the building phase and aims to help students manage and track their academic performance effectively.

## **Features**

- **SGPA Calculation:** Compute SGPA from internal and expected external marks for various subjects.
- **Subject Management:** Supports input for multiple subjects including Media, Maths, Electrical, Physics, and more.
- **Failing Subjects:** Identifies any subjects where the student has failed based on their marks.
- **User-Friendly Interface:** Simple and intuitive graphical user interface (GUI) using Tkinter.
- **Performance Tracking:** Helps students monitor their academic progress and plan for improvement.




## **Usage**

To run the **UVCE SGPA Calculator**, follow these steps:

### **1. Launch the Application**

Run the main script using the following command:

```bash
python main.py
```

### **2. Input Marks**

- Select the cycle (P Cycle or C Cycle).
- Enter the internal marks and approximate semester marks for each subject.
- Click the "Calculate SGPA" button to compute the SGPA and see any failed subjects.

### **3. View Results**

A message box will display the computed SGPA and a list of any subjects in which you have failed.

## **Example Usage**

1. **Select Cycle:** Choose "P Cycle" 
2. **Enter Marks:** Fill in internal and semester marks for all subjects.
3. **Calculate SGPA:** Click the "Calculate SGPA" button.
4. **View SGPA:** The SGPA result will be displayed along with any failing subjects.

## **Code Structure**

Here’s a brief overview of the code structure:

- `main.py`: Main script to launch the application.
- `calculate_sgpa()`: Function to compute SGPA based on internal and semester marks.
- `create_subject_row()`: Helper function to create input fields for subjects.
- `app` Variable: Tkinter window and widgets setup.


## **Acknowledgements**

- **Tkinter:** The standard Python interface to the Tk GUI toolkit.
- **U.V.C.E. Community:** Inspiration for creating a tool tailored to the needs of 1st-year P Cycle students.




