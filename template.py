#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nov/23

Student Name: Moises Munaldi

Student ID: R00225292

Cohort: evSD3

"""
import pandas as pd
#import matplotlib.pyplot as plt


def task1():
    # read the files normally
    movieFile = pd.read_csv('movies.csv')
    mainGenreFile = pd.read_table('main-genre.txt')

    # print the columns to identify the common column
    # print("Columns in movies_df:", movieFile.columns)
    # print("Columns in main_genre_df:", mainGenreFile.columns)

    # print("Head of main_genre_df:\n", mainGenreFile.head())
    # print("First few rows of movies:")
    # print(movieFile.head())

    # print("\nFirst few rows of main_genre:")
    # print(mainGenreFile.head())

    # common_columns = set(movieFile.columns) & set(mainGenreFile.columns)
    # print("Potential common columns:", common_columns)

    # identifying the actual name of the column that is common between the two DataFrames
    #print("Columns in movies:", movieFile.columns)
    #print("Columns in main_genre:", mainGenreFile.columns)

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

    # top_genres = mergingFiles['main_genre'].value_counts().nlargest(8)
    # plt.figure(figsize=(10, 6))
    # plt.bar(top_genres.index, top_genres.values, color='skyblue')
    # plt.title('Top 8 Popular Genres')
    # plt.xlabel('Main Genre')
    # plt.ylabel('Number of Movies')
    # plt.xticks(rotation=45)
    # plt.show()

task1()



# def task2():
    
#     """
#     What is the most and least common genre? Note that there are two
#     columns related to genres: ’genre’ and ’main genre.’ For this task, the
#     ’genre’ attribute is the focus, not ’main genre. How the results should
#     be displayed? Only print the most and the least common genres and
#     nothing else
#     """
    
    
    
    
# def task3():
    
#     """
#     Apply an appropriate visualization technique to display the outliers in
#     movie duration (Runtime). Print the names of the movies for which the
#     duration is considered an outlier. How the results should be dis-
#     played? Only print the title of the movies that belong to the outliers.
#     Also display the visualization - no need to save the visualization in any
#     file.
#     """
    
    
    
    
    
# def task4():
    
#     """
#     Apply an appropriate visualization technique to analyze the relationship
#     between the ’number of votes’ and the ’rating’. Report if there are any
#     null values in either of the mentioned attributes. If any null values are
#     found, they should be filled with the average of the existing values for each
#     attribute prior to the visualization. Note the difference scale of the two
#     attributes, ’number of votes’ and the ’rating’. How the results should
#     be displayed? Write a short comment below this task’s function and
#     explain the the existence of null values in those attributes/columns. Also
#     display the figure. No need to save the visualization in any file.
#     """
    
    
    
    
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

