# Data-Cleaner
# Objective:

 The objective of this term project is to create a comprehensive Python library for data preprocessing tasks, publishable on the Python Package Index (PyPI). The library provides functions for various data cleaning, transformation, and manipulation operations.

 
# Project Goals and Scope:
 The primary goal of this project is to develop a publishable Python library for data preprocessing. The library includes a variety of functions to handle common data preprocessing tasks such as missing value handling, outlier detection, data scaling, text cleaning,
 
 data type conversion, categorical encoding, and datetime handling. The scope of the project covers the following functionalities:
 
# Data Cleaning:

 1. Handling Missing Values:

  - Imputation with mean, median, constant, or deletion
    
 2. Identifying and Correcting Outliers:
    
- IQR outlier detection with threshold
  
 3. Standardizing and Normalizing Data:

    - Min-Max and Standard normalization
      
 4. String Manipulation and Text Cleaning:
    
    - Remove stopwords, lowercase, remove punctuation, lemmatize (requires NLTK)
      
# Data Transformation:

 1. Data Type Conversion:

    - Convert to numeric, convert to categorical
    
 2. Encoding Categorical Data:
   
    - One hot encode, label encode
    
 3. Date and Time Manipulation:
   
    - convert to datetime, extract date features, find and process datetime column, clean invalid dates
      
# Technical Design and Implementation:

 The library is implemented using Python, leveraging pandas and NumPy for data handling, and NLTK for text processing. The library is structured into several submodules, each focusing on a specific aspect of data preprocessing.
 
 # Submodules and Their Functionalities:
 # 1. MissingValueHandler
 
 Provides methods for handling missing values
 
 - impute_mean: Fill missing values with the mean.
   
 - impute_median: Fill missing values with the median.
   
 - impute_constant: Fill missing values with a constant value.
     
 - drop_missing: Drop rows containing missing values.

         
 # 2. OutlierHandler
 
 Provides methods for detecting and handling outliers.
 
 - iqr_outliers: Detects and cleans outliers using the IQR method.
 
 - filter_rare_categories: Filters rare categories.
   
 - lower_text: Converts text to lowercase and removes unnecessary spaces.
     
- upper_text: Converts text to uppercase and removes unnecessary spaces.

         
# 3. TextCleaner

 Provides methods for text cleaning and manipulation.
 
- remove_stopwords: Removes stopwords.

- to_lowercase: Converts text to lowercase.

- remove_punctuation: Removes punctuation marks.

- lemmatize: Lemmatizes words to their root form.

  
# 4. Scaler

 Normalizes or standardizes the dataset.
 
- min_max_scale: Performs Min-Max normalization.

- standard_scale: Standardizes using z-score normalization.

  
# 5. DataTypeConverter

 Converts data types.
 
- to_numeric: Converts data to numeric type.

- to_categorical: Converts data to categorical type.

  
# 6. CategoricalEncoder

 Encodes categorical data.
 
- label_encode: Performs label encoding.

- one_hot_encode: Performs one-hot encoding.

  
 # 7. DateTimeHandler
 
 Handles date and time data.
 
- convert_to_datetime: Converts data to datetime format.

- extract_date_features: Extracts date features.

- find_and_process_datetime_column: Finds and processes a datetime column.

- clean_invalid_dates: Cleans invalid dates.


# Main Script (main.py):
 The main script provides an interactive menu for users to select and apply various data preprocessing operations. The user is prompted to choose a task, such as handling missing values, scaling data, or encoding categorical data. Based on the user's input, the 
 
 corresponding functions from the submodules are called, and the processed data is displayed.
 
 # Workflow:
 
 1. Load the dataset.
 
 2. Display the preprocessing menu.
  
 3. User selects an operation (e.g., handling missing values).
  
 4. User specifies parameters (e.g., column name, imputation method).
  
 5. Apply the selected preprocessing operation.
    
 6. Display the processed data.

# Testing:

 Unit tests are implemented for each submodule to ensure the correctness and robustness of the functions. The tests cover various edge cases and typical usage scenarios.
