from src.connectors.base import SourceConnector

class FileSourceConnector(SourceConnector):
    def read(self):
        #demo
        return [
            {
                "EMPLOYEE_ID": 1,
                "EMPLOYEE_NUMBER": "E001",
                "FIRST_NAME": "Manas",
                "LAST_NAME": "Maru",
                "EMAIL_ADDRESS": "manas@example.com",
                "PHONE_NUMBER": "9999999999",
                "DATE_OF_BIRTH": "1999-01-01",
                "HIRE_DATE": "2022-06-01",
                "TERMINATION_DATE": None,
                "JOB_TITLE": "Software Engineer",
                "DEPARTMENT_ID": 10,
                "MANAGER_ID": 100,
                "EMPLOYMENT_STATUS": "Active",
                "SALARY_AMOUNT": 80000.00,
                "CURRENCY_CODE": "INR",
                "CREATE_TS": "2022-06-01 10:00:00",
                "UPDATE_TS": "2024-01-01 12:00:00"
            },
            {
                "EMPLOYEE_ID": 2,
                "EMPLOYEE_NUMBER": "E002",
                "FIRST_NAME": "Anita",
                "LAST_NAME": "Verma",
                "EMAIL_ADDRESS": "anita.verma@example.com",
                "PHONE_NUMBER": "8888888888",
                "DATE_OF_BIRTH": "1995-08-20",
                "HIRE_DATE": "2020-11-10",
                "TERMINATION_DATE": None,
                "JOB_TITLE": "Senior Analyst",
                "DEPARTMENT_ID": 20,
                "MANAGER_ID": 101,
                "EMPLOYMENT_STATUS": "Active",
                "SALARY_AMOUNT": 90000.00,
                "CURRENCY_CODE": "INR",
                "CREATE_TS": "2020-11-10 09:15:00",
                "UPDATE_TS": "2025-12-20 16:45:00"
            }
        ]
