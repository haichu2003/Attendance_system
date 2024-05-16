import pandas as pd
from datetime import datetime

class AddAttendance:
    def __init__(self, id, course_path):
        self._course_path = course_path
        self._id = id
        self._name = None
        self._today_date = datetime.now().strftime("%d.%m.%Y")
        self._today_time = datetime.now().strftime("%H.%M")
        self._load_student_data()
        self.add_to_excel()

        def add_student(self,id, name):
            self._name = name
            
            students_df = pd.read_csv('students.csv')

            new_student = pd.DataFrame({'id': [id], 'name': [name]})
            students_df = pd.concat([students_df, new_student], ignore_index=True)
            students_df.to_csv('students.csv', index=False)

    def _load_student_data(self):
        #need to add path to csv
        students_df = pd.read_csv('students.csv')
        row = students_df[students_df['id'] == self._id]
        if not row.empty:
            self._name = row.iloc[0]['name']
        else:
            #to ask id
            self._name = 'kalle'

    def get_name(self):
        return self._name

    

    def add_to_excel(self):
        try: 
            # Need to add path to excel    
            attendance_df = pd.read_excel(self._course_path)
            if self._today_date not in attendance_df.columns:
                attendance_df[self._today_date] = pd.NaT

            
            # Check if the student ID already exists in the attendance data
            if self._id in attendance_df['ID'].values:
                # Update the attendance time for the specified student
                attendance_df.loc[attendance_df['ID'] == self._id, self._today_date] = str(self._today_time)
            else:
                # add a new record
                new_record = pd.DataFrame({'ID': [self._id], 'Name': [self._name], self._today_date: [self._today_time]})
                attendance_df = pd.concat([attendance_df, new_record], ignore_index=True)
            
            # Save updated attendance data
            attendance_df.to_excel('attendance.xlsx', index=False)

        except FileNotFoundError:
            print("course file not found.")
        except pd.errors.ParserError:
            print("Error parsing course file.")

student = AddAttendance(2, 'C:/Users/Joni/Documents/kesaharkka/Attendance_system/testiqr/attendance.xlsx')
print("Name:", student.get_name())