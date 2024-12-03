import streamlit as st

# Save the data to the phonebook
def save():
    name = st.text_input("Enter Name:")
    contact_no = st.text_input("Enter Contact No:")
    email = st.text_input("Enter Email:")
    if st.button("Save"):
        with open("phonebook.txt", "a") as f:
            f.write(f"Name: {name}, Contact No: {contact_no}, Email: {email} \n")
        st.success("*****Data Saved Successfully*****")

# Fetch the saved data from phonebook
def retrieve():
    name = st.text_input("Enter name to find the data:")
    if st.button("Find"):
        with open("phonebook.txt", "r") as f:
            data = f.readlines()
        for item in data:
            if name.lower() in item.lower():
                st.success("*****Record Found:*****")
                st.write(item)

# The input menu of the phonebook
def menu():
    st.title("Phonebook App")
    choice = st.selectbox("Choose an option", ["Add new Contact", "Find a Contact", "Quit"])
    if choice == "Add new Contact":
        save()
    elif choice == "Find a Contact":
        retrieve()
    elif choice == "Quit":
        st.stop()

# Call to the menu from main
if __name__ == "__main__":
    menu()
