from src.generated.employee_transformation import EmployeeETL
from src.connectors.source.file_source import FileSourceConnector
from src.connectors.target.file_target import FileTargetConnector

source = FileSourceConnector()
target = FileTargetConnector()

etl = EmployeeETL()

raw_data = source.read()
transformed_data = etl.transform(raw_data)
target.write(transformed_data)