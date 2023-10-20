import streamlit as st

def main():
    st.title("Interview UI")

    # Create two columns for the UI layout
    col1, col2 = st.columns(2)

    # First Column (Left)
    with col1:
        # Draw an oval using a placeholder and markdown trick
        st.markdown(
            """
            <div style="background-color: #E0E0E0; height: 300px; border-radius: 150px;"></div>
            """, 
            unsafe_allow_html=True
        )
        
        # Buttons under the oval
        st.write("")  # Adding some spacing
        if st.button("CC"):
            st.write("You pressed 'CC' button.")
        
        if st.button("Repeat the question"):
            st.write("You pressed 'Repeat the question' button.")

    # Second Column (Right)
    with col2:
        # Displaying Time
        st.write("**Time:** 15.03")
        st.write("")  # Adding some spacing

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
        st.write("")  # Adding some spacing
        if st.button("Leave the interview"):
            st.write("You pressed 'Leave the interview' button.")
        
        if st.button("Skip the question"):
            st.write("You pressed 'Skip the question' button.")

if __name__ == "__main__":
    main()
