from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.yfinance import YFinanceTools
from agno.tools.duckduckgo import DuckDuckGoTools

web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for information",
    model=Gemini(id="gemini-2.0-flash-exp"),
    tools=[DuckDuckGoTools()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance AI Agent",
    model=Gemini(id="gemini-2.0-flash-exp"),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            company_info=True,
            company_news=True,
            key_financial_ratios=True
        )
    ],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,   
)

agents = Agent(
    name="Financial Research Agent",
    model=Gemini(id="gemini-2.0-flash-exp"),
    team=[web_search_agent, finance_agent],
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

# agents.print_response("What is the current stock price of Apple Inc. (AAPL)?", stream = True)