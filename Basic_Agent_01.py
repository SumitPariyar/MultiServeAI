import asyncio
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.graph import StateGraph, MessagesState, START
from langgraph.prebuilt import ToolNode, tools_condition

# ==============================
# 🔑 Hardcoded API keys here
# ==============================
GOOGLE_API_KEY = "AIzaSyB1yqMzYYcTUuWE62l97NZelyH1eQo5vSo"
OWM_API_KEY = "b44d5819333319a250c663db464acaa6"
# ==============================


async def main():
    # Initialize MCP client for the weather server
    client = MultiServerMCPClient(
        {
            "weather": {
                "transport": "stdio",
                "command": "C:/Users/Lenovo/OneDrive/Desktop/Agentic_AI_MCP_LangGraph/mcp-openweather/mcp-weather.exe",
                "args": [],
                "env": {"OWM_API_KEY": OWM_API_KEY},
            },

            "calculator": {
                "transport": "stdio",
                "command": "python",
                "args": ["-m", "mcp_server_calculator"]

            }
        }
    )


    # Load available MCP tools
    tools = await client.get_tools()

    # Initialize Gemini (Google Generative AI) model
    model = ChatGoogleGenerativeAI(
        model="models/gemini-2.5-flash",
        api_key=GOOGLE_API_KEY,
        temperature=0
    )

    # Define a function to call the model with tools
    def call_model(state: MessagesState):
        response = model.bind_tools(tools).invoke(state["messages"])
        return {"messages": response}

    # Create and connect graph nodes
    builder = StateGraph(MessagesState)
    builder.add_node("call_model", call_model)
    builder.add_node("tools", ToolNode(tools))


    builder.add_edge(START, "call_model")
    builder.add_conditional_edges("call_model", tools_condition)
    builder.add_edge("tools", "call_model")


    graph = builder.compile()

    # Run the graph (query weather)
    result = await graph.ainvoke({"messages": "what is the temperature in cities of india right now mumbai, dehli, kolkota, banglore?"})
    #print(result["messages"][-1].content)

    while True:
        user_question = input("n\Ask me anything (weather or calculator) : ")
        if user_question.strip().lower() in ["exit", "quit", "No"]:
            print("GoodBye!")
            break

        print("n\--- AI Agent is thinking...--- ")
        result = await graph.ainvoke({"messages":user_question})
        print("\n---Answer---")
        print(result["messages"][-1].content)



if __name__ == "__main__":
    asyncio.run(main())
