# Website Performance Diagnostics

## Abstract
This repository contains the code to generate automated website diagnosis reports by synthesizing data from server logs, Microsoft Clarity, and Google Analytics. 

---

## Solution Overview

![Architectural Overview](https://github.com/user-attachments/assets/6a2e48e1-636a-41db-af76-dc21a2a2c8e0)

### Inputs
1. **Server Logs:** Incorporated to monitor and ensure core website health/uptime.
2. **Microsoft Clarity:** Leverages co-pilot session summaries instead of heavy video feeds to save tokens and processing costs while capturing essential UX insights.
3. **Google Analytics:** Captures quantitative traffic and engagement metrics crunched by GA.

### Output
A detailed, traceable report that correlates data across all three sources, highlights performance outliers, and suggests actionable recommendations.

### Logic
The pipeline uses a **hierarchical agentic orchestration**:
* Individual specialized agents fetch and structure data from each input source into a standardized JSON format.
* A synthesizing LLM then correlates, combines, and extracts patterns from the combined data to generate the final diagnostic report.

### Constraints & Proof of Concept (POC)
Since direct production platform access wasn't available during development, this POC utilizes a custom local server with mock agents providing dummy responses.

---

## Instructions to Run

### Pre-Requisites
1. **Python:** Built and tested on **Python 3.12**.
2. **API Key:** You will need a `GEMINI_API_KEY`, or you will need to refactor `client.py` and `llm.py` to use your preferred LLM provider.

### Quick Start
1. Install the dependencies:
   ```bash
    pip install -r requirements.txt
2. Run main.py:
  ```bash
  python main.py
