import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from google.colab import files
print("Please upload your student data CSV or excel file:")
uploaded_file = files.upload()
uploaded_filename = list(uploaded_file.keys())[0]
try:
    student_df = pd.read_csv(uploaded_filename)
    print("File loaded successfully!")
except Exception as error:
    print("Error loading file:", error)
    raise SystemExit
subject_list = ['Probability', 'Web_Technology', 'Python', 'DBMS', 'Coding_Skills']
for subject in subject_list:
    student_df[f'{subject}_Marks'].fillna(student_df[f'{subject}_Marks'].mean(), inplace=True)
    student_df[f'{subject}_Attendance'].fillna(student_df[f'{subject}_Attendance'].mean(), inplace=True)
student_df['Overall_Attendance'] = student_df[[f'{subject}_Attendance' for subject in subject_list]].mean(axis=1)
student_df['Overall_Marks'] = student_df[[f'{subject}_Marks' for subject in subject_list]].mean(axis=1)
attendance_features = student_df[[f'{subject}_Attendance' for subject in subject_list]]
target_marks = student_df['Overall_Marks']
X_train, X_test, y_train, y_test = train_test_split(attendance_features, target_marks, test_size=0.2, random_state=42)
regression_model = LinearRegression()
regression_model.fit(X_train, y_train)
predicted_marks_test = regression_model.predict(X_test)
mse = mean_squared_error(y_test, predicted_marks_test)
print(f"Model trained. Mean Squared Error: {mse:.2f}")
subject_to_career = {
    'Python': 'Data Science / AI',
    'DBMS': 'Database Administration / Data Analyst',
    'Web_Technology': 'Frontend or Full-Stack Developer',
    'Probability': 'Machine Learning / Data Analyst',
    'Coding_Skills': 'Software Developer / Competitive Programming Roles'
}
def generate_student_feedback(student_record):
    attendance_inputs = [student_record[f'{subject}_Attendance'] for subject in subject_list]
    predicted_average = regression_model.predict([attendance_inputs])[0]
    actual_average = student_record['Overall_Marks']
    attendance_avg = student_record['Overall_Attendance']
    has_good_attendance = attendance_avg >= 75
    has_good_marks = actual_average >= 80
    if has_good_attendance and has_good_marks:
        performance_scenario = "High Attendance, High Marks"
        general_advice = "Outstanding! You have great attendance and excellent academic performance."
    elif has_good_attendance:
        performance_scenario = "High Attendance, Low Marks"
        general_advice = "Good attendance, but marks need improvement. Revise regularly and focus on understanding core concepts."
    elif has_good_marks:
        performance_scenario = "Low Attendance, High Marks"
        general_advice = "Strong marks despite low attendance. Try to attend more classes to maintain and deepen your knowledge."
    else:
        performance_scenario = "Low Attendance, Low Marks"
        general_advice = "Low attendance and marks indicate lack of engagement. Step up your efforts to avoid academic risks."
    personalized_advice = [general_advice]
    for subject in subject_list:
        if student_record[f'{subject}_Marks'] < 60:
            personalized_advice.append(f"Pay extra attention to {subject.upper()} — current performance is below satisfactory.")
    performance_gap = predicted_average - actual_average
    if performance_gap > 10:
        effort_level = "High"
        personalized_advice.append("You're underperforming significantly compared to what your attendance suggests.")
    elif 5 < performance_gap <= 10:
        effort_level = "Moderate"
        personalized_advice.append("Slight underperformance — consistent revision and time management can bridge the gap.")
    else:
        effort_level = "Low"
        personalized_advice.append("You're aligned with or above expected performance. Keep it up!")
    strongest_subject = max(subject_list, key=lambda subj: student_record[f'{subj}_Marks'])
    recommended_career = subject_to_career.get(strongest_subject, "General Tech Roles")
    personalized_advice.append(f"Your best-suited career path could be in **{recommended_career}** based on your strengths.")
    return predicted_average, recommended_career, effort_level, performance_scenario, " ".join(personalized_advice)
feedback_records = []
for _, student in student_df.iterrows():
    predicted, career, effort, scenario, full_feedback = generate_student_feedback(student)
    feedback_records.append({
        'StudentName': student['StudentName'],
        'Predicted_Overall_Marks': round(predicted, 2),
        'Performance_Scenario': scenario,
        'Effort_Level_Required': effort,
        'Recommended_Career_Path': career,
        'Feedback': full_feedback
    })
feedback_df = pd.DataFrame(feedback_records)
final_output = pd.merge(student_df, feedback_df, on='StudentName')
output_filename = 'student_performance_feedback.csv'
final_output.to_csv(output_filename, index=False)
print("\nAnalysis complete. File saved as:", output_filename)
files.download(output_filename)
