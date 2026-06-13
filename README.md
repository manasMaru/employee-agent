# Employee Agent (AI-based ETL Code Generation)

A system that explores automated generation of ETL transformation code from Confluence mapping documents using LLMs.

---

## Overview

This project implements a two-phase pipeline:

1. Code Generation Phase  
   - Fetches mapping documents from Confluence  
   - Stores them into a local markdown file  
   - Uses an LLM (via LangChain) to generate Python ETL transformation code  

2. Execution Phase  
   - Uses generated transformation code  
   - Reads input data via a source connector  
   - Applies transformation logic  
   - Writes output via a target connector  

---

## Architecture

```
Confluence (HTML)
        ↓
Markdown Mapping File (docs/)
        ↓
LLM (LangChain + OpenAI)
        ↓
Generated Python ETL Code (src/generated/)
        ↓
Execution Pipeline (connectors + transform)
```

---

## How It Works

### 1. Fetch Mapping
- Uses Confluence REST API  
- Authenticated via API token  
- Retrieves mapping content (HTML)  

### 2. Store Mapping
- Saves content to:
```
docs/employee_mapping.md
```

### 3. Generate ETL Code
- LLM generates Python code based on mapping  
- Enforced constraints:
  - No external libraries  
  - Input: list of dictionaries  
  - 1:1 field mapping  
  - Includes extract(), transform(), load()  

- Output saved to:
```
src/generated/employee_transformation.py
```

### 4. Execute ETL Pipeline
- Source connector provides input data  
- Generated transform() applies mapping  
- Target connector outputs transformed data  

---

## Tech Stack

- Python  
- LangChain  
- OpenAI API  
- Confluence REST API  

---

## 📂 Project Structure

```
employee-agent/
├── docs/
│   └── employee_mapping.md
├── src/
│   ├── agent/
│   │   └── etl_codegen_agent.py
│   ├── connectors/
│   │   ├── source/
│   │   │   └── file_source.py
│   │   ├── target/
│   │   │   └── file_target.py
│   │   └── base.py
│   ├── generated/
│   │   └── employee_transformation.py
│   └── confluence_to_md.py
├── .env
├── .gitignore
├── README.md
├── requirements.txt
├── run_agent.py
└── run_employee_etl.py
```

---

##  How to Run

### 1. Install dependencies
```
pip install -r requirements.txt
```

### 2. Set environment variables
```
CONFLUENCE_BASE_URL=
CONFLUENCE_PAGE_ID=
CONFLUENCE_EMAIL=
CONFLUENCE_TOKEN=
OPENAI_API_KEY=
```

### 3. Generate ETL code
```
python run_agent.py
```

### 4. Execute ETL pipeline
```
python run_employee_etl.py
```

---

##  Key Learnings

- ETL transformations are often deterministic and rule-based  
- LLM-based generation introduces variability and cost  
- Rule-based approaches are more reliable for structured mappings  

---

##  Limitations

- Not production-ready  
- Generated code may not always be consistent
- LLM adds unnecessary complexity for deterministic transformations  

---

##  Conclusion

While LLMs can generate ETL transformation logic, many real-world ETL workflows are better handled using deterministic, rule-based systems.

---

## 👤 Author

Manas Maru