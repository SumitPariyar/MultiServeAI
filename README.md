🧠 Agentic AI – Multi MCP Agent Project
🚀 Overview

Agentic AI is a simple yet powerful project demonstrating how to build and run OpenAI-compatible AI agents with Modular Communication Protocol (MCP) servers.
It connects tools like a Weather Server 🌦️ and a Calculator Server 🧮 to showcase how agents can use external APIs and logic for reasoning and action.

This project is designed for beginners and enthusiasts exploring AI agent orchestration, OpenAI SDK, and multi-tool integration within a local environment.

🏗️ Features

🌤️ Weather MCP Server — Fetch real-time weather updates.

🧮 Calculator MCP Server — Perform mathematical computations via MCP calls.

🤖 OpenAI Agent SDK — For intelligent reasoning and action chaining.

⚙️ Local Server Setup — Works easily in VS Code or terminal.

💬 Interactive Agent — Chat or issue commands via CLI or API.

📂 Project Structure
Agentic_AI_MCP/
│
├── mcp_servers/
│   ├── weather/
│   │   └── server.py
│   ├── calculator/
│   │   └── server.py
│
├── agent/
│   ├── main.py          # Core agent setup
│   ├── config.py        # Env and keys
│   └── utils.py         # Helper functions
│
├── .env                 # Your environment variables
├── requirements.txt
├── README.md
└── LICENSE

⚙️ Installation & Setup
1️⃣ Clone this repository
git clone https://github.com/<your-username>/Agentic_AI_MCP.git
cd Agentic_AI_MCP

2️⃣ Create & activate a virtual environment
python -m venv .venv
.\.venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Setup environment variables

Create a .env file in the root folder:

OPENAI_API_KEY=your_api_key_here
GEMINI_API_KEY=your_gemini_key_here

5️⃣ Run the MCP servers
python mcp_servers/weather/server.py
python mcp_servers/calculator/server.py

6️⃣ Start your Agent
python agent/main.py

🧩 Example Commands
> What's the temperature in London?
> Add 42 + 58
> Multiply 12 * 15


The agent automatically routes your question to the right MCP server and responds intelligently.

🛠️ Tech Stack

🧠 OpenAI Agent SDK

🌦️ Weather API (via MCP)

🧮 Custom Calculator MCP

🐍 Python 3.10+

⚡ LangChain / Phidata (optional extensions)

🧑‍💻 Author

Sumit [@yourGitHubHandle]
Built with ❤️ using Python & the OpenAI Agent SDK.

📜 License

This project is licensed under the MIT License — feel free to use, modify, and share.
