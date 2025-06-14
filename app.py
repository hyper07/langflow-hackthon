import streamlit as st
from langflow.load import run_flow_from_json
import tempfiler
import os
from dotenv import load_dotenv

# Load env vars
load_dotenv()
openai_api_key = st.secrets["OPENAI_API_KEY"]
astra_db_token = st.secrets["ASTRA_DB_APPLICATION_TOKEN"]
astra_endpoint = st.secrets["ASTRA_DB_API_ENDPOINT"]

st.markdown(
    """
    <style>
    .main {
        background-color: #F7729C;
    }
    .title {
        font-size: 3em;
        color: #4CAF50;
    }
    .subtitle {
        font-size: 1.5em;
        color: #555555;
    }
    .subtext {
        font-size: 1em;
        color: #777777;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Get the current directory
current_dir = os.path.dirname(__file__)

# Construct the file path 
data_image = os.path.join(current_dir, 'data_analysis.png')
langflow_json = os.path.join(current_dir, 'AI_Data_Analysis.json')

# Title of the app
# Center the title, header, image, and input form
st.markdown("<h1 style='text-align: center;'>Data Analysis AI</h1>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center;'>Intelligent Data Analysis and Insights</h2>", unsafe_allow_html=True)

st.markdown("<h6 style='text-align: center;'>Upload your dataset and specify your analysis requirements to get AI-powered insights and recommendations</h6>", unsafe_allow_html=True)

st.image(data_image, width=650, use_container_width='auto')

# Center the input form
analysis_query = st.text_input("Analysis Query:", key="analysis_query", help="Describe what kind of analysis or insights you want from your data.")

# file upload
temp_file_path = None
uploaded_file = st.file_uploader("Upload Dataset", type=["csv", "xlsx", "json", "pdf"])
if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp_file.write(uploaded_file.getvalue())
        temp_file_path = temp_file.name

# Langflow Implementation
TWEAKS = {
  "ParseData-EA01z": {},
  "Prompt-cwII3": {
  },
  "ChatOutput-T2xaq": {},
  "OpenAIEmbeddings-AGnvK": {
    "openai_api_key": f"{openai_api_key}",
  },
  "OpenAIModel-GM3Ha": {
    "openai_api_key": f"{openai_api_key}",
  },
  "File-S8g3y": {  
    "path": f"{temp_file_path}",
    "silent_errors": False
  },
  "ParseData-Rt5pZ": {},
  "ChatInput-ZffxB": {
      "input_value": f"{analysis_query}",
  },
  "AstraDB-T7QLI": {
      "api_endpoint": f"{astra_endpoint}",
      "token": f"{astra_db_token}",
       "collection_name": "job_listings",
      "embedding_choice": "Astra Vectorize",
      "embedding_provider": "OpenAI",
      "model": "text-embedding-3-small",
  },
  "Prompt-qGHGy": {},
  "OpenAIModel-umK6j": {
    "openai_api_key": f"{openai_api_key}",
  }
}

# Submit
if st.button("Submit"):
  st.write(f"Your analysis query is: {analysis_query}") 
  st.write(f"Thank you for submitting your data analysis request 🙏") 
  
  with st.spinner('Analyzing your data...'):
    result = run_flow_from_json(flow=langflow_json,
                input_value=f"{analysis_query}",
                fallback_to_env_vars=True, # False by default
                tweaks=TWEAKS)

  message = result[0].outputs[0].results['message'].data['text']
  st.write(message)


