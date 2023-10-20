import streamlit as st

def main():
    st.title("Interview UI")

    # Your HTML code
    html_code = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #1A1A1A;
                color: white;
                margin: 0;
            }
            .container {
                display: flex;
                justify-content: space-between;
                padding: 50px;
                height: 100vh;
            }
            .left, .right {
                flex: 0.45;
            }
            .left ul {
                list-style-type: none;
                padding: 0;
            }
            .left li {
                background-color: #333;
                margin-bottom: 10px;
                padding: 10px;
                border-radius: 5px;
            }
            .right-content {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: space-between;
                height: 100%;
            }
            .circle {
                background-color: #333;
                border-radius: 50%;
                width: 300px;
                height: 300px;
            }
            .buttons {
                display: flex;
                gap: 10px;
            }
            button {
                padding: 10px;
                background-color: #555;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
            .topics {
                display: flex;
                flex-direction: column;
                gap: 10px;
                align-items: center;
                padding: 10px;
            }
            .topic {
                padding: 10px;
                background-color: #333;
                width: 150px;
                text-align: center;
                border-radius: 5px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="left">
                <ul>
                    <li>Homepage</li>
                    <li>Behavioral Screen</li>
                    <li>Professional Screen</li>
                    <li>Resume Screen</li>
                    <li>Test Screen</li>
                </ul>
            </div>
            <div class="right">
                <div class="right-content">
                    <h1>Interview UI</h1>
                    <div class="circle"></div>
                    <div class="topics">
                        <div class="topic">Topic 1</div>
                        <div class="topic">Topic 2</div>
                        <div class="topic">Topic 3</div>
                    </div>
                    <div class="buttons">
                        <button>Leave the interview</button>
                        <button>Skip the question</button>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

    # # Your CSS code
    # css_code = """
    # <style>
    #     /* Place the CSS code here */
    # </style>
    # """

    # Display HTML and CSS in Streamlit
    # st.markdown(css_code, unsafe_allow_html=True)
    st.markdown(html_code, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
