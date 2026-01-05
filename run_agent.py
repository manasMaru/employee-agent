from src.agent.etl_codegen_agent import ETLCodegenAgent

agent = ETLCodegenAgent()

agent.fetch_mapping_from_confluence()

mapping_text = agent.read_mapping("docs/employee_mapping.md")
code = agent.generate_code(mapping_text)

agent.write_files(code)

print("End-to-end ETL code generation completed.")
