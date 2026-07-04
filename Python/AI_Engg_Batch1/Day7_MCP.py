def MCPFn():
    from dotenv import load_dotenv
    load_dotenv()
    import asyncio
    from langchain_mcp_adapters.client import MultiServerMCPClient
    from langgraph.prebuilt import create_react_agent
    import os

    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

    async def run_agent():
        client = MultiServerMCPClient(
            {
                "github": {
                    "command": "npx",
                    "args": [
                        "-y",
                        "@modelcontextprotocol/server-github"
                    ],
                    "env": {
                        "GITHUB_PERSONAL_ACCESS_TOKEN": GITHUB_TOKEN
                    },
                    "transport": "stdio"
                },

                # "filesystem": {
                #     "command": "npx",
                #     "args": [
                #         "-y",
                #         "@modelcontextprotocol/server-filesystem",
                #         "/Users/Asus/source/repos/prakash-manit/AgenticAI/Python/AI_Engg_Batch1"
                #     ],
                #     "transport":"stdio"
                # },

                # "TechyPrakashFileSystem": {
                #     "command": "python",
                #     "args": [
                #         "./MCPFileSystem.py"
                #     ],  
                #     "transport":"stdio"             
                # },
            }
        )
        
        tools = await client.get_tools()
        print (tools)
        print ("***********************")

        agent = create_react_agent("groq:llama-3.3-70b-versatile", tools)
        #prompt="Create a new file MCPLocal.txt in the current directory and list the top FIFA teams."
        prompt="Plz list down the files present in repo prakash-manit/AgenticAI/tree/main/Python/AI_Engg_Batch1"
        #prompt="create a new file named BinarySearch.py in the prakash-manit/AgenticAI/tree/main/Python/AI_Engg_Batch1 and add binary search algorithm code in it."
        response = await agent.ainvoke({"messages": prompt})
        print(response["messages"][-1].content)

    asyncio.run(run_agent())



