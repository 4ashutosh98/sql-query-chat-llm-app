import streamlit as st
from pathlib import Path
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_community.utilities import SQLDatabase
from langchain.agents.agent_types import AgentType
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from sqlalchemy import create_engine
import sqlite3
from langchain_groq import ChatGroq

st.set_page_config(page_title = "Langchain: Chat with SQL DB", page_icon="😊")
st.title("LangChain: Chat with SQL DB")

LOCALDB = "USE_LOCALDB"
MYSQL = "USE_MYSQL"

radio_opt: list[str] = ["Use SQLite 3 Database - Student.db", "Connect to your SQL Database"]

selected_opt = st.sidebar.radio(label = "Choose the DB which you want to use", options = radio_opt)

if radio_opt.index(selected_opt) == 1:
    db_uri = MYSQL
    mysql_host = st.sidebar.text_input("Provide My SQL Hostname")
    mysql_username = st.sidebar.text_input("Provide My SQL Username")
    mysql_password = st.sidebar.text_input("Provide My SQL Password", type="password")
    mysql_db = st.sidebar.text_input("MySQL database")
else:
    db_uri = LOCALDB

api_key = st.sidebar.text_input(label = "Groq API Key", type="password")

if not api_key:
    st.info("Please add the Groq API Key")
    st.stop()  # Stop execution here if no API key

if not db_uri:
    st.info("Please enter the database information and URI")
    st.stop()  # Stop execution here if no database info

# LLM Model - Only initialize when API key is available
llm = ChatGroq(groq_api_key=api_key, model_name="Llama3-8b-8192", streaming=True)

@st.cache_resource(ttl = "2h")
def configure_db(db_uri, mysql_host = None, mysql_username = None, mysql_password = None, mysql_db = None):
    if db_uri == LOCALDB:
        db_file_path = (Path(__file__).parent/"student.db").absolute()
        print(db_file_path)
        creator = lambda: sqlite3.connect(f"file:{db_file_path}?mode=ro", uri = True)
        return SQLDatabase(create_engine("sqlite:///", creator = creator))
    elif db_uri == MYSQL:
        if not (mysql_host and mysql_username and mysql_password and mysql_db):
            st.error("Please provide all MySQL connection details")
            st.stop()
        return SQLDatabase(create_engine(f"mysql+mysqlconnector://{mysql_username}:{mysql_password}@{mysql_host}/{mysql_db}"))
    
if db_uri == MYSQL:
    db = configure_db(db_uri=db_uri, mysql_host=mysql_host, mysql_username=mysql_username, mysql_password=mysql_password, mysql_db=mysql_db)
else:
    db = configure_db(db_uri=db_uri)

## Toolkit
toolkit = SQLDatabaseToolkit(db = db, llm = llm)

agent = create_sql_agent(
    llm = llm,
    toolkit = toolkit,
    verbose= True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION
)

if "messages" not in st.session_state or st.sidebar.button(("Clear message history")):
    st.session_state["messages"] = [{"role": "assistant", "content" : "How can I help you?"}]

for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).write(msg["content"])

user_query = st.chat_input(placeholder="Ask anything from the database e.g. Show me all students in the students table of the database")

if user_query:
    st.session_state.messages.append({"role": "user", "content": user_query})
    st.chat_message("user").write(user_query)

    with st.chat_message("assistant"):
        streamlit_callback = StreamlitCallbackHandler(st.container())
        response = agent.run(user_query, callbacks=[streamlit_callback])
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.write(response)