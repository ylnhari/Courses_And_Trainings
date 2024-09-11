# Why orchestrate your ML workflows?
  - Orchestration is about bringing standardization and software engineering and best practices to machine learning workflows so you can spend
  - more time focusing on solving your machine learning problem and have the details of your computing environment abstracted away.
<img width="1096" alt="image" src="https://github.com/user-attachments/assets/4e4a88cc-665a-4210-b6f1-66fbd22140ce">

# First step -> is to create TFX pipeline Iteratively using notebook.
  - You can build your pipeline iteratively using an interactive context object, as shown to handle component execution and artifact visualization in embedded HTML windows within the notebook.
<img width="595" alt="image" src="https://github.com/user-attachments/assets/caba4004-f042-4122-b6fc-ab85d900800a">
- Although notebooks are great for experimentation and interactive execution, they do not have a level of automation for continuous training and computation necessary for production machine learning.
- Different orchestrators are needed to serve as an abstraction that sits over the computing environment that supports your pipeline scaling with your data.
- TFX supports orchestrators, such as Apache airflow, Kubeflow Pipelines, and Apache Beam.

<img width="617" alt="image" src="https://github.com/user-attachments/assets/2c662af2-7d0a-44dc-8059-31c3e40a6c43">


