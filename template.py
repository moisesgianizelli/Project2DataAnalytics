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
    # Merge the files using 'genre' column
    mostCommonGenre = movieFile['Genre'].value_counts().idxmax()
    leastCommonGenre = movieFile['Genre'].value_counts().idxmin()

    # Print the results
    print("Most common genre:", mostCommonGenre)
    print("Least common genre:", leastCommonGenre)

    # Print out the results
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
    
    
    
    
#def task3():
    # Read the movies data
    # movieFile = pd.read_csv('movies.csv')

    # # Convert 'Runtime' column to numeric, handling non-numeric values
    # movieFile['Runtime'] = pd.to_numeric(movieFile['Runtime'], errors='coerce')

    # # Display box plot to visualize outliers in Runtime
    # plt.figure(figsize=(10, 6))
    # plt.boxplot(movieFile['Runtime'].dropna(), vert=False)  # Drop NaN values for the boxplot
    # plt.title('Boxplot of Movie Runtimes')
    # plt.xlabel('Runtime (minutes)')
    # plt.show()

    # # Identify outliers based on the box plot
    # runtime_outliers = movieFile[movieFile['Runtime'] > movieFile['Runtime'].quantile(0.75) + 1.5 * (movieFile['Runtime'].quantile(0.75) - movieFile['Runtime'].quantile(0.25))]

    # # Print the titles of the movies considered as outliers
    # print("Movies with Outlier Runtimes:")
    # print(runtime_outliers[['Title', 'Runtime']])
#task3()  
    
    
    
def task4():

    numberOfVotes = movieFile['Number of Votes'].isnull().sum()
    rating = movieFile['Rating'].isnull().sum()

    print(f"Number of null values in 'Number of Votes': {numberOfVotes}")
    print(f"Number of null values in 'Rating': {rating}")

    # Fill null values with the average for each attribute
    movieFile['Number of Votes'].fillna(movieFile['Number of Votes'].mean(), inplace=True)
    movieFile['Rating'].fillna(movieFile['Rating'].mean(), inplace=True)

    # Visualize the relationship between 'number of votes' and 'rating'
    plt.figure(figsize=(10, 6))
    plt.scatter(movieFile['Number of Votes'], movieFile['Rating'], alpha=0.5)
    plt.title('Relationship between Number of Votes and Rating')
    plt.xlabel('Number of Votes')
    plt.ylabel('Rating')
    plt.show()

task4()
    
    
    
    
# def task5():
    
#     """
#     he main genre.csv file contains various main genres (see Column head-
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
    
    
    
    
    
# def task6():
    
#     """
#     Apply one analytical task of your choice. Make sure the chosen task is
#     useful for people in this industry and also complex enough. Use comment
#     section and explain the idea of your task. How the results should be
#     displayed? Please comment below this task’s function and explain the
#     expected output. Do not generate additional output.
#     """

