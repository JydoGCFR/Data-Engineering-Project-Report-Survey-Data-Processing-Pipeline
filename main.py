from pipelinefinal import PipelineProcessor


if __name__ == "__main__":
    # Example usage:
    pipeline = PipelineProcessor(
        input_path=r'Pipeline Class Registration.csv',
        cleaned_path='Cleaned_Pipeline_Class_Registration.csv',
        output_path='Normalized_Pipeline_Class_Registration.xlsx'
    )

    pipeline.load_data()
    pipeline.clean_data()
    pipeline.save_cleaned_data()
    pipeline.normalize_and_save()

    # Example usage of class methods
    new_class_mapping = {
        'Day 1 (7/1)': 1,
        'Day 1 (7/1);Day 2 (7/8)': 2,
        'Day 1 (7/1);Day 2 (7/8);Day 3 (7/15)': 3,
        'Day 1 (7/1);Day 2 (7/8);Day 3 (7/15);Day 4 (7/22)': 4,
        'Day 1 (7/1);Day 2 (7/8);Day 3 (7/15);Day 4 (7/22);Day 5 (7/29)': 5
    }
    updated_class_mapping = PipelineProcessor.update_class_mapping(new_class_mapping)
    print(f"Updated class mapping: {updated_class_mapping}")

    experience_levels = PipelineProcessor.get_experience_levels()
    print(f"Experience levels: {experience_levels}")

    # Example usage of static method
    emails = ["example@example.com", "invalid-email.com"]
    for email in emails:
        print(f"Is '{email}' a valid email? {PipelineProcessor.is_valid_email(email)}")
