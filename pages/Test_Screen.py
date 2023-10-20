import streamlit as st
from streamlit_option_menu import option_menu
from app_utils import switch_page
from PIL import Image

im = Image.open("icon.png")
st.set_page_config(page_title = "AI Interviewer", layout = "centered", page_icon=im)

lan = st.selectbox("#### Language", ["English", "Русский"])

if lan == "English":
    home_title = "AI Interviewer"
    home_introduction = "Welcome to AI Interviewer, empowering your interview preparation with generative AI."
    
    # The main screen content
    st.image(im, width=100)
    st.markdown(f"""# {home_title} <span style=color:#2E9BF5><font size=5>Beta</font></span>""", unsafe_allow_html=True)
    st.markdown("Welcome to AI Interviewer! 👏 AI Interviewer is your personal interviewer powered by generative AI that conducts mock interviews."
                "You can upload your resume and enter job descriptions, and AI Interviewer will ask you customized questions. Additionally, you can configure your own Interviewer!")
    st.markdown("#### Get started!")
    st.markdown("Select one of the following screens to start your interview!")
    
    # This is the code for the horizontal selection buttons
    selected = option_menu(
            menu_title= None,
            options=["Professional", "Resume", "Behavioral","Customize!"],
            icons = ["cast", "cloud-upload", "cast"],
            default_index=0,
            orientation="horizontal",
        )

    # ... [continue the rest of the logic for the selected options as in the provided code]

    st.markdown("#### Wiki")
    st.write('[Click here to view common FAQs, future updates and more!](https://jiatastic.notion.site/wiki-8d962051e57a48ccb304e920afa0c6a8?pvs=4)')

    # Now, we add the topics and time to the right of the main screen. For this example, I'll use placeholders.
    st.markdown("""
    <div style="float:right">
        <h3>Topics</h3>
        <ul>
            <li>Topic 1</li>
            <li>Topic 2</li>
            <li>Topic 3</li>
        </ul>
        <h3>Time</h3>
        <p>12:30 PM</p>
    </div>
    """, unsafe_allow_html=True)

    # Sidebar content
    with st.sidebar:
        st.markdown('AI Interviewer - V0.1.2')
        st.markdown(""" 
        #### Let's contact:
        [Haoxiang Jia](https://www.linkedin.com/in/haoxiang-jia/)
        
        [Zicheng Wang](https://www.linkedin.com/in/todd-wang-5001aa264/)
        #### Please fill the form, we'd love to have your feedback:
        [Feedback Form](https://docs.google.com/forms/d/13f4q03bk4lD7sKR7qZ8UM1lQDo6NhRaAKv7uIeXHEaQ/edit)
    
        #### Powered by
    
        [OpenAI](https://openai.com/)
    
        [FAISS](https://github.com/facebookresearch/faiss)
    
        [Langchain](https://github.com/hwchase17/langchain)
    
                    """)

    st.markdown(
        "<style>#MainMenu{visibility:hidden;}</style>",
        unsafe_allow_html=True
    )
