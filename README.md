# **Data-Engineering-Survey-Data-Processing-Pipeline**

**Project Overview**

The project involves developing a data pipeline for Cardinal Surveying, an exclusive recruiting firm for University of Louisville Alumni. The task is to create a database from a survey of potential candidates, focusing on identifying individuals knowledgeable in Python for future healthcare client events. The pipeline will process an initial CSV file, normalize the data into structured tables, and output these tables into an Excel workbook.

**Data Sources**

**Input CSV File:** Pipeline Class Registration.csv
Contains survey responses from potential candidates regarding their programming skills, specifically in Python.

**Output Excel Workbook:** Normalized_Pipeline_Class_Registration.xlsx
Contains separate tabs for normalized tables derived from the input CSV file.

**Data Processing Pipeline**

**Steps in the Data Pipeline**

**Data Ingestion**

Read the input CSV file containing survey responses.
Used Pandas library to load data into a DataFrame.

**Data Cleaning**

Inspected and cleaned the data, handling missing values and duplicates as necessary.
Converted relevant columns to appropriate data types.

**Data Normalization**

Broke the data into normalized tables based on logical groupings. For example:
Candidates Table: Contains candidate information (name, contact details, etc.).
Skills Table: Contains programming skills related to Python.
Event Invitations Table: Lists events and invited candidates.
Created separate DataFrames for each normalized table.

**Output Preparation**

Prepared the normalized tables for output in an Excel workbook with separate tabs.
Used Pandas ExcelWriter to write multiple DataFrames to different sheets in an Excel file.

**Data Pathways and Schemas**

Defined schemas for each normalized table, detailing column names and data types. Here’s an example schema:
Candidates Table Schema
CandidateID: Integer
Name: String
Email: String
Skills Table Schema
CandidateID: Integer
Python: Boolean
OtherSkills: String
Events Table Schema
EventID: Integer
CandidateID: Integer
EventDate: Date

**Updated Cadence and Procedures**

The pipeline was designed to accommodate updates from the input CSV file. When a new CSV is provided:
The pipeline was coded to re-run the data cleaning, normalization, and output steps.
It would check for changes in candidate skills and event invitations, adjusting tables accordingly.

**Final Output**

Excel Workbook: Normalized_Pipeline_Class_Registration.xlsx
Contains the following tabs:
Candidates: List of candidates with their contact information.
Skills: Programming skills related to each candidate.
Events: Details of events and the candidates invited to each.

**Conclusion**

This project successfully created a data processing pipeline that transforms raw survey data into structured, normalized tables. The output Excel workbook serves as a foundation for Cardinal Surveying to manage candidate data efficiently, aiding in future event planning for Python programming events. The modular design allows for easy updates and maintenance, ensuring the system can adapt to changes in the source data.
