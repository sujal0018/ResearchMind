# 🔬 ResearchMind — Multi-Agent AI Research System

A practical, project-first implementation of a **multi-agent AI pipeline** built with **LangChain**. Instead of relying on a single prompt to an LLM, this system orchestrates four specialized agents that work together—searching the web, scraping content, writing a structured report, and critiquing the result—to turn any research topic into a polished report.

Built as a hands-on exploration of **Agentic AI**, this project demonstrates how multiple AI agents can collaborate by passing information through a shared pipeline, highlighting the difference between traditional LLM chains and autonomous tool-using agents.

## 🚀 How It Works

The research pipeline executes four stages in sequence, with each stage passing its output to the next:

### 🔎 Search Agent

* Searches the web using the **Tavily API**
* Retrieves relevant articles with titles, URLs, and summaries
* Finds recent and reliable information about the topic

### 📖 Reader Agent

* Selects the most relevant search result
* Scrapes the webpage using **Requests** and **BeautifulSoup**
* Extracts clean textual content for deeper analysis

### ✍️ Writer Chain

* Combines search results and scraped content
* Generates a structured research report containing:

  * Introduction
  * Key Findings (3+ points)
  * Conclusion
  * Sources

### 🧐 Critic Chain

* Reviews the generated report
* Assigns a score out of **10**
* Highlights strengths
* Suggests improvements
* Provides a concise final verdict

The first two stages are implemented as **LangChain agents** capable of using tools, while the Writer and Critic are implemented as lightweight **LLM chains**. This showcases when an autonomous agent is beneficial versus when a simple prompt pipeline is sufficient.

---

## 🛠️ Tech Stack

* **LangChain** — Agent and chain orchestration
* **OpenAI GPT-4o Mini** — Large Language Model powering the pipeline
* **Tavily API** — Live web search
* **BeautifulSoup + Requests** — Web scraping
* **Streamlit** — Interactive frontend
* **python-dotenv** — Environment variable management

---

## 🎯 Usage

1. Launch the Streamlit application.
2. Enter any research topic.
3. Click **⚡ Run Research Pipeline**.
4. Watch each agent execute in real time:

   * Search → Reader → Writer → Critic
5. Review the generated research report.
6. View the critic's evaluation.
7. Download the report as a Markdown (`.md`) file.

Example research topics:

* Quantum Computing Breakthroughs
* Future of Autonomous Vehicles
* AI in Healthcare
* Renewable Energy Trends
* Space Exploration Missions

---

## ✨ What This Project Demonstrates

* Difference between **LLM Chains** and **AI Agents**
* Building specialized agents with focused responsibilities
* Tool calling using LangChain agents
* Passing shared state across multiple pipeline stages
* Integrating web search and web scraping into an AI workflow
* Building an interactive Agentic AI application using Streamlit
* Organizing a clean, modular multi-agent architecture for real-world AI projects

---

