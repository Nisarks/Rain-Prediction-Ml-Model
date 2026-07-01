Rain Prediction using Machine Learning

# Project Overview

This project predicts whether it will **rain or not** using a **Logistic Regression** machine learning model. The model is trained on weather parameters such as **Humidity**, **Pressure**, and **Cloud Cover** to classify the weather into two categories:

*  Rain
*  No Rain

The project demonstrates a complete machine learning workflow, including data preprocessing, feature scaling, model training, prediction, and evaluation.

---

##  Features

* Weather dataset preprocessing
* Data visualization using Seaborn
* Missing value inspection
* Feature scaling using StandardScaler
* Logistic Regression classifier
* Train-test data splitting
* Model accuracy evaluation
* Simple and beginner-friendly implementation

---

##  Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* TensorFlow (installed in the notebook environment)

---

##  Project Structure

```
Rain-Prediction-ML/
│
├── copy_of_ml_model_to_predcit_rain.py
├── weather_forecast_data.csv
├── README.md
└── requirements.txt (optional)
```

---

## 📊 Dataset

The dataset contains weather-related attributes used for predicting rainfall.

### Input Features

* Humidity
* Pressure
* Cloud_Cover
* Wind direction
* Temperature

## Target Variable

* Rain

  * 1 → Rain
  * 0 → No Rain
* Target Variable y = Rain / Weather (we have to predict this variable by training) 
* Input Variable  x = * Humidity / Pressure  / Cloud_Cover /  Wind direction / Temperature 
---(select input variables according to the precedence over the target means which variables is more influence on the target variable , there is no restructions to use all features as input its depend on the model and prediction power)

##  Machine Learning Pipeline

1. Load the weather dataset
2. Explore and inspect the data
3. Convert the Rain column into binary values
4. Select important weather features
5. Scale the features using StandardScaler
6. Split the dataset into training and testing sets
7. Train a Logistic Regression model
8. Predict rainfall on test data
9. Evaluate model performance using Accuracy Score

---
##  Preparing the Data


Remember to clean the data before loading into a variable 
remove nan and empty column and useless Data  


##  Model

**Algorithm Used**

* Logistic Regression

This algorithm is suitable for binary classification problems and predicts the probability of rainfall based on the selected weather parameters.

---

##  Evaluation

The model is evaluated using:

* Accuracy Score

Example:

```
Accuracy: 0.92
```

*(The actual accuracy depends on the dataset used.)*

---

##  How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Rain-Prediction-ML.git
```

### 2. Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn tensorflow
```

### 3. Run the Project

```bash
python copy_of_ml_model_to_predcit_rain.py
```

---

##  Workflow

```
Weather Dataset
       │
       ▼
Data Preprocessing
       │
       ▼
Clean the Data
       │
       ▼
Feature Selection
       │
       ▼
Feature Scaling
       │
       ▼
Train-Test Split
       │
       ▼
Logistic Regression
       │
       ▼
Prediction
       │
       ▼
Accuracy Evaluation
```

---

## Future Improvements

* Implement Random Forest Classifier
* Add Decision Tree Classifier
* Try Support Vector Machine (SVM)
* Compare multiple ML algorithms
* Hyperparameter tuning
* Build a Flask or Streamlit web application
* Deploy the model online
* Use additional weather parameters for improved accuracy

---

## Contributing

Contributions from Ceo of Sandur mines Mr Manjunatha S H, feature requests, and suggestions are welcome. Feel free to fork the repository and submit a pull request.

---

##  License

This project is released under the PES License.

---

##  Author

**NISAR K S.**

Electronics and Communication Engineering (ECE)

Interested in Machine Learning, Artificial Intelligence, and VLSI System Design.
