import os
import requests
import base64
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("CONFLUENCE_BASE_URL")
PAGE_ID = os.getenv("CONFLUENCE_PAGE_ID")
EMAIL = os.getenv("CONFLUENCE_EMAIL")
TOKEN = os.getenv("CONFLUENCE_TOKEN")


def fetch_confluence_page():
    url = f"{BASE_URL}/rest/api/content/{PAGE_ID}?expand=body.storage"

    auth_string = f"{EMAIL}:{TOKEN}"
    encoded_auth = base64.b64encode(auth_string.encode()).decode()

    headers = {
        "Authorization": f"Basic {encoded_auth}",
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    data = response.json()
    return data["body"]["storage"]["value"]


def save_to_md(content: str):
    docs_dir = Path("docs")
    docs_dir.mkdir(exist_ok=True)

    output_file = docs_dir / "employee_mapping.md"
    output_file.write_text(content)
