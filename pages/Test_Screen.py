import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def main():
    st.title("Interview UI")

    # Text input widget
    user_input = st.text_input("Enter some text:")

    # Data slider example
    number = st.slider("Select a number:", 1, 100)

    # Button to display a message
    if st.button("Click Me"):
        st.write("Button was clicked!")

    # Dynamic insertion of the user input and selected number into the ellipse
    ellipse_content = f"{user_input} {number}"

    # Your HTML code with the dynamic ellipse content
    html_code = f"""
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Design Mockup Implementation</title>
    </head>

    <body>
        <div class="container">
            <header>
                <h1>Interview UI</h1>
                <div class="time-indicator">Time: 15:03</div>
            </header>
            <div class="content">
                <div class="ellipse">{ellipse_content}</div>
                <div class="topics">
                    <div class="topic">User Research</div>
                    <div class="topic highlighted">Prototyping</div>
                    <div class="topic">Design Solution</div>
                </div>
            </div>
            <footer>
                <div class="actions">
                    <button class="repeat-btn">Repeat the question</button>
                    <button>Leave the interview</button>
                    <button>Skip the question →</button>
                </div>
                <div class="footer-text">Made with Streamlit</div>
            </footer>
        </div>
    </body>

    </html>
    """

    # Your CSS code (unchanged as there's no need for any modifications)
    css_code = """
    <style>
        /* ... [The rest of your CSS code remains unchanged] ... */
    </style>
    """

    # Display HTML and CSS in Streamlit
    st.markdown(css_code, unsafe_allow_html=True)
    st.markdown(html_code, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
