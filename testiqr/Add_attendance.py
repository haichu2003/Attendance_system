import pandas as pd
from datetime import datetime

class AddAttendance:
    def __init__(self, id):
        self._id = id
        self._name = None
        self._today_date = datetime.now().strftime("%d.%m")
        self._today_time = datetime.now().strftime("%H.%M")
        self._load_student_data()
        self.add_to_excel()


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

    def get_timestamp(self):
        return self._datetime
    
    def set_timestamp(self):
        self._datetime = datetime.now()
    

    def add_to_excel(self):
        #need to add path to excel    
        attendance_df = pd.read_excel('attendance.xlsx')
        if self._today_date not in attendance_df.columns:
            attendance_df[self._today_date] = pd.NaT
        attendance_df.loc[attendance_df['ID'] == self._id, self._today_date] = pd.to_datetime(attendance_df.loc[attendance_df['ID'] == self._id, self._today_date].dt.date.astype(str) + ' ' + self._today_time)
        new_record = pd.DataFrame({'ID': [self._id], 'Name': [self._name], self._today_date: [self._today_time]})
        attendance_df = pd.concat([attendance_df, new_record], ignore_index=True)
        attendance_df.to_excel('attendance.xlsx', index=False)

student = AddAttendance(1)
print("Name:", student.get_name())