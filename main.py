import streamlit as sl
import functions

todos = functions.get_todos()

sl.title("My todo app")
sl.subheader("WTH")
sl.write("well...")

for todo in todos:
    sl.checkbox(todo)

sl.text_input(label="user_entry",placeholder="Add a todo", label_visibility="hidden")