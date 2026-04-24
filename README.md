# Multi Tool AI Agent

A modular AI agent built with Python and LangChain that dynamically selects tools to solve different user requests.

## Overview

This project demonstrates how to build a production-style multi-tool AI agent using modern Python architecture.

The agent can:

* Search inside PDF documents
* Analyze CSV datasets
* Perform arithmetic calculations
* Route tasks to the correct tool automatically
* Respond in Hungarian

## Features

### Document Search

Uses vector search / retrieval to answer questions from PDF documents.

### CSV Analysis

Reads structured CSV files and performs operations such as:

* row count
* column listing
* mean
* sum
* min / max

### Calculator Tool

Safely evaluates arithmetic expressions.

### AI Tool Routing

Uses an LLM agent to decide which tool should handle the request.

## Project Structure

```text
multi-tool-agent/
├── src/
│   └── multi_tool_agent/
│       ├── config.py
│       ├── context.py
│       ├── prompts.py
│       ├── agent.py
│       ├── main.py
│       └── tools/
│           ├── calculator.py
│           ├── csv_tool.py
│           └── document_search.py
├── data/
├── notebooks/
├── README.md
├── pyproject.toml
└── .env.example
```

## Notebook Demo

The `notebooks/demo.ipynb` file contains the original experimentation and interactive demonstrations used during development.

## Tech Stack

* Python
* LangChain
* OpenAI API
* Pandas
* Jupyter Notebook

## Data Sources

- `sales.csv` is a synthetic mock dataset created for demo purposes.
- `kisvallalati_ado_szabalyzat.pdf` was downloaded from the official website of the Hungarian tax authority / government source and is used for retrieval testing.

## Installation

```bash
git clone https://github.com/yourusername/multi-tool-agent.git
cd multi-tool-agent
pip install -e .
```

## Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

## Run the Project

```bash
python -m multi_tool_agent.main
```

## Example Queries

* What is the total revenue?
* What does the PDF say about VAT exemption?
* Calculate 52000 * 1.27

## Why I Built This

This project was created to demonstrate skills relevant for a Junior AI Engineer role:

* modular Python development
* clean project architecture
* LLM tool orchestration
* retrieval-based question answering
* data analysis automation

## Future Improvements

* FastAPI deployment
* Web UI
* Memory support
* Unit tests
* Docker support
