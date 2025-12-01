class EmployeeMetadata:
    #Table information
    table_name =  "EMPLOYEE"
    load_type = "SCD1"

    #Keys
    surrogate_key = "EMPLOYEE_ID"
    business_keys = ["EMPLOYEE_NUMBER"]

    #schema for target table
    schema = {
        "EMPLOYEE_ID": "BIGINT",
        "EMPLOYEE_NUMBER": "STRING",
        "FIRST_NAME": "STRING",
        "LAST_NAME": "STRING",
        "EMAIL_ADDRESS": "STRING",
        "PHONE_NUMBER": "STRING",
        "DATE_OF_BIRTH": "DATE",
        "HIRE_DATE": "DATE",
        "TERMINATION_DATE": "DATE",
        "JOB_TITLE": "STRING",
        "DEPARTMENT_ID": "BIGINT",
        "MANAGER_ID": "BIGINT",
        "EMPLOYMENT_STATUS": "STRING",
        "SALARY_AMOUNT": "NUMERIC(18,2)",
        "CURRENCY_CODE": "STRING",
        "SRC_CREATE_TS": "TIMESTAMP",
        "SRC_UPDATE_TS": "TIMESTAMP",
        "LOAD_TS": "TIMESTAMP",
    }




