import streamlit as st
import cg2
import crosswind

# Define the main Streamlit app


def main_app():
    # Set the app title
    st.title("Aviation Tools")

    # Create a menu with options for running cg2.py or crosswind.py
    menu = ["CG Calculator", "Crosswind Component Calculator"]
    choice = st.sidebar.selectbox("Select an aviation tool", menu)

    # Show the appropriate app based on the user's choice
    if choice == "CG Calculator":
        cg2.app()
    elif choice == "Crosswind Component Calculator":
        crosswind.app()


# Run the main Streamlit app
if __name__ == '__main__':
    main_app()
