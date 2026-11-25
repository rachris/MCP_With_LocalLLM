import asyncio
import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from mcp_use import MCPAgent, MCPClient

async def main():
    # Load environment variables
    load_dotenv()

    # Create configuration dictionary
    config = {
  "mcpServers": {
    "custom_server": {
      "command": "python3",
      "args": ["qwen3_mcp_server.py"],  # Relative path if running from same directory
      "cwd": "/home/rachris/envTestMCP",  # Set working directory
      "env": {}
    }
  }
}

    # Create MCPClient from configuration dictionary
    client = MCPClient.from_dict(config)

    # Create LLM
    llm = ChatOllama(model="qwen2.5-coder:7b", temperature=0.7)

    # Create agent with the client
    agent = MCPAgent(llm=llm, client=client, max_steps=30)

    # Run the query
    result = await agent.run(
        "Get me details from the website https://clay-works.com/",
    )

    results1= agent.run()
    print(f"\nResult: {result}")

if __name__ == "__main__":
    asyncio.run(main())