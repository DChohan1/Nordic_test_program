import os
import requests
import streamlit as st
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from google import genai


load_dotenv()

api_key_gemini = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key_gemini)

st.set_page_config(page_title="PE Deal Screening Agent", layout="wide")

st.title("PE Deal Screening Agent")
st.write("Turn a company website into a first-pass private equity screening memo.")

company_name = st.text_input("Company name")
website_url = st.text_input("Company website URL")
sector_notes = st.text_area("Sector / extra notes")


def scrape_website(url):
    response = requests.get(
        url,
        timeout=10,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    soup = BeautifulSoup(response.text, "html.parser")

    for tag in soup(["script", "style", "nav", "footer"]):
        tag.decompose()

    text = soup.get_text(separator=" ")
    text = " ".join(text.split())

    return text[:8000]


def generate_memo(company_name, website_text, sector_notes):
    prompt = f"""
You are a private equity analyst.

Create a concise first-pass investment screening memo.

Company: {company_name}
Sector / notes: {sector_notes}

Website information:
{website_text}

Use this structure:

1. Business Overview
2. Revenue Model
3. Market / Sector
4. Investment Thesis
5. Key Risks
6. Diligence Questions
7. Comparable Companies
8. Scoring
   - Business quality: /10
   - Market attractiveness: /10
   - Scalability: /10
   - Risk level: /10
9. Initial Recommendation: Pass / Watch / Priority

Be realistic. If information is missing, say what needs to be verified.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )

    return response.text


if st.button("Generate Memo"):
    if not company_name or not website_url:
        st.warning("Please enter a company name and website URL.")
    else:
        with st.spinner("Generating PE screening memo..."):
            website_text = scrape_website(website_url)
            memo = generate_memo(company_name, website_text, sector_notes)

        st.subheader("Investment Screening Memo")
        st.markdown(memo)
