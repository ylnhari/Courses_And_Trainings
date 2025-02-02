# Introduction to Machine Learning

## Artificial Intelligence vs. Machine Learning
Let's address a common point of confusion: the difference between Artificial Intelligence (AI) and Machine Learning (ML).  These terms are often used interchangeably, but they aren't the same. 
![image](https://github.com/user-attachments/assets/d58d6b27-f5b0-4b2b-9996-748eb075abf6)


### AI
AI is the broader field. It encompasses any technique that enables computers to mimic human intelligence. Think of it as the overarching goal: creating intelligent machines. Examples of AI include robots, self-driving cars, and even game-playing algorithms.It involves creating systems that can perform tasks that typically require human intelligence such as natural language, recognizing patterns and making decisions.
![image](https://github.com/user-attachments/assets/f335cec5-c30e-48b0-9be4-dbd36f77ba9b)


### Machine learning
Machine learning is a subset of AI.  It focuses on enabling computers to learn from data without explicit programming.  Instead of telling the computer exactly what to do step-by-step, we provide it with data, and it figures out the patterns and rules on its own.

![image](https://github.com/user-attachments/assets/958cb656-74eb-46ba-ab61-14be1f6dd748)

Imagine you want to teach a computer to recognize handwritten digits.  You could try to write a program with very specific rules for each digit, but that would be incredibly complex and wouldn't work well for variations in handwriting.  Machine learning offers a different approach.

Instead of writing explicit rules, we give the computer a large amount of data – in this case, lots of images of handwritten digits, each labeled with the correct number.  The machine learning algorithm then finds patterns in this data that connect the images to the correct labels.  It learns these patterns, so that when you give it a new image, it can predict what digit it represents.

Think of it like learning to ride a bike.  You don't learn by someone giving you a list of precise instructions. You learn by doing – by trying, falling, adjusting, and gradually getting better.  Machine learning is similar. The algorithm "tries" different approaches, gets feedback from the data, and adjusts its "strategy" until it can make accurate predictions.

Every machine learning system involves these key components:
- Data: The raw material. The more relevant and high-quality data you have, the better the machine can learn.
- Algorithm: The set of rules and techniques that the machine uses to learn from the data. There are many different algorithms, each suited to different types of problems.
- Model: The output of the learning process. The model represents the patterns the machine has learned from the data. It's what we use to make predictions on new data.

## Two main types of machine learning: supervised and unsupervised learning.
![image](https://github.com/user-attachments/assets/099e49f9-a2c1-4126-a363-1aac088cb4ea)

### Supervised Learning - The Dog and Cat Example
Imagine you have a huge collection of pictures of cats and dogs. You already know which picture is a cat and which is a dog.  You label each picture accordingly – this is called labeled data.  In supervised learning, you feed this labeled data to the machine. The machine learns the relationship between the pictures and the labels (cat or dog).  Then, when you give it a new picture, it can predict whether it’s a cat or a dog.  It learned from the examples you provided.
![image](https://github.com/user-attachments/assets/5cab5ba4-dec0-40cb-98fe-4cf7888f5993)

### Unsupervised Learning - The Dog Breed Example
Now, imagine a different scenario. You have pictures of various dog breeds, but you don't know the breed of each dog.  This is unlabeled data.  In unsupervised learning, you give this unlabeled data to the machine. The machine's job is to find patterns in the data and group similar pictures together.  It might discover clusters of pictures that correspond to different breeds, even though you didn't tell it what those breeds were.
![image](https://github.com/user-attachments/assets/a90bc376-98d0-4230-88eb-df99a1ef5426)
![image](https://github.com/user-attachments/assets/2ec24526-daa4-4237-b760-7776822acf47)

### Supervised vs Unsupervised Learning
Here's a summary of the key differences:
- Supervised Learning: Labeled data, task-driven (you have a specific prediction in mind), identifies a goal.
- Unsupervised Learning: Unlabeled data, data-driven (explores the data to find patterns), identifies a pattern.
The key takeaway: Supervised learning has "answers" (labels) provided, while unsupervised learning does not.
![image](https://github.com/user-attachments/assets/95fcd75c-bcc2-4bd5-b5f6-1d03e58cc5f7)

### Types of Supervised Learning
There are two main types of supervised learning:
- Classification: Predicts a category. Example: Is this email spam or not spam? (Categorical variable)
- Regression: Predicts a number. Example: What will the house price be? (Numeric variable)
![image](https://github.com/user-attachments/assets/4e2bff8e-bce3-4a78-8c8a-ae4408242ba6)

### Types of Unsupervised Learning
There are three main types of unsupervised learning:
- Clustering: Groups similar data points together. Example: Customer segmentation.
- Association: Finds relationships between variables. Example: Recommending products.
- Dimensionality Reduction: Reduces the number of features in a dataset. Example: Simplifying complex data for easier analysis.
![image](https://github.com/user-attachments/assets/30b994e5-aebf-4958-a564-fa86ac352674)

## Let's Test our understanding
### Scenario 1 - Customer Spending)
You're asked to predict customer spending based on their purchase history.
![image](https://github.com/user-attachments/assets/0c2c6d04-0928-4e9d-b25e-034133b2fc16)
 - Is this supervised or unsupervised learning?
 -  Is this a classification or a regression problem?


### Scenario 2 - Customer Segmentation
You're using the same dataset, but this time you want to identify customer segments without relying on pre-defined categories.
![image](https://github.com/user-attachments/assets/17e6adae-fa43-4305-b4c4-446b262944c3)

- Is this supervised or unsupervised learning?
- Is it a clustering, association, or dimensionality reduction problem?

## Deeplearning
Within machine learning, there's another important area called Deep Learning. This uses artificial neural networks with multiple layers to analyze data at a deeper level. We'll explore neural networks in more detail later, but for now, understand that deep learning is a powerful technique within the machine learning toolkit.
![image](https://github.com/user-attachments/assets/4e53a428-3890-4994-94a7-79b780e33f2a)


