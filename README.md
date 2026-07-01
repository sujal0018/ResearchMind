# 🤖 Multi-Agent AI Research Assistant

An AI-powered research assistant built with **LangGraph**, **LangChain**, **Google Gemini**, and **Tavily Search** that autonomously searches the web, gathers information, scrapes relevant webpages, generates structured research reports, and reviews them using a multi-agent workflow.

---

## 🚀 Features

- 🔍 **Search Agent** – Searches the web for recent and reliable information using Tavily Search.
- 📄 **Reader Agent** – Scrapes the most relevant webpages for detailed information.
- ✍️ **Writer Agent** – Generates a well-structured research report.
- 📝 **Critic Agent** – Reviews the generated report and provides constructive feedback with a score.
- 🌐 Real-time web search with current information.
- 🤖 Powered by Google's **Gemini 2.5 Flash**.
- 🔄 Modular multi-agent architecture using LangGraph.

---

## 🏗️ Architecture

```
                    User Topic
                         │
                         ▼
               🔍 Search Agent
                         │
                         ▼
               Tavily Web Search
                         │
                         ▼
              Search Results + URLs
                         │
                         ▼
               📄 Reader Agent
                         │
                         ▼
                Webpage Scraping
                         │
                         ▼
               ✍️ Writer Agent
                         │
                         ▼
            Structured Research Report
                         │
                         ▼
               📝 Critic Agent
                         │
                         ▼
              Feedback & Quality Score
```

---

## 📂 Project Structure

```
MultiAiAgentSystem/
├── agents.py          # AI agents and prompt templates
├── pipeline.py        # Main research workflow
├── tools.py           # Tavily search and web scraping tools
├── requirements.txt   # Project dependencies
├── .env               # API keys (not included)
└── .gitignore
```

---

## 🛠️ Tech Stack

- Python
- LangChain
- LangGraph
- Google Gemini API
- Tavily Search API
- BeautifulSoup4
- Requests
- Python Dotenv

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/MultiAiAgentSystem.git

cd MultiAiAgentSystem
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate the virtual environment

#### Windows

```powershell
.venv\Scripts\Activate.ps1
```

#### Linux / macOS

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
TAVILY_API_KEY=YOUR_TAVILY_API_KEY
```

---

## ▶️ Running the Project

```bash
python pipeline.py
```

Example:

```
Enter a research topic:

Artificial Intelligence in Healthcare
```

---

## 📑 Example Output

```
Step 1 - Search Agent
✔ Gathered relevant search results

Step 2 - Reader Agent
✔ Scraped webpage content

Step 3 - Writer Agent
✔ Generated detailed research report

Step 4 - Critic Agent
✔ Score: 9/10
✔ Suggested improvements
```

---

## 🤖 Multi-Agent Workflow

### 🔍 Search Agent

- Searches trusted online resources
- Retrieves relevant titles, URLs, and snippets

### 📄 Reader Agent

- Selects relevant webpages
- Scrapes webpage content
- Extracts readable text

### ✍️ Writer Agent

Generates a structured report including:

- Introduction
- Key Findings
- Conclusion
- Sources

### 📝 Critic Agent

Evaluates the report by providing:

- Overall score
- Strengths
- Areas of improvement
- Final verdict

---

## 📦 Dependencies

- langchain
- langgraph
- langchain-google-genai
- tavily-python
- beautifulsoup4
- requests
- python-dotenv

---

## 🔮 Future Improvements

- Support multiple webpages instead of only one
- Parallel webpage scraping
- PDF report export
- Citation generation
- Memory support for previous research
- Research history database
- Streamlit web interface
- Multi-source report summarization

---

## ⭐ If you found this project useful

Please consider giving it a ⭐ on GitHub!
