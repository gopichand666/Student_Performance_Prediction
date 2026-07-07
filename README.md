# Student Performance Prediction and Career Recommendation System

## Project Overview

This project is a Machine Learning-based Student Performance Prediction System developed using Python. The system predicts a student's overall academic performance based on attendance in different subjects and provides personalized feedback along with career recommendations based on subject strengths.

The application uses a **Linear Regression** model from Scikit-learn to estimate students' overall marks and generates customized suggestions for improving academic performance.

---

## Features

- Upload student data in CSV format.
- Handle missing attendance and marks automatically.
- Predict overall student performance using Machine Learning.
- Calculate Mean Squared Error (MSE) for model evaluation.
- Generate personalized academic feedback.
- Classify students into different performance scenarios.
- Recommend suitable career paths based on strongest subject.
- Export the complete analysis to a CSV file.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Google Colab
- Linear Regression

---

## Requirements

Install the required Python libraries:

```bash
pip install pandas numpy scikit-learn
```

If using **Google Colab**, no installation is required since most libraries are pre-installed.

---

## Input Dataset

The input dataset should contain the following columns:

| Column Name |
|-------------|
| StudentName |
| Probability_Marks |
| Probability_Attendance |
| Web_Technology_Marks |
| Web_Technology_Attendance |
| Python_Marks |
| Python_Attendance |
| DBMS_Marks |
| DBMS_Attendance |
| Coding_Skills_Marks |
| Coding_Skills_Attendance |

Example:

| StudentName | Probability_Marks | Probability_Attendance | Python_Marks | Python_Attendance |
|--------------|------------------|------------------------|---------------|-------------------|
| Rahul | 82 | 90 | 88 | 95 |
| Priya | 70 | 80 | 75 | 82 |

---

## Project Workflow

1. Upload the student dataset.
2. Load the dataset using Pandas.
3. Replace missing attendance and marks with their respective mean values.
4. Calculate:
   - Overall Attendance
   - Overall Marks
5. Split the dataset into training and testing sets.
6. Train a Linear Regression model.
7. Predict student performance.
8. Calculate Mean Squared Error (MSE).
9. Generate personalized feedback.
10. Recommend career paths.
11. Save the final report as a CSV file.
12. Download the generated report.

---

## Machine Learning Model

**Algorithm Used**

- Linear Regression

### Input Features

- Probability Attendance
- Web Technology Attendance
- Python Attendance
- DBMS Attendance
- Coding Skills Attendance

### Target Variable

- Overall Marks

---

## Performance Scenarios

The system classifies students into four categories:

### 1. High Attendance + High Marks

- Excellent academic performance.
- Encourages maintaining consistency.

### 2. High Attendance + Low Marks

- Good attendance but poor academic performance.
- Suggests regular revision and concept clarity.

### 3. Low Attendance + High Marks

- Performs well despite low attendance.
- Recommends attending more classes.

### 4. Low Attendance + Low Marks

- Indicates lack of engagement.
- Advises increased participation and consistent study.

---

## Career Recommendations

Career suggestions are generated based on the student's highest scoring subject.

| Strongest Subject | Recommended Career |
|-------------------|--------------------|
| Python | Data Science / AI |
| DBMS | Database Administrator / Data Analyst |
| Web Technology | Frontend or Full-Stack Developer |
| Probability | Machine Learning / Data Analyst |
| Coding Skills | Software Developer / Competitive Programmer |

---

## Output

The program generates:

```
student_performance_feedback.csv
```

The output file contains:

- Student Name
- Overall Attendance
- Overall Marks
- Predicted Overall Marks
- Performance Scenario
- Effort Level Required
- Recommended Career Path
- Personalized Feedback

---

## Sample Output

| Student | Predicted Marks | Scenario | Career Recommendation |
|----------|-----------------|----------|-------------------------|
| Rahul | 84.75 | High Attendance, High Marks | Data Science / AI |
| Priya | 73.20 | High Attendance, Low Marks | Frontend Developer |

---

## Evaluation Metric

The model is evaluated using:

**Mean Squared Error (MSE)**

Lower MSE indicates better prediction accuracy.

---

## Advantages

- Easy to use.
- Predicts student performance automatically.
- Generates personalized feedback.
- Handles missing values.
- Supports career guidance.
- Produces downloadable reports.

---

## How to Run

1. Open Google Colab.
2. Upload the Python notebook or script.
3. Run all cells.
4. Upload the student dataset when prompted.
5. Wait for model training and prediction.
6. Download the generated CSV report.

