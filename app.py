import openai
import streamlit as st

# Setting the title of the app
st.title("RevenueMagnet")

# Connect OpenAI key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Initializing session state for model and messages if not already present
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Displaying the chat history
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input from the user
prompt = st.chat_input("What is up?")
if prompt:
    st.session_state["messages"].append({"role": "user", "content": prompt})

    # Displaying user's message in the chat
    with st.chat_message("user"):
        st.markdown(prompt)

    # Placeholder for assistant's message
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        # Generating and displaying response from OpenAI
        for response in openai.ChatCompletion.create(
                model=st.session_state["openai_model"],
                messages=st.session_state["messages"],
                stream=True,  # will provide lively writing
        ):
            # Get content in response
            full_response += response.choices[0].message["content"]
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")

        # Display final assistant's message
        message_placeholder.markdown(full_response)
        # Add assistant's response to the chat history
        st.session_state["messages"].append({"role": "assistant", "content": full_response})
