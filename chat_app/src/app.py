import streamlit as st
import ollama

# Set the page configuration
st.set_page_config(page_title="My local Chatbot", page_icon="🤖")

st.title("🤖 Local Llama Chatbot")
st.caption("Running locally with Llama - No Data Leaves This PC!")

#st.session_state stores data across reruns in Streamlit.Checks if "messages" exists.If not, it creates it and starts with a default assistant greeting.
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you today?"}]

# Display chat messages from history on app rerun
# for msg in st.session_state.messages:
#     if msg["role"] == "user":
#         st.chat_message(msg["role"]).write(msg["content"])
#     else:
#         st.chat_message(msg["role"]).write(msg["content"])
#This code reads all saved chat messages and displays them as chat bubbles in the app, so the conversation appears on screen every time the app reloads.
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Handle user input
if prompt := st.chat_input("What is on your mind?"):
    # 1. Display user message immediately
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # 2. Placeholder for the AI response
    #Creates the assistant message area.st.empty() creates a placeholder that can be updated repeatedly.Useful for streaming text word-by-word.
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""

        # 3. Call the Local Model
        # We use 'stream=True' so the text types out like in ChatGPT that is returns chunks instead of one full response
        stream = ollama.chat(
            model='llama3',
            messages=[{'role': 'user', 'content': prompt}],
            stream=True,
        )

        # 4. Process the stream. This processes streamed chunks.
        #Example "Hello"
        #" there"
        #"!"
        #full_response = "Hello there!"
        #The ▌ acts like a typing cursor like ChatGPT typing effect.
        for chunk in stream:
            if chunk['message']['content']:
                content = chunk['message']['content']
                full_response += content
                response_placeholder.markdown(full_response + "▌")

        # Final update to removes cursor and shows final complete response.
        response_placeholder.markdown(full_response)

    # 5. Save the AI's response to history
    st.session_state.messages.append({"role": "assistant", "content": full_response})