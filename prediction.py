import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import plotly.express as px
import joblib

# Membaca dataset
df = pd.read_csv('employee_data.csv')

# Mengisi missing value dengan nilai modus
df['Attrition'].fillna(df['Attrition'].mode()[0], inplace=True)

# Memisahkan fitur dan target
X = df.drop('Attrition', axis=1)
y = df['Attrition']

# Split data menjadi training dan testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Standarisasi fitur
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Membuat model RandomForest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Memprediksi data testing
y_pred = model.predict(X_test)

print(classification_report(y_test, y_pred))
print(f'Accuracy: {accuracy_score(y_test, y_pred)}')

new_employee_data = pd.DataFrame({
    'Age': [30],
    'Attrition': [0],
    'BusinessTravel': ['Travel_Rarely'],
    'DailyRate': [1000],
    'Department': ['Research & Development'],
    'DistanceFromHome': [10],
    'Education': [3],
    'EducationField': ['Life Sciences'],
    'EmployeeCount': [1],
    'EnvirontmentSatisfaction': [3],
    'Gender': 'Male',
    'HourlyRate': [100],
    'JobInvolvement': [3],
    'JobLevel': [2],
    'JobRole': ['Research Scientist'],
    'JobSatisfaction': [4],
    'MaritalStatus': ['Single'],
    'MonthlyIncome': [5000],
    'MonthlyRate': [20000],
    'NumCompaniesWorked': [1],
    'Over18': ['Y'],
    'OverTime': ['No'],
    'PercentSalaryHike': [12],
    'PerformanceRating': [3],
    'RelationshipSatisfaction': [3],
    'StandardHours': [80],
    'StockOptionLevel': [0],
    'TotalWorkingYears': [10],
    'TrainingTimesLastYear': [3],
    'WorkLifeBalance': [3],
    'YearsAtCompany': [5],
    'YearsInCurrentRole': [3],
    'YearsSinceLastPromotion': [1],
    'YearsWithCurrManager': [3]
})

# Encoding dan standarisasi data karyawan baru
new_employee_data = pd.get_dummies(new_employee_data)
new_employee_data = new_employee_data.reindex(columns=X.columns, fill_value=0)
new_employee_data = scaler.transform(new_employee_data)

# Prediksi attrition untuk karyawan baru
new_employee_pred = model.predict(new_employee_data)
print('Attrition Prediction for New Employee:', new_employee_pred)

joblib.dump(model, 'attrition_model.pkl')