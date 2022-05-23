import mysqlx
import streamlit as st

import mysql.connector as connection

import pandas as pd

mydb = connection.connect(host=st.secrets["host"], database = st.secrets["database"],user=st.secrets["user"], passwd=st.secrets["password"])

cur= mydb.cursor(buffered=True)
from datetime import datetime

timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def addData(a,b,c,d):
    
    cur.execute("""CREATE TABLE if not exists MyComfort_dataset (date_time  datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
    Location VARCHAR(50),Seat_Number int, Thermal_Sensation VARCHAR(50));""")
    cur.execute("INSERT INTO MyComfort_dataset VALUES(%s,%s,%s,%s);",( a,b,c,d))
    mydb.commit()
    mydb.close()
    st.success('Submission Success! ')

def form():  
    st.header('HVAC Request Interface')
    st.write('Raise Your Request Here')
  
    with st.form(key='Info form'):
        
        Location=st.selectbox('Office Location', ['Phase 1', 'Phase 2','Central block'])
        
        Thermal_Sensation=st.selectbox('Your Current thermal Sensation ?', ['Too Cool', 'Cool','Slightly cool',
        'Just fine','Slightly warm','Hot','Too Hot'])
        Seat_Number=st.number_input(label='Seat Number',min_value=1,max_value=50)        
        
        submission=st.form_submit_button(label='Submit')
        Date_time=timestamp
        
        if submission==True:
            addData(Date_time,Location,Seat_Number,Thermal_Sensation)
            





form()
