import streamlit as st
import functions

todos = functions.get_todos("todos.txt")


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos, "todos.txt")


todos = functions.get_todos("todos.txt")

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos, "todos.txt")

        # del here will delete the key pair from the session state dictionary
        # so that that now irrelevant info is gone
        del st.session_state[todo]

        # this will rerun the code "This is necessary for checkboxes"
        st.rerun()


st.text_input(label=" ", placeholder="Add a new todo...",
              on_change=add_todo, key="new_todo")

st.session_state
