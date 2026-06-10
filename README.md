# Nordic_test_program

## Overview

This project is a simple prototype exploring how AI could support an initial private equity deal-screening workflow.
The tool takes a company's public website, alongside any extra information, and generates a structured investment screening memo.

## Features
Scrapes public company website information
Generates a structured screening memo
Summarises the business model and market
Identifies potential investment merits and risks
Generates diligence questions
Provides an initial Pass / Watch / Priority recommendation

## Technology Stack
Python
Streamlit
Google Gemini API
BeautifulSoup
Requests

## Why I Built It

After learning more about Nordic Capital's AI internship programme and its focus on translating investment workflows into AI tools, I wanted to build a prototype to understand how AI can speed up workflow and to demonstrate that to you in the brief time I had.
The objective was not to automate investment decisions, but to explore how AI could help structure information and accelerate early-stage research.

## Future Development
If I could develop this further, I would add the following features:
  - Allow the upload of CIM's so the agent can extract information from there to aid faster decision making
  - Add an safety feature which ensures consistency in output format and validates outputs, definitley by checking the output, and perhaps by running 2 agents side by side or asking for sources for every output by the LLM
