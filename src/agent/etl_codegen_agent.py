from pathlib import Path
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from src.confluence_to_md import fetch_confluence_page, save_to_md

load_dotenv()


class ETLCodegenAgent:
    """
    Agent responsible for:
    1) Fetching mapping from Confluence
    2) Generating ETL transformation code from mapping
    """

    def __init__(self):
        self.llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0
        )

    def fetch_mapping_from_confluence(self):
        """
        Confluence -> MD
        """
        content = fetch_confluence_page()
        save_to_md(content)

    def read_mapping(self, mapping_path: str) -> str:
        """
        Reads mapping document
        """
        return Path(mapping_path).read_text()

    def generate_code(self, mapping_text: str) -> str:
        """
        Generates ETL transformation Python file using LLM
        """

        prompt = f"""
You are a senior data engineer.

Generate PURE PYTHON ETL code based on the mapping below.

Rules:
- Do NOT use any external libraries
- Input data is list of dictionaries
- Mapping is strictly 1:1
- Focus mainly on transformation logic
- Generate ONE Python file only
- File should contain:
    - extract() method (stub)
    - transform() method (real logic)
    - load() method (stub)
- Name the class EmployeeETL
- LOAD_TS should be system generated

Mapping:
{mapping_text}

Output ONLY valid Python code.
Do NOT add explanations.
"""

        return self.llm.invoke(prompt).content

    def write_files(self, code: str):
        """
        Writes generated transformation code
        """
        output_dir = Path("src/generated")
        output_dir.mkdir(parents=True, exist_ok=True)

        output_file = output_dir / "employee_transformation.py"
        output_file.write_text(code)
