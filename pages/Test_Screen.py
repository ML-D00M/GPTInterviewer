import streamlit as st

# Sidebar content
st.sidebar.title("Homepage")
st.sidebar.text("Behavioral Screen")
st.sidebar.text("Professional Screen")
st.sidebar.text("Resume Screen")
st.sidebar.text("Test Screen")

st.sidebar.subheader("Time: 15:03")

# Topics checkboxes
st.sidebar.subheader("Topics")
st.sidebar.checkbox("Topic 1: User Research")
st.sidebar.checkbox("Topic 2: Prototyping")
st.sidebar.checkbox("Topic 3: Design Solution")

# Main content
st.title("UI Interface")

# Placeholder for the large oval shape
oval_placeholder = st.empty()

# Buttons at the bottom
st.text("")  # This is just to give some space
if st.button("Repeat the Question"):
    st.write("Repeating Question...")

if st.button("Leave the Interview"):
    st.write("Leaving Interview...")

if st.button("Skip the Question"):
    st.write("Skipping Question...")

# Drawing the oval using SVG (Scalable Vector Graphics) as a placeholder
oval_svg = """
<svg width="300" height="150">
    <ellipse cx="150" cy="75" rx="140" ry="70" style="fill:#E0E0E0;" />
</svg>
"""
oval_placeholder.markdown(oval_svg, unsafe_allow_html=True)
