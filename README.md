# Data Analysis AI

_AI-powered data analysis tool built with LangFlow and Streamlit._

This project provides an intelligent data analysis assistant that can process datasets and provide insights based on user queries. Upload your data, ask questions, and get AI-generated analysis and recommendations.

## Features

- **Smart Data Processing**: Upload CSV, Excel, JSON, or PDF files for analysis
- **Natural Language Queries**: Ask questions about your data in plain English
- **AI-Powered Insights**: Get intelligent analysis and recommendations
- **Interactive Web Interface**: User-friendly Streamlit interface
- **Vector Database Integration**: Uses AstraDB for efficient data storage and retrieval

## Setup

1. Clone the repository:
```sh
git clone https://github.com/hyper07/langflow-hackthon.git
cd langflow-hackthon
```

2. Install dependencies:
```sh
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file or configure Streamlit secrets with:
- `OPENAI_API_KEY`: Your OpenAI API key
- `ASTRA_DB_APPLICATION_TOKEN`: Your AstraDB token
- `ASTRA_DB_API_ENDPOINT`: Your AstraDB endpoint

4. Run the application:
```sh
streamlit run app.py
```

## Usage

1. Open the web interface (typically at http://localhost:8501)
2. Upload your dataset (CSV, Excel, JSON, or PDF)
3. Enter your analysis query describing what insights you want
4. Click Submit to get AI-powered analysis results

## Resources

- [LangFlow Documentation](https://github.com/logspace-ai/langflow)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [AstraDB Documentation](https://docs.datastax.com/en/astra/home/astra.html)
