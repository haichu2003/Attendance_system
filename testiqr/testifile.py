import csv
import os
import pandas as pd
from datetime import datetime
from tkinter import *
from tkinter import ttk


def check_attendance(course_name, student_id):
    # Get today's date in "dd.mm" format
    today_date = datetime.now().strftime("%d.%m")
    today_time = datetime.now().strftime("%H.%M")

    # Check if course file exists
    if not os.path.exists(f"{course_name}.csv"):
        print(f"Course '{course_name}' does not exist.")
        return

    # Check if student file exists
    if not os.path.exists("student.csv"):
        print("Student file does not exist.")
        return

    # Read student file
    with open("student.csv", "r") as student_file:
        student_reader = csv.reader(student_file)
        student_data = list(student_reader)

    # Check if student exists
    student_exists = False
    student_name = ""
    for row in student_data:
        if row[0] == student_id:
            student_exists = True
            student_name = row[1]
            break

    if not student_exists:
        student_name = input("Enter student name: ")
        # Add new student to student file
        with open("student.csv", "a", newline='') as student_file:
            student_writer = csv.writer(student_file)
            student_writer.writerow([student_id, student_name])

    # Check if attendance file exists, if not create it with headers
    attendance_filename = f"{course_name}.csv"
    if not os.path.exists(attendance_filename):
        with open(attendance_filename, "w", newline='') as attendance_file:
            attendance_writer = csv.writer(attendance_file)
            attendance_writer.writerow(["ID", "Name", "Date"])

    # Read attendance file
    with open(attendance_filename, "r") as attendance_file:
        attendance_reader = csv.DictReader(attendance_file)
        attendance_data = list(attendance_reader)

    # Check if student attendance exists for today
    student_attendance_exists = False
    for row in attendance_data:
        if row['ID'] == student_id:
            student_attendance_exists = True
            break

    if not student_attendance_exists:
        # Record student attendance for today
        with open(attendance_filename, "a", newline='') as attendance_file:
            attendance_writer = csv.writer(attendance_file)

            # If the attendance file is empty, write the headers including today's date
            if os.path.getsize(attendance_filename) == 0:
                attendance_writer.writerow(["ID", "Name", today_date])
                attendance_writer.writerow([student_id, student_name, today_time])
            else:
                # If the attendance file already has headers, append student attendance for today
                attendance_writer.writerow([student_id, student_name, today_time])
        print("Attendance recorded for", today_date)
    else:
        print("Student has already been marked present for today.")


course_name = "course-name"
student_id = input("Enter student ID: ")
check_attendance(course_name, student_id)
