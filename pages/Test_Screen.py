import streamlit as st

def main():
    st.title("Interview UI")

    # Your HTML code
    html_code = """
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Design Mockup Implementation</title>
        <link rel="stylesheet" href="styles.css">
    </head>

    <body>
        <div class="container">
            <header>
                <h1>Interview UI</h1>
                <div class="time-indicator">Time: 15:03</div>
            </header>
            <div class="content">
                <div class="ellipse"></div>
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

    # Your CSS code
    css_code = """
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f6f6f6;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .container {
            background-color: white;
            border-radius: 10px;
            padding: 20px;
            width: 350px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        header {
            display: flex;
            justify-content: space-between;
            margin-bottom: 20px;
        }

        h1 {
            margin: 0;
            color: #333;
            font-size: 24px;
        }

        .time-indicator {
            font-size: 16px;
        }

        .content {
            display: flex;
            align-items: center;
        }

        .ellipse {
            background-color: lightgray;
            width: 150px;
            height: 150px;
            border-radius: 50%;
            margin-right: 30px;
        }

        .topics .topic {
            padding: 10px;
            background-color: white;
            color: black;
            margin: 10px 0;
            border: 1px solid lightgray;
            border-radius: 5px;
        }

        .topics .highlighted {
            background-color: #d0d0d0;
        }

        footer {
            margin-top: 20px;
        }

        .actions {
            display: flex;
            justify-content: space-between;
            margin-bottom: 10px;
        }

        .repeat-btn:before {
            content: '⏪';
            margin-right: 5px;
        }

        .footer-text {
            text-align: center;
            font-size: 12px;
            color: #888;
        }

    </style>
    """

    # Display HTML and CSS in Streamlit
    st.markdown(css_code, unsafe_allow_html=True)
    st.markdown(html_code, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
