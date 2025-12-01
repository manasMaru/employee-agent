from src.employee_metadata import EmployeeMetadata


class Extractor:
    def __init__(self):
        pass

    def extract(self):
        row1 = {
            "EMPLOYEE_ID": 1,
            "EMPLOYEE_NUMBER": "E001",
            "FIRST_NAME": "Rahul",
            "LAST_NAME": "Patel"
        }

        row2 = {
            "EMPLOYEE_ID": 2,
            "EMPLOYEE_NUMBER": "E002",
            "FIRST_NAME": "Sneha",
            "LAST_NAME": "Sharma"
        }

        row3 = {
            "EMPLOYEE_ID": 3,
            "EMPLOYEE_NUMBER": "E003",
            "FIRST_NAME": "Amit",
            "LAST_NAME": "Verma"
        }

        return [row1, row2, row3]



class Transformer:
    def __init__(self):
        pass

    def transform(self, data):
        return data


class Loader:
    def __init__(self):
        pass

    def load(self, data):
        print("loading rows into table:",EmployeeMetadata.table_name)
        print("rows:",data)
