#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
last update: 19/11/23

Student Name: Moises Munaldi

Student ID: R00225292

Cohort: evSD3

"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


movieFile = pd.read_csv('movies.csv')
mainGenreFile = pd.read_table('main-genre.txt')


def task1():
    # read the files normally
    # movieFile = pd.read_csv('movies.csv')
    # mainGenreFile = pd.read_table('main-genre.txt')
    # identifying the actual name of the column that is common between the two DataFrames
    # print the columns to identify the common column
    # print(movieFile.columns)
    # print(mainGenreFile.columns)
    # print(mainGenreFile.head())
    # print(movieFile.head())
    # print(mainGenreFile.head())
    # print(movieFile.columns)
    # print(mainGenreFile.columns)

    # merge the files using pd from pandas in a variable
    # inner: inner merge returns only the rows that have matching values in both DataFrames. Rows with non-matching values are excluded from the result.
    mergingFiles = pd.merge(movieFile, mainGenreFile, how='inner', left_on='main_Genre', right_on='fantasy')

    # Getting the requirements: 1) total unique genres, most popular genre and least popular genre
    totalUniqueGenres = mergingFiles['main_Genre'].nunique()  # pandas function
    # value_counts counts the occurrences of each unique value in the column, creating a Series with the counts.
    # idxmax() returns the index
    # idxmin() returns the index
    mostPopularGenre = mergingFiles['main_Genre'].value_counts().idxmax()
    leastPopularGenre = mergingFiles['main_Genre'].value_counts().idxmin()

    # print out the results
    print("Total unique genres: ", totalUniqueGenres)
    print("Most popular: ", mostPopularGenre)
    print("Least popular: ", leastPopularGenre)

    # Now we use matplotlib to generate the datas
    # mergingFiles['main_Genre'].value_counts(): This part counts the occurrences of each unique value in the 'main_Genre' column. nlargest(8): This method selects the 8 largest counts. So, topGenres contains the top 8 genres and their respective counts.
    topGenres = mergingFiles['main_Genre'].value_counts().nlargest(8)
    # this one creates a figure 10 x 6
    plt.figure(figsize=(10, 6))
    #(x,y) sizes with the layout
    plt.bar(topGenres.index, topGenres.values, color='green')
    # print up the information
    plt.title('Top 8 Popular Genres')
    plt.xlabel('Main Genre')
    plt.ylabel('Number of Movies')
    # read it better
    plt.xticks(rotation=45)
    plt.show()

#task1()



def task2():

    #print(movieFile['Genre'].unique())
    #print(movieFile['Genre'].dtype)
    # Merging the files
    mostCommonGenre = movieFile['Genre'].value_counts().idxmax()
    leastCommonGenre = movieFile['Genre'].value_counts().idxmin()
    print("Most common genre: ", mostCommonGenre)
    print("Least common genre: ", leastCommonGenre)

    #same as task1
    topGenres = movieFile['Genre'].value_counts().nlargest(16)
    plt.figure(figsize=(10, 6))
    plt.bar(topGenres.index, topGenres.values, color='red')
    plt.title('Top 15 Genre Distribution')
    plt.xlabel('Genre')
    plt.ylabel('Number of Movies')
    plt.xticks(rotation=45)
    plt.show()

#task2()
    
    
    
    
def task3():
    """"    
    boxplot is a statistical visualization tool that provides a concise summary of the distribution of a dataset. It is particularly useful for identifying outliers and understanding the central tendency and spread of the data
     - Identify outliers, because boxplots are effective in visually highlighting potential outliers in a dataset
     - A boxplot provides a clear summary of the distribution of the data
     - If you have multiple groups or categories of movies, a boxplot can help compare the distributions of runtimes across different groups
     https://www.geeksforgeeks.org/finding-the-outlier-points-from-matplotlib/
    
    obs: my first approach to solve this task  was with matpltlib, but it was too dificult to get the result. So I found more documentation using numpy:
    https://medium.com/@dark.coding/finding-outliers-in-dataset-using-python-ffd2f585589c
    https://www.geeksforgeeks.org/numpy-percentile-in-python/
    """
    # movieFile['Runtime'] = pd.to_numeric(movieFile['Runtime'], errors='coerce')
    # Convert 'Runtime' column to numeric, extracting numeric values from strings

    #debugging
    # print("Original 'Runtime' column:")
    # print(movieFile['Runtime'])

    # Convert 'Runtime' column to numeric, extracting numeric values from strings
    movieFile['Runtime'] = movieFile['Runtime'].apply(lambda x: int(''.join(filter(str.isdigit, str(x)))) if pd.notna(x) else np.nan)

    # Calculate quartiles and IQR using numpy
    q1 = np.percentile(movieFile['Runtime'].dropna(), 25)
    q3 = np.percentile(movieFile['Runtime'].dropna(), 75)
    iqr = q3 - q1

    # outlier bounds
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    # print("Lower Bound:", lower_bound)
    # print("Upper Bound:", upper_bound)

    # Identify outliers using numpy
    outliers = movieFile[(movieFile['Runtime'] < lower_bound) | (movieFile['Runtime'] > upper_bound)]

    # Print titles of movies considered as outliers
    if not outliers.empty:
        print("\nMovies with outlier runtimes:")
        for title in outliers['Title']:
            print(title)
    else:
        print("No outliers found.")
# movieFile = movieFile.drop_duplicates(subset=['Title'])
# investigate why it is printing duplicated data

#task3()  
    
    
    
def task4():

    #fills missing (NaN) values in the 'Number of Votes' column of the movieFile DataFrame. The fillna method is used to replace NaN values
    movieFile['Number of Votes'].fillna(movieFile['Number of Votes'].mean(), inplace=True)
    #  same but noe in 'Rating'
    movieFile['Rating'].fillna(movieFile['Rating'].mean(), inplace=True)

    # isnull() method, which returns a boolean and associating with sum() the program tells us how many null exist in the file
    nullVotes = movieFile['Number of Votes'].isnull().sum()
    nullRating = movieFile['Rating'].isnull().sum()

    print("Number of null values in Number of Votes:", nullVotes)
    print("Number of null values in Rating:", nullRating)

    # printing 0, is that right?
#task4()
    
    
    
    
def task5():
    """""
    Dont get this question, so I will be trying to solve what the task wants breaking down in smaller tasks.
    """""
    #  Your task is to read the main genre.csv file DONE

    # for each main-genre, select a group of movies in the (movies.csv) file whose synopses contain one or more terms associated with the given main genre in main genre.csv.

    # Please note that the words in the Synopsis need to be lower-cased and cleansed by removing the following noises: [’,’, ”’, ’.’, ’-’]. DONE
    # The terms from the main-genres file should also be lower-cased. DONE
    movieFile['Synopse'] = movieFile['Synopsis'].str.lower().replace('[’“”\.\-]', '', regex=True)
    mainGenreFile.iloc[:, 1:] = mainGenreFile.iloc[:, 1:].applymap(lambda x: x.lower() if pd.notna(x) else x)

    # after forming this group, further analysis is required to determine which main genre in movies.csv in that group has the highest frequency.
    # form a group ?

    group = []
    for i in range(1, len(mainGenreFile.columns)):
        main_genre = mainGenreFile.columns[i]
        movies = movieFile[movieFile['Synopse'].str.contains('|'.join(mainGenreFile[main_genre].dropna()))]

    # how to calculate now the most frequent genre?
    # should I put in a new data frame?
    # how to print?    
    


#task5()    
    
    
def task6():


    """"    
    My first idea was: Identifying Trends in Movie Ratings, analyze the trends in movie ratings over the years but I was gettting too many problems, so I decided to go for Plooting trends.
    I decided to create a bar plot to analyse the each genre in a specific year. This approach is good (and complex enough in my opinion) because follows the same structure that I have been doing also 
    helps to identify patterns and trends. As I really like to see data over the years, we can basically identify trends, most popular genres and we can make future decision with that. This can be good for movie industry because
    the industry can map audience preferences and choose to invest in similar projects.
    https://www.analyticsvidhya.com/blog/2021/08/understanding-bar-plots-in-python-beginners-guide-to-data-visualization/
    https://www.geeksforgeeks.org/matplotlib-pyplot-tight_layout-in-python/
    https://builtin.com/data-science/pandas-pivot-tables
    """

    #extract the columns I want to check
    getGenre = movieFile[['Release Year', 'main_Genre']]

    """""
     as this Release year column has "broken" data, I need to convert it to numerci values, and remove row with NaN values. Obs: that part took me almost one day to solve
     https://www.easytweaks.com/convert-pandas-column-to-numeric-types/
     https://sparkbyexamples.com/pandas/pandas-drop-rows-with-nan-values-in-dataframe/#:~:text=You%20can%20use%20the%20dropna,the%20DataFrame%20after%20removing%20rows.
    """

    getGenre.loc[:, 'Release Year'] = pd.to_numeric(getGenre['Release Year'].str.extract('(\d+)', expand=False), errors='coerce')
    getGenre = getGenre.loc[getGenre['Release Year'].notna() & getGenre['main_Genre'].notna()]

    # count the occurrences of each genre in each year. size() grouped series or dataframe with the grouping column as the index. 
    # reset index() is used to reset the index, and name='Count' is used to assign a name to the newly created count column.
    countsGenre = getGenre.groupby(['Release Year', 'main_Genre']).size().reset_index(name='Count')

    # each genre in a column 
    genreInColumn = countsGenre.pivot(index='Release Year', columns='main_Genre', values='Count').fillna(0)

    # plotting trends
    plt.figure(figsize=(15, 8))
    genreInColumn.plot.bar(stacked=True, ax=plt.gca())
    plt.title('Genre Popularity Trends Over Time')
    plt.xlabel('Year')
    plt.ylabel('Count')
    plt.grid(True)
    plt.legend(title='Genre', bbox_to_anchor=(1, 1), loc='upper left')

    plt.tight_layout()
    plt.show()


task6()
