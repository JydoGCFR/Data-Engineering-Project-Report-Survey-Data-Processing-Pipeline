import pandas as pd
from dateutil import tz

class PipelineProcessor:
    class_mapping = {
        'Day 1 (6/20)': 1,
        'Day 1 (6/20);Day 2 (6/27)': 2,
        'Day 1 (6/20);Day 2 (6/27);Day 3 (7/11)': 3,
        'Day 1 (6/20);Day 2 (6/27);Day 3 (7/11);Day 4 (7/18)': 4,
        'Day 1 (6/20);Day 2 (6/27);Day 3 (7/11);Day 4 (7/18);Day 5 (7/25)': 5
    }

    experience_mapping = {
        'Zero experience': 0,
        'Beginner': 1,
        'Capable': 2,
        'Intermediate': 3,
        'Effective': 4,
        'Experienced': 5,
        'Advanced': 6,
        'Distinguished': 7,
        'Master': 8
    }

    def __init__(self, input_path, cleaned_path, output_path):
        self.input_path = input_path
        self.cleaned_path = cleaned_path
        self.output_path = output_path
        self.df = None

    def load_data(self):
        self.df = pd.read_csv(self.input_path)

    def clean_data(self):
        # Rename columns
        self.df = self.df.rename(columns={
            'Username': 'Email Address',
            'StudentID': 'Student ID',
            'Which class session will you attend? (Select all that apply)': 'Classes Attended',
            'Programming Experience level (Any language)': 'Programming Language Experience',
            'Python Programming Experience level': 'Python Experience',
            'LinkedIn Profile URL': 'LinkedIn URL'
        })

        # Create a new column named Username
        self.df['Username'] = self.df['Email Address'].str.split('@').str[0]

        # Create a mapping of job status codes to their descriptions
        job_status_mapping = {
            'Working in Data': 'W',
            'Seeking Job in Data': 'S'
        }
        self.df['Job Status'] = self.df['Job Status'].map(job_status_mapping)

        # Format the ‘Classes Attended’ column
        self.df['Classes Attended'] = self.df['Classes Attended'].map(PipelineProcessor.class_mapping).fillna(0).astype(int)

        # Create a mapping for experience columns
        self.df['Programming Language Experience'] = self.df['Programming Language Experience'].map(PipelineProcessor.experience_mapping).fillna(0).astype(int)
        self.df['Python Experience'] = self.df['Python Experience'].map(PipelineProcessor.experience_mapping).fillna(0).astype(int)

        # Validate and format the LinkedIn profile URLs column
        self.df['LinkedIn URL'] = self.df['LinkedIn URL'].apply(lambda x: f"https://www.linkedin.com/in/{x.split('linkedin.com/in/')[-1]}" if pd.notnull(x) else 'Flag for Review')

        # Ensure the most recent entry for each Username is kept
        self.df['Timestamp'] = pd.to_datetime(self.df['Timestamp'], errors='coerce')
        self.df = self.df.sort_values(by='Timestamp').drop_duplicates(subset='Username', keep='last')

    def save_cleaned_data(self):
        self.df.to_csv(self.cleaned_path, index=False)

    def normalize_and_save(self):
        # Reload cleaned data
        self.df = pd.read_csv(self.cleaned_path)

        # Create normalized tables
        student_pii = self.df[['Username', 'Student ID', 'Email Address', 'Birth Month', 'Timestamp']]
        employment_readiness = self.df[['Username', 'Job Status', 'Classes Attended', 'LinkedIn URL']]
        programming_experience = self.df[['Username', 'Classes Attended', 'Programming Language Experience', 'Python Experience']]
        eligible_invitees = self.df[self.df['Python Experience'] >= 2][['Username', 'Email Address', 'Python Experience']]

        # Save the tables as an Excel workbook
        with pd.ExcelWriter(self.output_path) as writer:
            student_pii.to_excel(writer, sheet_name='Student PII', index=False)
            employment_readiness.to_excel(writer, sheet_name='Employment Readiness', index=False)
            programming_experience.to_excel(writer, sheet_name='Programming Experience', index=False)
            eligible_invitees.to_excel(writer, sheet_name='Eligible Invitees', index=False)

    @classmethod
    def update_class_mapping(cls, new_mapping):
        """Class method to update the class session mapping"""
        cls.class_mapping = new_mapping
        return cls.class_mapping

    @classmethod
    def get_experience_levels(cls):
        """Class method to get the experience levels"""
        return cls.experience_mapping

    @staticmethod
    def is_valid_email(email):
        """Static method to validate email format"""
        return "@" in email and "." in email

