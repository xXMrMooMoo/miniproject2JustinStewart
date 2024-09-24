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

def main():
    csvfile = "Impact_of_Remote_Work_on_Mental_Health.csv"
    df = pd.read_csv(csvfile, index_col=0)

    #   creating charts folder
    create_chart_folder()

    #   lists to iterate through
    stress_levels = ['High', 'Medium', 'Low']
    genders = ['Male', 'Female', 'Non-binary']
    colors = ['Red', 'Orange', 'Blue']

    #   looping through stress levels, gender, and colors to create bar graphs based on hours worked and stress level
    #   by gender.
    for stress, color in zip(stress_levels, colors):
        for gender in genders:
            filtered_df = df.loc[
                (df['Stress_Level'] == stress) &
                (df['Gender'] == gender) &
                (df['Hours_Worked_Per_Week'].between(30,40, inclusive='both'))
            ]
            plot_graph_based_on_hours(filtered_df, color, stress, gender)

#   function to plot and save the bar graph, name is created based on passed variables.
def plot_graph_based_on_hours(df, barColor, stressType, gender):
    count_by_hours = df['Hours_Worked_Per_Week'].value_counts().sort_index()

    #   setting and formatting the bar graphs
    plt.bar(count_by_hours.index, count_by_hours.values, color=barColor, edgecolor='black', linewidth=1.5)

    #   Labeling the graph
    plt.xlabel('Hours Worked Per Week')
    plt.ylabel(f'Count of {stressType} stress')
    plt.title(f'Count of {stressType} stress {gender} Working 30-40 Hours Per Week')

    #   alternate way to set plt.axis (x-axis range)
    plt.xticks(range(30,41))

    # Set the background color to light grey
    plt.gcf().set_facecolor('#A9A9A9')  # Set the figure background
    plt.gca().set_facecolor('#808080')  # Set the axes background

    plt.savefig(f'charts/{stressType}_Stress_{gender}.png')
    plt.show()

def create_chart_folder():
    if not os.path.exists("charts"):
        os.mkdir("charts")

if __name__ == '__main__':
    main()

