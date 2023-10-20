import streamlit as st

def main():
    st.title("Interview UI")

    # Displaying Time
    st.write("**Time:** 15.03")

    # Displaying Topics
    topics = [
        ("Topic 1", "User Research"),
        ("Topic 2", "Prototyping"),
        ("Topic 3", "Design Solution")
    ]

    for topic_name, topic_description in topics:
        st.write(f"**{topic_name}**")
        st.write(topic_description)
        st.write("---")  # adding a horizontal line for separation

    # Displaying Buttons
    if st.button("Repeat the question"):
        st.write("You pressed 'Repeat the question' button.")
    
    if st.button("Leave the interview"):
        st.write("You pressed 'Leave the interview' button.")
    
    if st.button("Skip the question"):
        st.write("You pressed 'Skip the question' button.")

if __name__ == "__main__":
    main()
