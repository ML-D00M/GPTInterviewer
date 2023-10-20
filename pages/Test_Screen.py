import streamlit as st

def main():
    st.title("UI Interface")
    
    # Central oval: Just representing with a placeholder for now
    st.markdown("<div style='background-color: grey; border-radius: 50%; width: 200px; height: 300px; margin: auto;'></div>", unsafe_allow_html=True)
    
    # Time Display
    st.sidebar.markdown("### Time: 15:03")
    
    # Topics in the sidebar
    st.sidebar.markdown("### Topics")
    topic1 = st.sidebar.checkbox("Topic 1: User Research")
    topic2 = st.sidebar.checkbox("Topic 2: Prototyping")
    topic3 = st.sidebar.checkbox("Topic 3: Design Solution")
    
    # If any topic is selected, show details (you can expand on this!)
    if topic1:
        st.write("Details about User Research...")
    elif topic2:
        st.write("Details about Prototyping...")
    elif topic3:
        st.write("Details about Design Solution...")
    
    # Buttons
    if st.button("Repeat the Question"):
        st.write("Repeating the question...")
    
    col1, col2, col3 = st.beta_columns(3)
    
    with col2:
        if st.button("Leave the Interview"):
            st.write("Exiting interview...")
            
    with col3:
        if st.button("Skip the Question"):
            st.write("Skipping to next question...")

if __name__ == "__main__":
    main()
