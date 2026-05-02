# 🤖 Multi-Agent AI Assistant

A powerful **multi-agent AI system** that can:

* Break down user tasks
* Perform web research
* Generate code
* Debug and improve code automatically

Built using **LangGraph, Groq, Tavily, and Streamlit**.

---

## 🚀 Live Demo

👉 https://your-app-name.streamlit.app
*(replace with your actual Streamlit URL)*

---

## 🧠 How It Works

This project uses a **multi-agent pipeline**:

User Input
⬇
🧠 Task Agent → Breaks problem into steps
⬇
🔍 Research Agent → Fetches relevant info (Tavily)
⬇
💻 Software Agent → Generates code
⬇
🐞 Debug Agent → Fixes and improves code

---

## 🧩 Features

* ✅ Multi-agent orchestration using **LangGraph**
* ✅ Web search integration (**Tavily API**)
* ✅ Fast LLM responses (**Groq API**)
* ✅ Automatic code generation
* ✅ Code debugging and improvement
* ✅ Secure API key handling (no secrets in code)
* ✅ Streamlit UI

---

## 🛠️ Tech Stack

* Python
* LangChain / LangGraph
* Groq (LLM)
* Tavily (Search API)
* Streamlit (Frontend)

---

## 📂 Project Structure

```
multi-agent-ai-assistant/
│
├── app/
│   ├── agents/
│   │   ├── task_agent.py
│   │   ├── research_agent.py
│   │   ├── software_agent.py
│   │   └── debug_agent.py
│   │
│   ├── graph/
│   │   └── workflow.py
│   │
│   ├── config.py
│   └── main.py
│
├── streamlit_app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation (Local Setup)

### 1. Clone the repo

```
git clone https://github.com/subhakarRPeddakkagar/multi-agent-ai-assistant.git
cd multi-agent-ai-assistant
```

---

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

### 4. Add API Keys

Create a `.env` file:

```
GROQ_API_KEY=gsk-your-key
TAVILY_API_KEY=tvly-your-key
```

---

### 5. Run the app

```
streamlit run streamlit_app.py
```

---

## ☁️ Deployment (Streamlit Cloud)

1. Push code to GitHub
2. Go to Streamlit Cloud
3. Deploy using `streamlit_app.py`
4. Add secrets:

```
GROQ_API_KEY = "your-key"
TAVILY_API_KEY = "your-key"
```

---

## 📸 Screenshots

*(Add screenshots of your app here for better presentation)*

---

## 🎯 Example Prompt

```
Build a Flask API for login with JWT authentication
```

---

## 🔐 Security

* API keys are stored securely using:

  * `.env` (local)
  * `Streamlit secrets` (deployment)
* No secrets are exposed in the repository

---

## 🚀 Future Improvements

* Add memory (chat history)
* Code execution agent
* Better UI (chat interface)
* Improved research filtering
* Caching & rate limit handling

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

**Subhakar R Peddakkagar**
GitHub: https://github.com/subhakarRPeddakkagar

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
