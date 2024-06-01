# Components of a production machine learning system
![image](https://github.com/ylnhari/Courses_And_Trainings/assets/45874226/1a90be16-075b-4c15-839a-af0010cf884d)

# Production ML System Flow Chart
![image](https://github.com/ylnhari/Courses_And_Trainings/assets/45874226/491832c0-51d5-4b24-a73a-11de0c2fc33c)

# Data Handling
## Types of Data
![image](https://github.com/ylnhari/Courses_And_Trainings/assets/45874226/34bf23e8-4175-4a2e-bf66-573b9b8ebd88)
## After data Extraction , during data analysis , what happens ?
![image](https://github.com/ylnhari/Courses_And_Trainings/assets/45874226/7006428e-d642-4099-86d7-42500bfda91e)
## Data Preparation involves ?
![image](https://github.com/ylnhari/Courses_And_Trainings/assets/45874226/0fddaf75-99c9-4e8f-adce-e0bc053ceb3c)

# Model Training, Evaluation, Validation
## Model Training 
  - incrementally improve model's predictive ability.
## Model Evaluation
  - Model evaluation consists of a person or a group of people evaluating or assessing the model, with respect to some business-relevant metric like AUC, area under the curve, or cost weighted error.
  - If the model meets their criteria, it is moved from the assessment phase to development.For example, in the development phase, you may want to modify hyperparameter values to increase the model's performance, which correlates to improvements in evaluation results.
  - After development, the model is then ready for a live experiment or real-world test of the model.
    ![image](https://github.com/ylnhari/Courses_And_Trainings/assets/45874226/b7bbde95-ecf4-4f0d-9530-0449a051a6a7)
## Model Validation
  - In contrast to the model evaluation component, which is performed by humans, the model validation component evaluates the model against fixed thresholds and alerts engineers when things go wrong.

# Trained model, Prediction Service, Performance Monitoring
  - The output of model validation is a trained model that can be pushed to the model registry.
  - The machine learning model registry is a centralized tracking system that stores linage, versioning, and related metadata for published machine learning models. A registry may capture governance data required for auditing purposes, such as who trained and published a model, which datasets were used for training, the values of metrics measuring predictive performance, and when the model was deployed to production.
  - deploy model for serving.
    ![image](https://github.com/ylnhari/Courses_And_Trainings/assets/45874226/9771f7a6-76b4-48d9-949c-4e70b0809300)
  - As a best practice, you need a way to actively monitor the quality of your model in production.
  - The output of monitoring for these changes then feeds into the data analysis component, which can serve as a trigger to execute the pipeline or to execute a new experimental cycle.
  - What can be monitored?
    ![image](https://github.com/ylnhari/Courses_And_Trainings/assets/45874226/07ce9156-5219-4dc9-adb7-86c93af62d73)

# Training design decisions
  - Types of Training: If the relationship you're trying to model is constant, like physics, a statically trained model may be sufficient.If, in contrast, the relationship you're trying to model is one that changes, like fashion, the dynamically trained model might be more appropriate.
  - Part of the reason the dynamic is harder to build and test is that new data may have all sorts of bugs in it.
  - Engineering might also be harder because we need more monitoring, model rollback, and data quarantine capabilities.
02:04
Let's explore some use cases and think about which sort of training style would be most appropriate.
  ![image](https://github.com/ylnhari/Courses_And_Trainings/assets/45874226/ac829e35-c0f2-4cc3-9c1a-333595182806)
  ![image](https://github.com/ylnhari/Courses_And_Trainings/assets/45874226/0800a8c6-589f-4fc5-a8e3-39f96b11edc3)









