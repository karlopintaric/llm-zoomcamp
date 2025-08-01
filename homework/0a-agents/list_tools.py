import asyncio

from fastmcp import Client

async def main():
    async with Client("weather_server.py") as mcp_client:
        tools = await mcp_client.list_tools()
        return tools

if __name__ == "__main__":
    test = asyncio.run(main())
    print(test)