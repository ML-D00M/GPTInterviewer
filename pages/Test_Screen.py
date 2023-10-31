import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Interview UI Test Screen",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)


def main():
    # st.title("Interview UI")

    # # Text input widget
    # user_input = st.text_input("Enter some text:")

    # # Data slider example
    # number = st.slider("Select a number:", 1, 100)

    # # Button to display a message
    # if st.button("Click Me"):
    #     st.write("Button was clicked!")

    # # Dynamic insertion of the user input and selected number into the ellipse
    # ellipse_content = f"{user_input} {number}"

   # Your CSS code (unchanged as there's no need for any modifications)
    css_code = """
    <style>
        :root {
        --color-black: #000000;
        --color-white: #FFFFFF;
        --color-grey: #767676;
        --color-grey-light: #D9D9D9;
        }

        * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        font-family: Arial, Helvetica, sans-serif;
        }

        h5 {
        font-weight: 400;
        }

        .wrapper {
        min-height: 100vh;
        display: flex;
        flex-direction: column;
        }

        .header {
        height: 3.3125rem;
        background: var(--color-grey-light);
        }

        .button {
        border: none;
        padding: 1.06rem 1.75rem;
        border-radius: 1rem;
        background: var(--color-grey);
        color: var(--color-white);
        font-size: 1rem;
        cursor: pointer;
        transition: background-color 250ms;
        }

        .buttons {
        display: flex;
        flex-wrap: wrap;
        gap: 1.06rem 0.81rem;
        }

        .content {
        flex-grow: 1;
        display: flex;
        align-items: center;
        justify-content: space-around;
        }

        .left {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 2.44rem;
        }

        .thing {
        width: 25.25rem;
        height: 32.8125rem;
        border-radius: 12.625rem;
        background: var(--color-grey-light);
        }

        .right {
        max-width: 25rem;
        }

        .time {
        font-size: 1rem;
        opacity: 0.5;
        color: var(--color-black);
        margin-bottom: 2.75rem;
        }

        .cards {
        margin-bottom: 2.5rem;
        }

        .card {
        padding: 1.06rem 1.31rem;
        margin-bottom: 1.06rem;
        }

        .card:last-child {
        margin-bottom: 0;
        }

        .card:nth-child(odd) {
        background: var(--color-grey-light);
        }

        .card:nth-child(even) {
        background: var(--color-grey);
        }

        .card__title, .card__text {
        color: var(--color-white);
        font-size: 1rem;
        }

        .card__title {
        margin-bottom: 1.44rem;
        }
    </style>
    """

    # Your HTML code with the dynamic ellipse content
    html_code = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    </head>
    <body>
    <div class="wrapper">
        <header class="header">
        </header>
        <main class="content">
        <div class="left">
            <div class="thing">
            </div>
            <div class="buttons">
            <button class="button">
                CC
            </button>
            <button class="button">
                Repeat the question
            </button>
            </div>
        </div>
        <div class="right">
            <div class="time">Time: 15.03</div>
            <div class="cards">
                <div class="card">
                <h5 class="card__title">Топик 1</h5>
                <p class="card__text">User Research</p>
                </div>
                <div class="card">
                <h5 class="card__title">Топик 2 </h5>
                <p class="card__text">Prototyping</p>
                </div>
                <div class="card">
                <h5 class="card__title">Топик 3</h5>
                <p class="card__text">Design Solution</p>
                </div>
            </div>
            <div class="buttons">
                <button class="button">
                Leave the interview
                </button>
                <button class="button">
                Skip the question
                </button>
                <button class="button">
                One more question in this topic
                </button>
            </div>
            </div>
        </div>
        </main>
    </div>
    </body>
    </html>
    """


    # Display HTML and CSS in Streamlit
    st.markdown(css_code, unsafe_allow_html=True)
    st.markdown(html_code, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
