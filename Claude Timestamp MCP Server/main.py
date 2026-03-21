#!/usr/bin/env python3
# save as: time_server.py

from mcp.server.fastmcp import FastMCP
from datetime import datetime
import pytz

mcp = FastMCP("Time Server")

@mcp.tool()
def get_current_time() -> str:
    """Get the current date and time in Australian Eastern time."""
    tz = pytz.timezone("Australia/Brisbane")
    now = datetime.now(tz)
    return now.strftime("It's %A, %d %B %Y at %I:%M %p AEST")

if __name__ == "__main__":
    mcp.run(transport="sse", host="0.0.0.0", port=8000)