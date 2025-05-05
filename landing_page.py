# importing streamlit for web app
import streamlit as st

# creating page contents i.e. title, subheader, etc.
def show_landing_page():
    st.title("Welcome to the National Incubation Center Home Page!")
    st.subheader("Your one-stop solution for brainstorming startup ideas using generative AI.")
    st.write("Got a keyword or an idea? Let's help you turn it into a full startup concept using generative AI!")

    st.markdown("---")
    st.image("https://cdn-icons-png.flaticon.com/512/1533/1533904.png", width=150)

    st.markdown(
        """
        This tool helps you:
        - Brainstorm startup ideas
        - Get product descriptions
        - Understand possible target audiences
        - Suggest monetization strategies

        All you need is a keyword or theme. We'll do the rest.
        """
    )

    # Footer
    st.markdown(
        """
        <hr style="margin-top: 50px;"/>
        <div style="text-align: center; color: gray; font-size: 14px;">
            Created by: <strong>Faisal Abubakar</strong>
        </div>
        """,
        unsafe_allow_html=True
    )
