# importing required dependencies
import streamlit as st
import google.generativeai as genai

# Load Gemini API key from Streamlit secrets
API_KEY = st.secrets["GEMINI_API_KEY"]

# Configuring Gemini client
genai.configure(api_key=API_KEY)

# Load Gemini 1.5 Flash model
model = genai.GenerativeModel("models/gemini-1.5-flash")

# creating function to generate startup idea with error handling
def generate_startup_idea(prompt_text):
    try:
        response = model.generate_content(prompt_text)
        return response.text
    except Exception as e:
        st.error(f"Generation failed: {e}")
        return None

# Function to generate when Enter is pressed instead button
def trigger_generation():
    st.session_state.generate = True

# creating function to show startup generator page
def show_startup_generator_page():
    st.title("💡 Start-Up Idea Generator")

    # setting default prompt
    st.text_input(
        "Enter a few keywords or themes:",
        "AI, data-engineering, supply chain, automation, ...",
        key="keywords",
        on_change=trigger_generation
    )

    # when user presses Enter, it will trigger the generation
    if st.button("Generate Idea"):
        st.session_state.generate = True

    # asking user to enter keywords when nothing is entered or proceed onwards
    if st.session_state.get("generate"):
        keywords = st.session_state.get("keywords", "").strip()
        if not keywords:
            st.error("Please type anything in your mind to spark your startup vision!")
        else:
            with st.spinner("Thinking..."):
                # ensuring a well detailed and well structured startup plan
                prompt = f"""
Generate a detailed startup plan based on the following themes: {keywords}.

The plan should include:
1. Startup Name
2. Problem Statement
3. Proposed Solution
4. Target Market
5. Revenue Model
6. Go-to-Market Strategy
7. Technology Stack
8. Competitive Advantage
9. Potential Challenges
10. Future Vision

Make it neatly formatted and easy to read.
"""
                idea = generate_startup_idea(prompt)
                if idea:
                    st.subheader("✨ Here's your startup plan:")
                    st.write(idea)

        st.session_state.generate = False  # Reset

    # Footer
    st.markdown("---")
    st.markdown("<p style='text-align: center; color: gray;'>Created by: Faisal Abubakar</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    show_startup_generator_page()
