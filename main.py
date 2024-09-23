### INF601 - Advanced Programming in Python
### Justin Stewart
### Mini Project 2



#(5/5 points) Initial comments with your name, class and project at the top of your .py file.
#(5/5 points) Proper import of packages used.
#(20/20 points) Using a data source of your choice, such as data from data.gov or using the Faker package, generate or retrieve some data for creating basic statistics on. This will generally come in as json data, etc.
#Think of some question you would like to solve such as:
#"How many homes in the US have access to 100Mbps Internet or more?"
#"How many movies that Ridley Scott directed is on Netflix?" - https://www.kaggle.com/datasets/shivamb/netflix-shows
#Here are some other great datasets: https://www.kaggle.com/datasets
#(10/10 points) Store this information in Pandas dataframe. These should be 2D data as a dataframe, meaning the data is labeled tabular data.
#(10/10 points) Using matplotlib, graph this data in a way that will visually represent the data. Really try to build some fancy charts here as it will greatly help you in future homework assignments and in the final project.
#(10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
#(10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
#(10/10 points) I will be checking out the main branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.
#(20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown. Be thorough on the explanations.

import pandas as pd
import os
import matplotlib.pyplot as plt
from fontTools.misc.arrayTools import pointInRect


def main():
    csvfile = "Impact_of_Remote_Work_on_Mental_Health.csv"
    df = pd.read_csv(csvfile, index_col=0)

    #   Filtering df down to df's that are split by stress level.
    #   This creates a df that only returns the rows in which stress is high.
    #   If df['Stress_Level' == 'High'] == True, then that row is added to high_stress_df.

    stress_levels = ['High', 'Medium', 'Low']
    genders = ['Male', 'Female', 'Non-binary']
    colors = ['Red', 'Orange', 'Blue']

    #   looping thru stress levels, gender, and colors to create bar graphs based on hours worked and stress level
    #   by gender.
    for stress, color in zip(stress_levels, colors):
        for gender in genders:
            filtered_df = df.loc[
                (df['Stress_Level'] == stress) &
                (df['Gender'] == gender) &
                (df['Hours_Worked_Per_Week'].between(30,40, inclusive='both'))
            ]
            plotGraphBasedonHours(filtered_df, color, stress, gender)

#   function to plot and save the bar graph
def plotGraphBasedonHours(df, barColor, stressType, gender):
    count_by_hours = df['Hours_Worked_Per_Week'].value_counts().sort_index()

    plt.bar(count_by_hours.index, count_by_hours.values, color=barColor)
    plt.xlabel('Hours Worked Per Week')
    plt.ylabel(f'Count of {stressType} stress')
    plt.title(f'Count of {stressType} stress {gender} Working 30-40 Hours Per Week')
    plt.xticks(range(30,41))
    plt.show()


if __name__ == '__main__':
    main()

def createChartFolder():
    if os.path.exists("charts") == False:
        os.mkdir("charts")
