# House Price Predictions

---

## Acknowlegde

 Although I know that I shouldn't say a lot, I want to describe somethings before. It was a hard time for me from the last of my first year in PTIT to now when I'm studying in Australia. In the beginning, I early found my interest in ML and AI, therefore, I spent my time learning it, about the algorithms, data, and math. In the end of first year, I built a strong block of knowlegde in ML and can make a basic project as well. However, it was not depend on intense but consistence. I fell into a hole of depression and anxiety which made me fell extremely terrible. I could not focus on anything: subjects in school, learning new skills, remaining good habits,.. and so on. So I considered taking a big step - studying aboard. And now I am here, start everythings again and try to be optimistic. And now, this is my first ML project which is similar to many ones as well as based on them. However, I try to build it on my own from the skills and knowledge I get from one-month learning.

## Description

This is a ML project from a newbie trying to predict house price. It's based on "Hands-on Machine Learning" book and "Immediate Machine Learning" course of Kaggle. This project aims to predict house price from Ames Housing Dataset. It's an incredible alternative for data scientists looking for a modernized and expanded version of the often cited Boston Housing dataset. 

## Process

- Get the data
- Explore and Visualize the Data to Gain Insights
    - Visualizing Geographical Data
    - Look at Correlations between Attributes
    - Experiment with Attribute Combinations (Division, Multiplication, addition, substraction)
- Prepare Data for ML Algos
    - Clean the Data (Missing Data)
        - Drop missing rows
        - Drop columns missing data
        - Import some value
    - Handle Text and Categorical Attributes
        - Ordinal Encoder
        - One-hot Encoder
    - Feature Scaling and Transformation (features should have similar scale)
        - Min-max scaling (normalization): rescaled ranging from 0 to 1
        - Standardization (subtract mean → mean = 0), and divide standard
        - When have long tails, using some functions (log, distribution)
        - Or bucketizing the data
    - Custom Transformers
    - Transformation Pipelines
- Seclect and Train a Model
    - Train and Evaluate on the Training Set
    - Better evaluation Using Cross-Validation
- Fine-Tune Your Model
    - Grid Search
    - Randomized Search
    - Ensemble Methods
    - Analyzing the Best Models and Their Errors
    - Evaluate Your System on the Test Set
- Launch, Monitor, and Maintain Your System