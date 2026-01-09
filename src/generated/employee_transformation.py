class EmployeeETL:
    def extract(self):
        # Stub for extract method
        pass

    def transform(self, source_data):
        transformed_data = []
        for record in source_data:
            transformed_record = {
                "EMPLOYEE_ID": record.get("EMPLOYEE_ID"),
                "EMPLOYEE_NUMBER": record.get("EMPLOYEE_NUMBER"),
                "FIRST_NAME": record.get("FIRST_NAME"),
                "LAST_NAME": record.get("LAST_NAME"),
                "EMAIL_ADDRESS": record.get("EMAIL_ADDRESS"),
                "PHONE_NUMBER": record.get("PHONE_NUMBER"),
                "DATE_OF_BIRTH": record.get("DATE_OF_BIRTH"),
                "HIRE_DATE": record.get("HIRE_DATE"),
                "TERMINATION_DATE": record.get("TERMINATION_DATE"),
                "JOB_TITLE": record.get("JOB_TITLE"),
                "DEPARTMENT_ID": record.get("DEPARTMENT_ID"),
                "MANAGER_ID": record.get("MANAGER_ID"),
                "EMPLOYMENT_STATUS": record.get("EMPLOYMENT_STATUS"),
                "SALARY_AMOUNT": record.get("SALARY_AMOUNT"),
                "CURRENCY_CODE": record.get("CURRENCY_CODE"),
                "SRC_CREATE_TS": record.get("CREATE_TS"),
                "SRC_UPDATE_TS": record.get("UPDATE_TS"),
                "LOAD_TS": self.get_current_timestamp()
            }
            transformed_data.append(transformed_record)
        return transformed_data

    def load(self, target_data):
        # Stub for load method
        pass

    def get_current_timestamp(self):
        from datetime import datetime
        return datetime.now()