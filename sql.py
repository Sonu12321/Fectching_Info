from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GEMINI_KEY"))

def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt, question])
    return response[0]['generated_text']  # Ensure this is the correct way to get the text from response

def read_sql(sql, db):
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        conn.close()
        return rows
    except Exception as e:
        print(f"Error: {e}")
        return []

# Prompt for the generative AI
prompt = '''
you are an expert in converting the SQL question in code language. The SQL database has the name 'student' with the following columns: name, class, section. After that, when the question is asked about how many counts are there, just return 'select count(*) from student'.
'''

# Streamlit app configuration
st.set_page_config(page_title="I can retrieve any query")
st.header('Gemini App to Retrieve')

question = st.text_input("Input: ", key='input')
submit = st.button("Ask the question")

if submit:
    response = get_gemini_response(question, prompt)
    rows = read_sql(response, 'student.db')
    st.subheader("Response is:")
    for row in rows:
        st.write(row)
