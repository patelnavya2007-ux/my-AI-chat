import streamlit as st

st.set_page_config(
    page_title="My AI Chat",
    page_icon="🤖"
)

st.title("🤖 My AI Chat")
st.caption("Your personal AI assistant")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display old messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
prompt = st.chat_input("Ask me anything...")

if prompt:

    # Show user message
    with st.chat_message("user"):
        st.write(prompt)

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # Temporary response
    response = f"You asked: {prompt}"

    # Show AI response
    with st.chat_message("assistant"):
        st.write(response)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })