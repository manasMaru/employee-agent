from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_classic.tools import tool
from langchain_classic.agents import create_react_agent, AgentExecutor
from langchain_classic.prompts import PromptTemplate

from src.employee_transformation import Extractor, Transformer, Loader

load_dotenv()

extractor = Extractor()
transformer = Transformer()
loader = Loader()


@tool
def run_etl(input : str) -> list:
    """Runs the ETL pipeline: extract -> transform -> load."""
    raw = extractor.extract()
    transformed = transformer.transform(raw)
    loader.load(transformed)
    return transformed


def create_agent():
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    tools = [run_etl]


    prompt = PromptTemplate(
        input_variables=["input", "agent_scratchpad", "tool_names", "tools"],
        template="""
You are an ETL agent.
When the user requests to run ETL, use the tool `run_etl`.

Available tools:
{tools}

Tool names:
{tool_names}

User message:
{input}

{agent_scratchpad}
""",
    )

    agent = create_react_agent(
        llm=llm,
        tools=tools,
        prompt=prompt
    )

    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    return agent_executor
