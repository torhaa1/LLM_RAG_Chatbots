import streamlit as st # quick and easy web app
import langchain_helper # function to generate restaurant name and menu items

# Title
st.title("Restaurant Name Generator")

# Selection in sidebar
cusine = st.sidebar.selectbox("Select a cuisine", ["Chinese", "Italian", "Mexican", "American", "Japanese"])

if cusine:
    # Generate the restaurant name and menu items
    response = langchain_helper.generate_restaurant_name_and_menu_items(cusine)
    menu_items = response['menu_items'].strip().split(",")

    # Display the restaurant name
    st.header(response['restaurant_name'].strip().replace('"', ''))

    # Display the menu items
    st.write("#### **Menu Items:**")
    for item in menu_items:
        st.write(item)

# in terminal: streamlit run main.py