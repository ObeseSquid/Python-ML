import pandas as pd
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import LabelEncoder

# Dataset
data = {
    'Sex': ['Male', 'Female', 'Male', 'Male', 'Male', 'Male', 'Female', 'Male', 'Male', 'Female', 'Male', 'Female', 'Male', 'Male', 'Male'],
    'Student': ['No', 'No', 'Yes', 'No', 'No', 'No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No', 'No', 'No'],
    'Age': ['Old', 'Mid Age', 'Mid Age', 'Old', 'Mid Age', 'Mid Age', 'Mid Age', 'Young', 'Young', 'Mid Age', 'Young', 'Mid Age', 'Old', 'Mid Age', 'Mid Age'],
    'Car Type': ['BMW', 'AUDI', 'BMW', 'AUDI', 'AUDI', 'BMW', 'AUDI', 'BMW', 'BMW', 'BMW', 'BMW', 'BMW', 'AUDI', 'BMW', 'AUDI']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Label encoding the categorical data
le_sex = LabelEncoder()
le_student = LabelEncoder()
le_age = LabelEncoder()
le_car_type = LabelEncoder()

df['Sex_encoded'] = le_sex.fit_transform(df['Sex'])
df['Student_encoded'] = le_student.fit_transform(df['Student'])
df['Age_encoded'] = le_age.fit_transform(df['Age'])
df['Car_Type_encoded'] = le_car_type.fit_transform(df['Car Type'])

# Prepare features (X) and target (y)
X = df[['Sex_encoded', 'Student_encoded', 'Age_encoded']]
y = df['Car_Type_encoded']

# Initialize and train Naive Bayes model
nb_model = CategoricalNB()
nb_model.fit(X, y)

# Define a function to take user input and predict car type
def predict_car_type():
    # Get user input for each feature
    sex_input = input("Enter Sex (Male/Female): ")
    student_input = input("Are they a Student? (Yes/No): ")
    age_input = input("Enter Age (Old/Mid Age/Young): ")
    
    # Convert the inputs to encoded form using the LabelEncoders
    sex_encoded = le_sex.transform([sex_input])[0]
    student_encoded = le_student.transform([student_input])[0]
    age_encoded = le_age.transform([age_input])[0]
    
    # Create a new DataFrame with the encoded inputs
    new_buyer = pd.DataFrame({
        'Sex_encoded': [sex_encoded],
        'Student_encoded': [student_encoded],
        'Age_encoded': [age_encoded]
    })
    
    # Predict the car type using the trained model
    predicted_car_type = nb_model.predict(new_buyer)
    
    # Convert the prediction back to the original label (BMW/AUDI)
    predicted_car = le_car_type.inverse_transform(predicted_car_type)
    
    # Output the result
    print(f'\nThe predicted car type is: {predicted_car[0]}')

# Call the function to predict based on user input
predict_car_type()
