import pandas as pd
from datetime import datetime
import os

class AddAttendance:
    def __init__(self, course_path):
        self._course_path = course_path

        #checks if file exists and if not creates one
        if not os.path.exists(course_path):
            attendance_df = pd.DataFrame(columns=['ID', 'Name'])
            students_df = pd.DataFrame(columns=['ID', 'Name', 'Email'])
            with pd.ExcelWriter(course_path) as writer:
                attendance_df.to_excel(writer, sheet_name='Attendance', index=False)
                students_df.to_excel(writer, sheet_name='Students', index=False)

        self._today_date = None
        self._today_time = None
        #self.add_to_excel()

    #adds student to the csv file
    def add_student(self,id, name = None, email = None):
        students_df = pd.read_csv('C:/Users/OMISTAJA/Documents/kesaharkka/Attendance_system/testiqr/students.csv')
        row = students_df[students_df['id'] == id]
        if row.empty:
            new_student = pd.DataFrame({'id': [id], 'name': [name], 'email': [email]})
            students_df = pd.concat([students_df, new_student], ignore_index=True)
            students_df.to_csv('C:/Users/OMISTAJA/Documents/kesaharkka/Attendance_system/testiqr/students.csv', index=False)




    def get_name(self):
        return self._name


    #adds attendance to excel file
    def add_attendance(self, id):
        name = None
        students_df = pd.read_csv('C:/Users/OMISTAJA/Documents/kesaharkka/Attendance_system/testiqr/students.csv')
        row = students_df[students_df['id'] == id]
        if not row.empty:
            name = row.iloc[0]['name']
            email = row.iloc[0]['email']
        else:
            name = "Unknown"


        try:
            self._today_date = datetime.now().strftime("%d.%m.%Y")
            self._today_time = datetime.now().strftime("%H.%M")
            attendance_df = pd.read_excel(self._course_path, sheet_name="Attendance")
            # Check if there is a column for today's date
            if self._today_date not in attendance_df.columns:
                attendance_df[self._today_date] = pd.NaT

            # Check if the student ID already exists in the attendance data
            if id in attendance_df['ID'].values:
                # Update the attendance time for the specified student
                attendance_df.loc[attendance_df['ID'] == id, self._today_date] = str(self._today_time)
            else:
                # Add a new record
                new_record = pd.DataFrame({'ID': [id], 'Name': [name], self._today_date: [str(self._today_time)]})
                attendance_df = pd.concat([attendance_df, new_record], ignore_index=True)

            # Save updated attendance data back to the same file
            with pd.ExcelWriter(self._course_path, mode='a', if_sheet_exists='overlay') as writer:
                attendance_df.to_excel(writer, sheet_name="Attendance", index=False)


        except FileNotFoundError:
            print(f"course file not found. course file: {self._course_path}")
        except pd.errors.ParserError:
            print("Error parsing to course file, ")
        except PermissionError:
            print(f"Permission error, make sure the excel file is closed when the application is on. excelfile: {self._course_path}")

        students_df = pd.read_excel(self._course_path, sheet_name="Students")
        if id not in students_df['ID'].values:
            new_record = pd.DataFrame({'ID': [id], 'Name': [name], 'Email': [email]})
            students_df = pd.concat([students_df, new_record], ignore_index=True)

            with pd.ExcelWriter(self._course_path, mode='a', if_sheet_exists='overlay') as writer:
                students_df.to_excel(writer, sheet_name="Students", index=False)

student = AddAttendance('C:/Users/OMISTAJA/Documents/kesaharkka/Attendance_system/testiqr/attendance.xlsx')
student.add_student(1,'kalle')
student.add_attendance(1)
