import openai
import streamlit as st
import json

openai.api_key = 'API-KEY'

system_message = {

  "role": "assistant",
  "content" : "You are Amelia, a virtual in-flight attendant set in the cabin of one of NASA's AAM passenger transport vehicles. Your job is to help with notifying passengers of arrival times, \
    weather conditions, and other features to ease the nerves of the passengers as this program is still in testing. Please assume this drone is in Chicago, traveling between downtown and \
    O'Hare airport. Scrape today's date from the internet to gather data."
}


#thread = OpenAI.beta.threads.create()

# Function to get response from OpenAI
def get_chatgpt_response(prompt, model="gpt-3.5-turbo"):
    messages = [{"role":"user", "content": prompt}]
    response = openai.chat.completions.create(
        model = model,
        messages=messages,
        temperature=0.7,
        #max_tokens=150
    )
    return response.choices[0].message.content

# Streamlit app content
st.title("Amelia Chatbot")

# Initialize session state for conversation history
if 'conversation' not in st.session_state:
    st.session_state.conversation = []
    #st.session_state.conversation.append(system_message)

# Input form for user prompt
user_input = st.text_input("You:", key="user_input")

if st.button("Send"):
    if user_input:
        st.session_state.conversation.append(f"You: {user_input}")
        prompt = f"""
        {{
            "task": "Based on the given summary of the conversation and the context, answer the question",
            "context": "{system_message}",
            "summary": "{st.session_state.conversation}",
            "question": "{user_input}",
            "answer": "...",
        }}"""
        response = get_chatgpt_response(prompt)
        #parsed_response = json.loads(response)
        #answer = parsed_response.get("answer", "error")
        st.session_state.conversation.append(f"Amelia: {response}")

# Display conversation history
for message in st.session_state.conversation:
    st.write(message)

