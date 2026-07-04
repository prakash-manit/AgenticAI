from mcp.server.fastmcp import FastMCP
import os

mcp = FastMCP("TechyPrakashFileSystem")

@mcp.tool()
def addFile(filename: str) -> str:
    """Create a new file in current directory"""
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            pass
        return f"File '{filename}' created successfully."
    else:
        return f"File '{filename}' already exists."

@mcp.tool()
def addFolder(directory_name: str) -> str:
    """Create a new Directory in current directory"""
    if not os.path.exists(directory_name):
        os.mkdir(directory_name)
        return f"Directory '{directory_name}' created successfully."
    else:
        return f"Directory '{directory_name}' already exists."

mcp.run(transport="stdio")