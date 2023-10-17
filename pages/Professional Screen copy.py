import streamlit as st

def main():
    st.title("Mockup Implementation")

    # Large Oval - Placeholder for Image/Video
    st.image("/workspaces/GPTInterviewer/static/images/ai_icon.png", use_column_width=True)  # Placeholder for an image
    
    # Information Panel on the Right
    col1, col2, col3 = st.beta_columns([1,2,1])
    
    with col2:
        # Time
        st.subheader("Time: 15:03")
        
        # Topics
        st.write("**Topic 1**: User Research")
        st.write("**Topic 2**: Prototyping")
        st.write("**Topic 3**: Design Solution")

    # Bottom buttons
    st.button("Repeat the question")
    st.button("Leave the interview")
    st.button("Skip the question")

if __name__ == '__main__':
    main()
