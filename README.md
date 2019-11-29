# CS34012 Measuring Software Engineering

    1. Measuring Engineering - a report
    2. GitHub Access 
    3. Social Graph


## 1. Meausuring Software Engineering- a report 
This is a paper exploring how software metrics can and is done, the ethical implications of the practice of evaluating engineers and the usefulness of it.

The Meausring software engineering paper is in PDF format entitled 'Measuring Software Engineering', and can be found in the main directory of this repository.

## 2. GitHub Access 
This assignment was a precursor to the final Social Graph assignment. The task was to interrogate the GitHub API to retrieve and display data regarding the logged in developer. 
To familiarise myself with the basics of the GitHub API, I chose to do a small application in python that displays data about the users followers and repositories in the terminal. To build this simple terminal application I used the github3.py (https://github3.readthedocs.io/) library instead of accessing the bare API.

The python file GitInterrogation.py file can be found in the GitInterrogation folder. 
### Dependencies
Python must be installed

    sudo apt-get install python3.6.
github3.py must be installed 

    pip install github3.py

To run the program, navigate into the folder where you have saved the project. Run the following command in the terminal

    python fileName.py

Before running the file must be edited to have the username and password of the account to be accessed.

## 3. Social Graph 
This assignment follows on from the GitHub Access assignment. The task was to interrigate the GitHub API to build visualisation of data available. The suggested tool for visualisation was the d3js library (https://d3js.org).

### My Idea
For this assignment I wanted to look at the relationship between the amount of langauges a user has included in their public repositories, and the amount of followers they have. In other words, does knowing a lot of programming langauges make you popular on GitHub?

### Different Components
#### Welcome Page and Searching for a User
The application is a web application that I ran locally. There is a welcome page and this is followed by a search bar that takes a string inputted by the user and finds that github user. A secondary data page is then generated for that users profile which contains the data visualisation for that user. 

#### User Profile
The first component I built was a simple Information profile on the GitHub. It interrogates the API using the oktokit library to retrieve data about the user searched for and then displays that data in a user profile component along with their avatar.

#### Language Breakdown
I built a function that again uses oktokit to interrogate the API to retrieve the list of repositories of a user and the list of languages from each repository. This method returns the langauges and their occurency as an object to a method to create the pie chart. I then built a pie chart that displays the languages found in their profile and the percentage of the users repositories in each language.This gives the searcher an insight into the variety of languages in a github users repoirtoire. 

#### Language vs Follower Count for a small Community 
My third and fourth graphs attempted to count the number of languages of a user and compare it to their follower count. The third was two interactive buttons that display language vs follower count for the searched user, used mainly for debugging while I developed the method to count languages in a profile. The fourth was a scatter plot graph. The scatter plot intends to display the relationship of language count vs follower count for each of the searched users followers. The aim here was to visualise the correlation between popularity of users in a mini-community and their language count, using a scatter plot graph. 

I eventually got the algorithm to count languages to work for the buttons and it also works for the scatter plot graph. The two algorithims correctly retrieve and calculate the number of languages in a users profile. The interactive buttons do display the users follower count vs their language count. However, I ran into more issues when trying to return the count of languages to the graphData. Therefore the graph does not display the scatter plot correctly.

Screenshots of all the working parts of my project can be seen in the images folder in the main directory of the repository.

### Technical Decisions
I also wanted to challenge myself with this assignment to use an unfamilar framework and graphing library.
The assigment is done using vue.js framework and d3.js library to build visualisations. Octokit/rest.js is used to interrogate the API. This nay not have been the best decision in hindsight, as perhaps a more familar framework would have enabled me to fully complete the fourth graph to correctly display the data retrieved from the API. 
 The assignment is located in GitInterrogation/githubSocialGraph. 
 The dependencies for this assignment can be found in the ReadMe.md in the socical graph folder.
 A github personal access token is required to run this. It may be inserted in the env file where currently is token.


