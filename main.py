import streamlit as st
import functions

todos = functions.get_todos()
checkbox_list = []
# streamlit needs to initialize keys before they're called
if 'user_input' not in st.session_state:
    st.session_state['user_input'] = ''

def add_todo():
    # session_state is a dictionary of sort, that contains events data etc
    todo = st.session_state['user_input'] + "\n"
    if todo != "\n":
        todos.append(todo)
    functions.write_todos(todos)

def remove_todo():
    for index, todo in enumerate(todos):
        cb_i = "cb_" + str(index)
        if st.session_state[cb_i]:
            todos.pop(index)
            functions.write_todos(todos)
            del st.session_state[cb_i]
            st.experimental_rerun()

st.title("My todo app")
st.subheader("WTH")
st.write("well...")

try:
    for index,todo in enumerate(todos):
        if todo != "" or todo != "\n":
            st.checkbox(todo, key="cb_"+str(index))
except:
    print("needs some input check")
    pass

st.text_input(label='user_entry',placeholder='Add a todo', label_visibility='hidden',
              key='user_input')
st.button(label="Add", key="add_todo", on_click=add_todo())
st.button(label="Completed", key="completed", on_click=remove_todo())

st.session_state