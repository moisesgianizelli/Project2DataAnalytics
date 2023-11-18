#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nov/23

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
    #print(movieFile.columns)
    #print(mainGenreFile.columns)

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
    #read it better
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

    topGenres = movieFile['Genre'].value_counts().nlargest(16)
    plt.figure(figsize=(10, 6))
    plt.bar(topGenres.index, topGenres.values, color='red')
    plt.title('Top 15 Genre Distribution')
    plt.xlabel('Genre')
    plt.ylabel('Number of Movies')
    plt.xticks(rotation=45)
    plt.show()


# Call the function to execute the task
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

    # Display box plot to visualize outliers in Runtime
    #plt.figure(figsize=(10, 6))
    # extract the column 'Runtime', making a horizontal boxplot with box type
#    movieFile['Runtime'].plot(kind='box', vert=False)
#    plt.title('Boxplot of Movie Runtimes')
#    plt.xlabel('Runtime (minutes)')
#    plt.show()
    # calculate the first quartileof the 'Runtime'
#    q1 = movieFile['Runtime'].quantile(0.25) 
    # calculate the third quartiles
#    q3 = movieFile['Runtime'].quantile(0.75)

    #movieFile['Runtime'] = pd.to_numeric(movieFile['Runtime'], errors='coerce')
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

    # Define outlier bounds
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
#investigate why it is printing duplicated data

#task3()  
    
    
    
def task4():

    # Fill null values with the average for each attribute - commom strategy to handle missing data fillna method is used to replace null values with the specified value

    # movieFile['Number of Votes'].isnull(): This creates a boolean Series where each element is True if the corresponding value in the 'Number of Votes' column is null and False otherwise.

    # .sum(): This sums up the boolean values. Since True is treated as 1 and False as 0 when summed, you effectively get the count of True values, which corresponds to the number of null values in the 'Number of Votes' column.

    # nullVotes = This count is then stored in the variable nullVotes. The same logic applies to counting null values in the 'Rating' column.

    movieFile['Number of Votes'].fillna(movieFile['Number of Votes'].mean(), inplace=True)
    movieFile['Rating'].fillna(movieFile['Rating'].mean(), inplace=True)

    # isnull() method, which returns a boolean and associating with sum() the program tells us how many null exist in the file
    nullVotes = movieFile['Number of Votes'].isnull().sum()
    nullRating = movieFile['Rating'].isnull().sum()

    print("Number of null values in Number of Votes:", nullVotes)
    print("Number of null values in Rating:", nullRating)

    # Visualize the relationship between 'number of votes' and 'rating'
    # plt.figure(figsize=(10, 6))
    # plt.scatter(movieFile['Number of Votes'], movieFile['Rating'], alpha=0.5)
    # plt.title('Relationship between Number of Votes and Rating')
    # plt.xlabel('Number of Votes')
    # plt.ylabel('Rating')
    # plt.show()

#task4()
    
    
    
    
def task5():
    
#     """
#     The main genre.csv file contains various main genres (see Column head-
#     ers). Each main genre (column header) is associated with multiple terms.
#     For instance, fantasy is associated with Imagination, Reverie, Dream,
#     Delusion, and more. Please open the file to view its contents.
#     Your task is to read the main genre.csv file and, for each main-genre,
#     select a group of movies in the (movies.csv) file whose synopses contain one
#     or more terms associated with the given main genre in main genre.csv.
#     After forming this group, further analysis is required to determine which
#     main genre in movies.csv in that group has the highest frequency.
#     Please note that the words in the Synopsis need to be lower-cased and
#     cleansed by removing the following noises: [’,’, ”’, ’.’, ’-’]. The terms from
#     the main-genres file should also be lower-cased.
#     How the results should be displayed? There are 8 main-genres in
#     the main genre.csv. For each main-genre, print the main-genre (the one
#     in main genre.csv, column header) itself, and next to it, print the most
#     frequent main genre related to the group of movies from movies.csv. For
#     example, the ’fantasy’ main-Genre in main genre.csv appears in many
#     movie synopses where the main genre of those movies is also ’fantasy.’
#     Do not print or output anything else. Only 8 main-genres, and for each
#     main-genre, the main genre with the highest frequency.
#     """
    print("oi")
    
#task5()    
    
    
def task6():
# Load the movies dataset
# Extract relevant columns
    ratings_data = movieFile[['Release Year', 'IMDb']].copy()

# Convert 'Release Year' to numeric, coerce errors to NaN
    ratings_data.loc[:, 'Release Year'] = pd.to_numeric(ratings_data['Release Year'], errors='coerce')

# Drop rows with NaN values in 'Release Year' and 'IMDb'
    ratings_data = ratings_data.dropna(subset=['Release Year', 'IMDb'])

# Group by release year and calculate the average rating
    average_ratings = ratings_data.groupby('Release Year')['IMDb'].mean().reset_index()

# Plotting trends
    plt.figure(figsize=(10, 6))
    plt.plot(average_ratings['Release Year'], average_ratings['IMDb'], marker='o')
    plt.title('Average IMDb Rating Trends Over Time')
    plt.xlabel('Year')
    plt.ylabel('Average IMDb Rating')
    plt.grid(True)
    plt.show()
task6()
