import streamlit as st
from streamlit_option_menu import option_menu
from app_utils import switch_page
import streamlit as st
from PIL import Image

im = Image.open("icon.png")
st.set_page_config(page_title = "AI Interviewer", layout = "centered",page_icon=im)

lan = st.selectbox("#### Language", ["English", "Русский"])

if lan == "English":
    home_title = "AI Interviewer"
    home_introduction = "Welcome to AI Interviewer, empowering your interview preparation with generative AI."
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
    st.image(im, width=100)
    st.markdown(f"""# {home_title} <span style=color:#2E9BF5><font size=5>Beta</font></span>""",unsafe_allow_html=True)
    st.markdown("""\n""")
    #st.markdown("#### Greetings")
    st.markdown("Welcome to AI Interviewer! 👏 AI Interviewer is your personal interviewer powered by generative AI that conducts mock interviews."
                "You can upload your resume and enter job descriptions, and AI Interviewer will ask you customized questions. Additionally, you can configure your own Interviewer!")
    st.markdown("""\n""")
    # with st.expander("Updates"):
    #     st.write("""
    #     08/13/2023
    #     - Fix the error that occurs when the user input fails to be recorded. """)
    # with st.expander("What's coming next?"):
    #     st.write("""
    #     Improved voice interaction for a seamless experience. """)
    st.markdown("""\n""")
    st.markdown("#### Get started!")
    st.markdown("Select one of the following screens to start your interview!")
    selected = option_menu(
            menu_title= None,
            options=["Professional", "Resume", "Behavioral","Customize!"],
            icons = ["cast", "cloud-upload", "cast"],
            default_index=0,
            orientation="horizontal",
        )
    if selected == 'Professional':
        st.info("""
            📚In this session, the AI Interviewer will assess your technical skills as they relate to the job description.
            Note: The maximum length of your answer is 4097 tokens!
            - Each Interview will take 10 to 15 mins.
            - To start a new session, just refresh the page.
            - Choose your favorite interaction style (chat/voice)
            - Start introduce yourself and enjoy！ """)
        if st.button("Start Interview!"):
            switch_page("Professional Screen")
    if selected == 'Resume':
        st.info("""
        📚In this session, the AI Interviewer will review your resume and discuss your past experiences.
        Note: The maximum length of your answer is 4097 tokens!
        - Each Interview will take 10 to 15 mins.
        - To start a new session, just refresh the page.
        - Choose your favorite interaction style (chat/voice)
        - Start introduce yourself and enjoy！ """
        )
        if st.button("Start Interview!"):
            switch_page("Resume Screen")
    if selected == 'Behavioral':
        st.info("""
        📚In this session, the AI Interviewer will assess your soft skills as they relate to the job description.
        Note: The maximum length of your answer is 4097 tokens!
        - Each Interview will take 10 to 15 mins.
        - To start a new session, just refresh the page.
        - Choose your favorite interaction style (chat/voice)
        - Start introduce yourself and enjoy！ 
        """)
        if st.button("Start Interview!"):
            switch_page("Behavioral Screen")
    if selected == 'Customize!':
        st.info("""
            📚In this session, you can customize your own AI Interviewer and practice with it!
             - Configure AI Interviewer in different specialties.
             - Configure AI Interviewer in different personalities.
             - Different tones of voice.
             
             Coming at the end of July""")
    st.markdown("""\n""")
    st.markdown("#### Wiki")
    st.write('[Click here to view common FAQs, future updates and more!](https://jiatastic.notion.site/wiki-8d962051e57a48ccb304e920afa0c6a8?pvs=4)')
    #st.write(
    #        f'<iframe src="https://17nxkr0j95z3vy.embednotionpage.com/AI-Interviewer-Wiki-8d962051e57a48ccb304e920afa0c6a8" style="width:100%; height:100%; min-height:500px; border:0; padding:0;"/>',
    #        unsafe_allow_html=True,
    #    )

if lan == 'Русский': 
    home_title = "AI Интервьюер"
    home_introduction = "Добро пожаловать в AI Интервьюер, помогая вам подготовиться к интервью с помощью генеративного AI."
    with st.sidebar:
        st.markdown('AI Интервьюер - V0.1.2')
        st.markdown(""" 
            #### Свяжитесь с нами:
            [Хаосян Джа](https://www.linkedin.com/in/haoxiang-jia/)

            [Цзычэн Ван](https://www.linkedin.com/in/todd-wang-5001aa264/)
            #### Пожалуйста, заполните форму, мы будем рады получить ваш отзыв:
            [Форма обратной связи](https://docs.google.com/forms/d/13f4q03bk4lD7sKR7qZ8UM1lQDo6NhRaAKv7uIeXHEaQ/edit)

            #### Работает на технологиях:

            [OpenAI](https://openai.com/)

            [FAISS](https://github.com/facebookresearch/faiss)

            [Langchain](https://github.com/hwchase17/langchain)

                        """)
    st.markdown(
        "<style>#MainMenu{visibility:hidden;}</style>",
        unsafe_allow_html=True
    )
    st.image(im, width=100)
    st.markdown(f"""# {home_title} <span style=color:#2E9BF5><font size=5>Beta</font></span>""", unsafe_allow_html=True)

    st.markdown("""\n""")
    st.markdown(
        "Добро пожаловать в AI Интервьюер! 👏 AI Интервьюер - это ваш личный интервьюер, работающий на генеративном AI, который проводит тренировочные интервью. "
        "Вы можете загрузить свое резюме и ввести описание рабочих вакансий, и AI Интервьюер задаст вам индивидуальные вопросы. Кроме того, вы можете настроить своего Интервьюера!")
    st.markdown("""\n""")
    # with st.expander("Журнал обновлений"):
    #     st.write("""
    #         08/13/2023
    #         - Исправлена ошибка, возникающая при сбое записи пользовательского ввода. """)
    # with st.expander("Что дальше?"):
    #     st.write("""
    #         Улучшенное голосовое взаимодействие для бесшовного опыта. """)
    st.markdown("""\n""")
    st.markdown("#### Давайте начнем!")
    st.markdown("Выберите один из следующих экранов, чтобы начать интервью!")
    selected = option_menu(
        menu_title=None,
        options=["Профессиональное", "Резюме", "Поведенческое", "Настройка!"],
        icons=["cast", "cloud-upload", "cast"],
        default_index=0,
        orientation="horizontal",
    )
    if selected == 'Профессиональное':
        st.info("""
                📚В этой сессии AI Интервьюер оценит ваши технические навыки в соответствии с описанием вакансии.
                Примечание: Максимальная длина вашего ответа составляет 4097 токенов!
                - Каждое интервью займет от 10 до 15 минут.
                - Чтобы начать новую сессию, просто обновите страницу.
                - Выберите свой любимый стиль взаимодействия (чат/голос)
                - Начните представлять себя и наслаждайтесь! """)
        if st.button("Начать интервью!"):
            switch_page("Professional Screen")
    if selected == 'Резюме':
        st.info("""
                📚В этой сессии AI Интервьюер рассмотрит ваше резюме и обсудит ваши прошлые опыты.
                Примечание: Максимальная длина вашего ответа составляет 4097 токенов!
                - Каждое интервью займет от 10 до 15 минут.
                - Чтобы начать новую сессию, просто обновите страницу.
                - Выберите свой любимый стиль взаимодействия (чат/голос)
                - Начните представлять себя и наслаждайтесь! """)
        if st.button("Начать интервью!"):
            switch_page("Resume Screen")
    if selected == 'Поведенческое':
        st.info("""
            📚В этой сессии AI Интервьюер оценит ваши мягкие навыки в соответствии с описанием вакансии.
            Примечание: Максимальная длина вашего ответа составляет 4097 токенов!
            - Каждое интервью займет от 10 до 15 минут.
            - Чтобы начать новую сессию, просто обновите страницу.
            - Выберите свой любимый стиль взаимодействия (чат/голос)
            - Начните представлять себя и наслаждайтесь! 
            """)
        if st.button("Начать интервью!"):
            switch_page("Behavioral Screen")
    st.markdown("""\n""")
    st.markdown("#### Вики")
    st.write(
        '[Нажмите здесь, чтобы просмотреть часто задаваемые вопросы, будущие обновления и многое другое!](https://jiatastic.notion.site/wiki-8d962051e57a48ccb304e920afa0c6a8?pvs=4)')



# if lan ==  '中文':
#     home_title = "AI面试官"
#     home_introduction = "欢迎使用 AI 面试官，它能够通过生成式AI帮助您准备面试。"
#     with st.sidebar:
#         st.markdown('AI面试管 - V0.1.2')
#         st.markdown(""" 
#             #### 领英:
#             [贾皓翔](https://www.linkedin.com/in/haoxiang-jia/)

#             [王梓丞](https://www.linkedin.com/in/todd-wang-5001aa264/)
#             #### 请填写表格，我们非常希望听到您的反馈：
#             [Feedback Form](https://docs.google.com/forms/d/13f4q03bk4lD7sKR7qZ8UM1lQDo6NhRaAKv7uIeXHEaQ/edit)

#             #### 使用的技术：

#             [OpenAI](https://openai.com/)

#             [FAISS](https://github.com/facebookresearch/faiss)

#             [Langchain](https://github.com/hwchase17/langchain)

#                         """)
#     st.markdown(
#         "<style>#MainMenu{visibility:hidden;}</style>",
#         unsafe_allow_html=True
#     )
#     st.image(im, width=100)
#     st.markdown(f"""# {home_title} <span style=color:#2E9BF5><font size=5>Beta</font></span>""", unsafe_allow_html=True)

#     st.markdown("""\n""")
#     # st.markdown("#### Greetings")
#     st.markdown(
#         "欢迎使用AI面试官！👏AI面试官是一款由生成式人工智能驱动的个人面试官，可以进行模拟面试。您可以上传您的简历或者复制粘贴工作描述，AI面试官会根据您的情况提出定制化的问题。"
#     )
#     st.markdown("""\n""")
#     with st.expander("更新日志"):
#         st.write("""
#             08/13/2023
#             - 修复了当用户输入失败时的报错问题 """)
#     with st.expander("未来计划"):
#         st.write("""
#             - 提供更加稳定和快速的语音交互
#             - 支持全中文的模拟面试 """)
#     st.markdown("""\n""")
#     st.markdown("#### 让我们开始吧!")
#     st.markdown("请选择以下其中一个开始您的面试！")
#     selected = option_menu(
#         menu_title=None,
#         options=["专业评估", "简历评估", "行为评估"],
#         icons=["cast", "cloud-upload", "cast"],
#         default_index=0,
#         orientation="horizontal",
#     )
#     if selected == '专业评估':
#         st.info("""
#                 📚在本次面试中，AI面试官将会根据职位描述评估您的技术能力。
#                 注意: 您回答的最大长度为4097个tokens!
#                 - 每次面试将会持续10到15分钟。
#                 - 您可以通过刷新页面来开始新的面试。
#                 - 您可以选择您喜欢的交互方式(文字/语音)
#                 - 开始介绍您自己吧！ """)
#         if st.button("开始面试!"):
#             switch_page("Professional Screen")
#     if selected == '简历评估':
#         st.info("""
#                 📚在本次面试中，AI面试官将会根据您的简历评估您的过往经历。
#                 注意: 您回答的最大长度为4097个tokens!
#                 - 每次面试将会持续10到15分钟。
#                 - 您可以通过刷新页面来开始新的面试。
#                 - 您可以选择您喜欢的交互方式(文字/语音)
#                 - 开始介绍您自己吧！ """)
#         if st.button("开始面试!"):
#             switch_page("Resume Screen")
#     if selected == '行为评估':
#         st.info("""
#             📚在本次面试中，AI面试官将会根据您的简历评估您的技术能力。
#             注意: 您回答的最大长度为4097个tokens!
#             - 每次面试将会持续10到15分钟。
#             - 您可以通过刷新页面来开始新的面试。
#             - 您可以选择您喜欢的交互方式(文字/语音)
#             - 开始介绍您自己吧！ """)
#         if st.button("开始面试!"):
#             switch_page("Behavioral Screen")
#     st.markdown("""\n""")
#     st.markdown("#### 维基")
#     st.write(
#         '[点击查看常见问题，更新和计划！](https://jiatastic.notion.site/wiki-8d962051e57a48ccb304e920afa0c6a8?pvs=4)')