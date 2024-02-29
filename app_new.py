import streamlit as st
from langchain_openai import OpenAI, ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains.conversation.memory import ConversationSummaryMemory
from langchain.chains import ConversationChain
from dotenv import load_dotenv
import os

# get openai_api_key
load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

chat = ChatOpenAI(temperature=0.5,model='gpt-3.5-turbo')
memory = ConversationSummaryMemory(llm=OpenAI())

conversation = ConversationChain(
    llm = chat,
    verbose=True,
    memory=memory
)

def get_llm_response(q):
    response = conversation.predict(input=q)
    return response

# Streamlit webpage customisation
st.set_page_config(page_title='Your Friendly Chatbot', layout='wide')

st.header('Just a friendly chatbot')
q = st.text_input("Ask me anything: ",key="input")
if st.button('Generate response'):
    st.write(get_llm_response(q))



