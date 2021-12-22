import streamlit as st
import pandas as pd

st.title("Student Enrollment Data")
save_data = st.button("Save")
df = pd.read_csv("cep.csv")
st.write(df)

st.sidebar.header("Enroll")
options_form = st.sidebar.form("options_form")
user_Name = options_form.text_input("Name")
user_ID = options_form.text_input("ID")
user_Department = options_form.text_input("Department")
add_data = options_form.form_submit_button()
if add_data:
    st.write(user_Name, user_ID, user_Department)
    new_data = {"Name": user_Name, "ID": int(user_ID), "Department": user_Department}
    df = df.append(new_data, ignore_index=True)
    result = df.sort_values('Department')
    result.to_csv("cep.csv", index=False)


