# What can change?
![image](https://github.com/user-attachments/assets/3d7fbd43-d6ee-4e66-a5c0-5a4eeaf88cf2)

# What to do?
![image](https://github.com/user-attachments/assets/6d0280f2-ad16-4459-b562-e3edf0822361)

## Adapt to data
  - Look for data leakage.
  - Look for cold start problems(Starting with no data or not considering new data generated).
![image](https://github.com/user-attachments/assets/e595f6f0-fa51-438e-a76a-6c73dbbbacfd)
![image](https://github.com/user-attachments/assets/2c523bec-c60c-44c5-8523-f812ab5e8949)

# Drifts (Data & Concept)
  - Why do machine learning models lose their predictive power over time?
  - Traditional supervised learning assumes that the training and the application data come from the same distribution and
    they developed  with certain assumptions.
  - Production data can diverge or drift from the baseline data over time due  to changes in the real world.
  - Data Drift or change in probability of X P(X) is a shift in the model’s input data distribution. For example, the incomes of all applicants increase by 5%, but the economic fundamentals are the same.
  - Concept drift, or change in  probability of Y given X, is a shift in the actual relationship between the model inputs and the output. An example of concept drift is when macroeconomic factors make lending riskier, and there is a higher standard  to be eligible for a loan.In this case, an income level that was earlier considered creditworthy is no longer creditworthy.
  - Prediction drift, or change in the predicted value of Y given X, is a shift in the model’s predictions. For example, a larger proportion of credit-worthy applications when your product was launched in a more affluent area.Your model still holds, but your business may be  unprepared for this scenario.
  - Label drift or change in the predicted value of Y as your target variable is a shift in the model’s  output or label distribution.
  - Concept drift can occur due to shifts in the feature space and/or the decision boundary, so we need to be aware of these during production.If the data is changing, or if the relationship between the features and the label is changing, this is going to cause issues with our model.
![image](https://github.com/user-attachments/assets/01e3e7e5-e82e-4900-894c-14d2b4a8b636)
![image](https://github.com/user-attachments/assets/7e82f6da-cf7b-4c86-b673-6c6b84990239)
![image](https://github.com/user-attachments/assets/ebfcb57c-d9b2-49d2-90d8-7a486585c95a)
![image](https://github.com/user-attachments/assets/5bfc82da-de70-46f1-a6a8-971e3e90ff39)
![image](https://github.com/user-attachments/assets/2b418ebf-315c-4c6a-869b-69a4fc87e72a)

# Mitigate concept drift
![image](https://github.com/user-attachments/assets/78f22b73-232d-4e46-9694-decee88f7028)
![image](https://github.com/user-attachments/assets/820942a5-3b5f-454b-bd30-35105337134a)
![image](https://github.com/user-attachments/assets/e9924d4c-c6db-453e-b3c4-2d411fc8d83a)
![image](https://github.com/user-attachments/assets/2777d0e3-0187-405b-927d-6d9d1e9c42df)








    



