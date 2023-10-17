import streamlit as st

def main():
    st.title("Your App Title")

    # Placeholder for the large circle (You can replace this with an image or another widget)
    st.empty()

    # Display the time
    st.sidebar.text("Time: 15:03")

    # Topics with their corresponding labels
    topics = {
        "Топик 1": "User Research",
        "Топик 2": "Prototyping",
        "Топик 3": "Design Solution",
    }
    for topic, label in topics.items():
        st.sidebar.subheader(topic)
        st.sidebar.text(label)

    # "Leave the interview" and "Skip the question" buttons
    if st.sidebar.button("Leave the interview"):
        st.sidebar.text("You chose to leave the interview.")
    if st.sidebar.button("Skip the question"):
        st.sidebar.text("You chose to skip the question.")

    # Placeholder for "CC" and "Repeat the question" (Assuming they are buttons or icons)
    st.button("CC")
    st.button("Repeat the question")

if __name__ == "__main__":
    main()
