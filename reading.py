import pandas as pd

# Replace 'project.xlsx' with your actual file path
file_path = 'project.xlsx'

# Read the Excel sheet into a DataFrame
df = pd.read_excel(file_path)

# Display the DataFrame (optional)
print(df)

# Access subjects and questions columns
subjects = df['Subject'].tolist()
questions = df['Question'].tolist()

# Display subjects and questions
for subject, question in zip(subjects, questions):
    print(f"Subject: {subject}\nQuestion: {question}\n")
