# Student Performance Analysis & Prediction

This project analyzes student performance using Python data analysis and visualization tools.  
The goal is to explore student scores, visualize trends, and build a simple model to predict whether a student will pass or fail.

The analysis is implemented in a Jupyter Notebook called:

part4_visualization_ml.ipynb

## Dataset

The dataset `students.csv` contains information about students including:

- Name
- Subject scores (Math, Science, English, History, PE)
- Attendance percentage
- Study hours per day
- Pass/Fail status

## Tasks Implemented

### Task 1 – Data Exploration
Using the pandas library:
- Load the dataset
- Display the first 5 rows
- Check dataset shape and data types
- Generate summary statistics
- Compare average subject scores for pass vs fail students
- Identify the student with the highest overall average

### Task 2 – Data Visualization (Matplotlib)
The following plots are created:

1. Bar chart – Average score per subject
2. Histogram – Distribution of Math scores
3. Scatter plot – Study hours vs average score
4. Box plot – Attendance comparison between pass and fail students
5. Line plot – Math vs Science scores across students

### Task 3 – Visualization with Seaborn
Additional visualizations using seaborn:

- Bar chart comparing Math scores for pass vs fail students
- Scatter plot showing attendance vs average score

### Task 4 – Machine Learning Model
A Logistic Regression model is used to predict student pass/fail outcomes.

Steps include:
- Splitting the dataset into training and testing sets
- Scaling features
- Training the model
- Evaluating model accuracy
- Displaying feature importance

## Generated Plots

The notebook generates the following image files:

plot1_bar.png  
plot2_hist.png  
plot3_scatter.png  
plot4_box.png  
plot5_line.png  
plot6_seaborn_bar.png  
plot7_seaborn_scatter.png  

