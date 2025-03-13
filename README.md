# SQL Query Chat LLM App

A natural language to SQL query interface powered by Large Language Models, enabling users to query databases using plain English. This application uses LangChain and Groq's Llama3 model to translate natural language into SQL queries, making database interaction more intuitive and accessible.

## Live Demo

Try the application here: [SQL Query Chat App](https://sql-query-chat-llm-app-ash.streamlit.app/)

## Repository

Find the code on GitHub: [https://github.com/4ashutosh98/sql-query-chat-llm-app.git](https://github.com/4ashutosh98/sql-query-chat-llm-app.git)

## Features

- Natural language to SQL query conversion
- Support for both SQLite and MySQL databases
- Interactive chat interface built with Streamlit
- Real-time query execution and result display
- Streaming response generation
- Conversation history maintenance

## Technologies Used

- **LangChain**: Framework for developing applications with language models
- **Groq**: API access to Llama3-8b-8192 model
- **Streamlit**: Web application framework
- **SQLite**: Local database engine
- **MySQL**: Optional external database connection
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping (ORM) library

## Project Architecture

### Database Component
- SQLite local database with student information
- Optional MySQL database connection

### LLM Component
- Groq API integration with Llama3-8b-8192 model
- LangChain for agent-based LLM orchestration

### Web Interface
- Streamlit-based chat interface
- Supports real-time streaming of LLM responses

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/4ashutosh98/sql-query-chat-llm-app.git
   cd sql-query-chat-llm-app
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the SQLite database:
   ```bash
   python sqlite.py
   ```

5. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage

### Local SQLite Database

1. Select "Use SQLite 3 Database - Student.db" from the sidebar
2. Enter your Groq API key
3. Start asking questions about the student database, such as:
   - "Show me all students"
   - "Who has the highest marks?"
   - "How many students scored less than 50 marks?"
   - "List students in section A"

### External MySQL Database

1. Select "Connect to your SQL Database" from the sidebar
2. Provide MySQL connection details:
   - Hostname
   - Username
   - Password
   - Database name
3. Enter your Groq API key
4. Start querying your MySQL database in natural language

## Default Database Schema

The default SQLite database contains a STUDENT table with the following structure:

| Column  | Type      | Description         |
|---------|-----------|---------------------|
| NAME    | VARCHAR   | Student's name      |
| CLASS   | VARCHAR   | Class/Course name   |
| SECTION | VARCHAR   | Class section       |
| MARKS   | INT       | Student's marks     |

## How It Works

1. User inputs a natural language query
2. The LangChain SQL agent processes the query
3. The agent uses the Llama3 model to understand the intent
4. It translates the natural language to appropriate SQL
5. Executes the SQL against the database
6. Returns the results in a readable format

## Limitations

- Performance depends on the Groq API and Llama3 model capabilities
- Complex analytical queries might require refinement
- Limited to the database schema provided

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Ashutosh Choudhari