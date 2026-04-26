import streamlit as st
import pandas as pd
from langchain_ollama import OllamaLLM

# Configure the page layout
st.set_page_config(page_title="AI Data Analyst", layout="wide")
st.title("📊 AI Data Analyst Agent")
st.markdown("Upload a CSV file and let local AI generate EDA code and statistical insights.")

# Sidebar for controls
with st.sidebar:
    st.header("Upload Data")
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
# Initialize variables
df = None
schema_info = None

# Load file
if uploaded_file is not None:
    # Load dataset
    df = pd.read_csv(uploaded_file)

    st.subheader("Raw Data Preview")
    st.dataframe(df.head()) # Renders an interactive table in the browser

    # Extract structural info (from your original logic)
    schema_info = {
        "columns": df.columns.tolist(),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "missing_values": df.isnull().sum().to_dict(),
        "shape": df.shape
    }

# Initialize the local LLM
llm = OllamaLLM(model="mistral")

if st.button("Generate Analysis Code & Insights"):
    # Check if file exists
    if df is None:
        st.warning("Please upload a CSV file first.")
    else:

        with st.spinner("Writing EDA code..."):
            prompt = f"""
                You are a data scientist.
                Here is dataset metadata: {schema_info}
                Write Python code using pandas, matplotlib, and seaborn to:
                1. Generate summary statistics
                2. Plot distributions for numerical columns
                3. Plot correlation heatmap
                4. Identify missing values visually
                Only return executable Python code. Do not include markdown formatting like ```python.
                """

            generated_code = llm.invoke(prompt)

            st.subheader("💻 Generated EDA Code")
            st.code(generated_code, language="python")

        with st.spinner("Analyzing statistics..."):
            # Generate statistical summary
            analysis_summary = df.describe(include="all").to_string()

            insight_prompt = f"""
                You are a senior data scientist.
                Here are summary statistics: {analysis_summary}
                Provide:
                - Key patterns
                - Potential data quality issues
                - Interesting correlations
                - Recommendations for modeling
                Format the response nicely using Markdown.
                """

            insights = llm.invoke(insight_prompt)

            st.subheader("🧠 AI Insights")
            st.markdown(insights)