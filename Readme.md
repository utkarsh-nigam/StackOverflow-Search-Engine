
# StackOverflow-Search-Engine 

## Introduction

Stack Overflow is the largest and most popular online community for programmers to learn and share knowledge. Due to its increasingly high user-base, the website has experienced a combination of repetitive and synonymous questions creating clutter in the repository. The clutter interferes with Stack Overflow’s ability to generate accurate query results for its users. While various attempts to refine Stack Overflow’s query results have been made through Kaggle Notebooks, they were generally limited to identifying patterns and trends in topics and programming languages. (Mooney, 2020) Our research shows that no attempts have been made to develop an algorithm that not aims to decrease redundancy but also returns existing or synonymous posts to address the users' query. The objective of this project is to implement natural language processing algorithms that will declutter the Stack Overflow repository and offer users high-quality query results. By identifying and reorganizing the most impactful posts, the project aims to minimize time and effort for the user.


## Dataset

Though discovered on Kaggle, the dataset is an accumulation of archived data sourced from a Google BigQuery pull from the Stack Exchange Data Explorer. The original dataset offers 17 tables and 118 million observations which includes timestamp, content, tags, responses, and scores posted ranging from July 2008 to September 2020. However, due to the volume of the dataset, the scope of the project was reduced to 2.3 million observations focusing on the language with the most frequent questions: python. These questions were primarily centered around Machine Learning, Visualization, Python Basics, Web Scraping, Application Building, and Dataframes. These clusters paved the way to once again reduce scope down to only  include posts that include the most popular tag among the top 50: Pandas. While most tags centered around certain topics, to create constraints in this project, we had to filter out the ‘stray’ tags. The resulting dataset size is 0.13 million rows.


## Text Pre-Processing
To prepare the dataset, we began by identifying and eliminating null values. Then, synonymous and duplicate posts were compiled and clustered to aggregate scores by appropriate votes. Column-wise pre-processing enabled tokenization that paved the way to remove stop-words from both the title and question, punctuation marks, tags from the header, paragraph, and code. The overall score matrices were then normalized and multi-label classification was converted into one hot encoded tag column to avoid biases in machine learning classification.


![Alt text](/assets/img/preprocessing1.png?raw=true "")

![Alt text](/assets/img/preprocessing2.png?raw=true "")


## Results
![Alt text](/assets/img/results.png?raw=true "")

## Conclusion
This project is an effort to declutter the Stack Overflow repository to increase the accuracy of the query results. 
