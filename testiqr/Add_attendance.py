import pandas as pd
from datetime import datetime

class AddAttendance:
    def __init__(self, course_path):
        self._course_path = course_path
        self._id = None
        self._name = None
        self._today_date = datetime.now().strftime("%d.%m.%Y")
        self._today_time = datetime.now().strftime("%H.%M")
        #self.add_to_excel()

        def add_student(self,id, name):
            self._name = name
            self._id = id
            students_df = pd.read_csv('students.csv')

            new_student = pd.DataFrame({'id': [id], 'name': [name]})
            students_df = pd.concat([students_df, new_student], ignore_index=True)
            students_df.to_csv('students.csv', index=False)


    def get_name(self):
        return self._name



    def add_to_excel(self):
        try:
            attendance_df = pd.read_excel(self._course_path)

            #checks if there is a column for todays date
            if self._today_date not in attendance_df.columns:
                attendance_df[self._today_date] = pd.NaT


            # Check if the student ID already exists in the attendance data
            if self._id in attendance_df['ID'].values:
                # Update the attendance time for the specified student
                attendance_df.loc[attendance_df['ID'] == self._id, self._today_date] = str(self._today_time)
            else:
                # add a new record
                new_record = pd.DataFrame({'ID': [self._id], 'Name': [self._name], self._today_date: [str(self._today_time)]})
                attendance_df = pd.concat([attendance_df, new_record], ignore_index=True)

            # Save updated attendance data
            attendance_df.to_excel('attendance.xlsx', index=False)

        except FileNotFoundError:
            print(f"course file not found. course file: {self._course_path}")
        except pd.errors.ParserError:
            print("Error parsing to course file, ")
        except PermissionError:
            print(f"Permission error, make sure the excel file is closed when the application is on. excelfile: {self._course_path}")

#student = AddAttendance('C:/Users/Joni/Documents/kesaharkka/Attendance_system/testiqr/attendance.xlsx')