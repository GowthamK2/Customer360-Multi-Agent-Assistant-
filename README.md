# 🧠 Customer360: Multi-Agent Assistant for Retail Banking

A smart, agentic AI solution that provides a 360-degree view of retail banking customers using a modular multi-agent architecture powered by local LLMs. Built with LangChain, Streamlit, and SQLite for easy deployment and interactive user experience.

---

## 🚀 Project Overview

Customer360: Multi-Agent Assistant is designed to help banks and financial institutions better understand their customers through conversational AI. It leverages multiple intelligent agents—each specialized in a unique task such as querying data, generating summaries, providing product recommendations, or fetching external data.

> 🤖 Ask the system anything about your customers and get actionable insights!

---

## 🛠️ Tools & Technologies

| Type               | Stack/Tool                                      |
|--------------------|--------------------------------------------------|
| **LLM**            | [Phi](https://huggingface.co/microsoft/phi-2) via Ollama |
| **Framework**      | [LangChain](https://www.langchain.com) Agents & Tools |
| **Frontend**       | [Streamlit](https://streamlit.io/)              |
| **Database**       | SQLite                                          |
| **Embeddings**     | Ollama built-in or LangChain Embedding support  |
| **Vector Store**   | FAISS (optional for long-term memory)           |
| **Agent Platform** | LangChain Multi-Agent Chain                      |

---

## 🧩 Multi-Agent Architecture

| Agent Name         | Role                                                                 |
|--------------------|----------------------------------------------------------------------|
| 📊 **DB Query Agent**     | Retrieves customer records from SQLite                         |
| 🧠 **Summary Agent**      | Summarizes customer behavior & financial history               |
| 🛍️ **Recommender Agent**  | Suggests banking products or services tailored to customers   |
| 🌐 **Web Search Agent**   | Fetches financial news or external updates using tools         |
| 🧵 **Coordinator Agent**  | Delegates queries to the appropriate specialized agents        |

See [Agent Interaction Diagram](./docs/agents_interaction_diagram.png)

---

## 📷 Screenshots

![App UI](./screenshots/ui_1.png)  
![Agent Error Debug](./screenshots/ui_2.png)  
![Output Simulation](./screenshots/output_mock.png)

---

## 💡 Features

- Natural language queries (e.g., *"Show me summary for customer 101"*)
- Modular agent interaction with memory and tool usage
- Recommendations and summaries based on customer profiles
- Clean UI built with Streamlit for live interaction
- Extensible codebase with room for cloud, embedding, or RAG upgrades

---

## 🧪 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/customer360-ai.git
cd customer360-ai
📂 Project Structure

customer360-ai/
├── agents/
│   ├── summary_agent.py
│   ├── query_agent.py
│   ├── recommender_agent.py
│   └── coordinator_agent.py
├── tools/
│   └── db_tool.py
├── database/
│   └── customer.db
├── app.py
├── README.md
├── requirements.txt
└── utils/
    └── langchain_setup.py

🧠 Use Cases

    Customer Support Automation

    Internal Employee Assistance

    Personalized Financial Product Promotion

    Pre-sales customer intel tool

👨‍💻 Author

Gowtham K
Built as part of an AI Hackathon project for retail banking innovation.
📜 License

This project is open-sourced under the MIT License. See LICENSE for details.
🙌 Acknowledgements

    LangChain

    Ollama

    Microsoft Phi-2

    Streamlit
