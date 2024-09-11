<img width="525" alt="image" src="https://github.com/user-attachments/assets/b2565bce-d898-4ba5-8764-3ca2234e7c87"># Why orchestrate your ML workflows?
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
  <img width="611" alt="image" src="https://github.com/user-attachments/assets/daf56639-8998-4519-aaf1-2e52f7e26ab6">

# Apache Beam
## Why Apache beam ?
  - TFX abstracts away data processing for me, why do I need to learn another framework?
  - Beam is an abstraction worth learning, because of its incredible flexibility and unification of batch and stream data processing that underpins TFX pipelines.
  - learn Beam, write code once, and don't worry about scaling data processing again with Apache Beam.
  <img width="522" alt="image" src="https://github.com/user-attachments/assets/818af717-2d85-4ae7-9eea-7ba4d1c559b3">
  <img width="521" alt="image" src="https://github.com/user-attachments/assets/71d8a70c-c457-4be8-9baa-0cc51f3e61e7">
  - The Beam software development kit can work within numerous runtimes including full operating system, Python, or Docker containers, and translate that to a distributed compute cluster via a runner.
  - Beam abstracts away an incredible amount of complexity to distribute your TFX pipeline data processing into a distributed graph.
   <img width="525" alt="image" src="https://github.com/user-attachments/assets/2fcd8bd2-2525-4a9b-9a5e-2be65253ffb3">
   <img width="521" alt="image" src="https://github.com/user-attachments/assets/6653a71b-7489-4d11-bc00-f6af3458306a">
   <img width="533" alt="image" src="https://github.com/user-attachments/assets/7393ef61-bb15-4d38-b085-7bfb071ee0be">
   <img width="524" alt="image" src="https://github.com/user-attachments/assets/9e8cd120-4b29-4824-9f50-227c6665eaac">
   <img width="538" alt="image" src="https://github.com/user-attachments/assets/3ae6faff-7fb3-4af7-bc47-4fe049100302">
   <img width="528" alt="image" src="https://github.com/user-attachments/assets/1d3aacb1-6b6d-46fd-8dd1-cbc051ab7722">













