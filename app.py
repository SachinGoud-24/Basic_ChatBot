import streamlit as st
from langchain_openai import OpenAI, ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from dotenv import load_dotenv
from langchain.schema import HumanMessage, AIMessage, SystemMessage
import os

# get openai_api_key
load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

chat = ChatOpenAI(temperature=0.5,model='gpt-3.5-turbo')
llm = OpenAI(temperature=0.5,model='gpt-3.5-turbo')
memory = ConversationBufferMemory()

conversation = ConversationChain(
    llm = chat
    verbose=True
    memory=memory=
)

if 'cont_context' not in st.session_state:
    st.session_state['cont_context'] = [
        SystemMessage(content = 'You are an assistant to a smart, curious and educated person. You always answer with a stern voice, and keep the message to the point')
    ]

# def get_llm_response(question):
#     st.session_state['cont_context'].append(HumanMessage(content=question))
#     response = chat(st.session_state['cont_context'])
#     st.session_state['cont_context'].append(AIMessage(content=question))
#     return response.content

def get_llm_response(q):
    response = chat()

# Streamlit webpage customisation
st.set_page_config(page_title='Your Friendly Chatbot', layout='wide')

st.header('Just a friendly chatbot')
q = st.text_input("Ask me anything: ",key="input")
if st.button('Generate response'):
    # st.text('Here is what I got :')
    st.write(get_llm_response(q))



