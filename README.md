# Financial Agent 🤖

A powerful AI-powered financial research assistant that combines web search capabilities with real-time financial data analysis. Built using Streamlit and the Agno framework, this application provides an intuitive interface for querying financial information and market data.

## Features ✨

- **Real-time Stock Data**: Get current stock prices, company information, and financial ratios
- **Analyst Recommendations**: Access professional analyst ratings and recommendations
- **Company News**: Stay updated with the latest company news and developments
- **Web Search Integration**: Combine financial data with general web search capabilities
- **Interactive UI**: Clean and user-friendly Streamlit interface
- **Data Visualization**: Automatic table formatting for better data presentation

## Prerequisites 📋

- Python 3.8 or higher
- pip (Python package installer)

## Installation 🚀

1. Clone the repository:
```bash
git clone <your-repository-url>
cd financial-agent
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage 💡

1. Start the Streamlit application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the provided local URL (typically http://localhost:8501)

3. Enter your financial questions in the text area. For example:
   - "What is the current stock price of Apple Inc. (AAPL)?"
   - "What are the key financial ratios for Microsoft?"
   - "Show me the latest news about Tesla"
   - "What are the analyst recommendations for Amazon?"

## Project Structure 📁

```
financial-agent/
├── app.py                 # Streamlit web application
├── Financial_Agent.py     # Core agent implementation
├── requirements.txt       # Project dependencies
└── README.md             # Project documentation
```

## Technologies Used 🛠

- **Streamlit**: Web application framework
- **Agno**: AI agent framework
- **Gemini**: Google's AI model for natural language processing
- **YFinance**: Yahoo Finance API for financial data
- **DuckDuckGo**: Web search capabilities

## Features in Detail 🔍

### Financial Data
- Real-time stock prices
- Company information
- Key financial ratios
- Analyst recommendations
- Company news

### Web Search
- General financial information
- Market trends
- Industry analysis
- News articles

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

## License 📄

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments 🙏

- Agno framework for AI agent capabilities
- Streamlit for the web interface
- Yahoo Finance for financial data
- DuckDuckGo for web search capabilities 