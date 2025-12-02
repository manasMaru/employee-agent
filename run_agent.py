from etl_agent import create_agent

agent = create_agent()

response = agent.invoke({"input": "Run the ETL pipeline"})
print(response["output"])
