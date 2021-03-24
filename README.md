# Election Analysis Results

## Overview of Election Audit
### Purpose
In this project, the Colorado Board of Elections has asked for an election analysis audit for a recent congressional election. In the sections below, I will discuss the process for completing the analysis and give detailed results of the election.

### Process
To do the analysis, we received raw voting data in *election_results.csv*. To parse this data, I created a script using Python. The script runs through the data to come up with the list of candidates and counties. 

To tabulate the votes for each candidate, I created a dictionary to hold both each candidate’s name and a tabulation of their votes. 
1.	Create “candidate_votes” dictionary and a “county_votes” dictionary.
2.	Go through the rows of voting data.
a.	Add each candidate and county to the corresponding dicitonary.
b.	For each vote, increase the vote by 1 for each of three places:
i.	The total vote
ii.	The candidate voted for
iii.	The county voted in
3.	Once the votes have all been tabulated, use the total to create percentage of the votes for each county and each candidate.
4.	Determine the winning candidate and the county with the highest turnout
5.	Report the details to a text file that can be shared with the board of elections.

Here is an example of the code showing how the candidate votes are initiated (the indented portion) and then how the votes are added.
‘‘‘
   For each row in the CSV file.
    for row in reader:
        # Get the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate add it to the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
‘‘‘

After the analysis is complete, the script also writes a summary showing the lists of candidates and counties with the number of votes cast and percentage of the vote. The file also lists the winner and states the county with the best turnout. 

Here is an example of the code showing how a portion of the text file is created:

![ElectionsOutput](https://github.com/DeliaDavila/Election_Analysis/blob/main/Images/ElectionsOutput.png)

And here is the resulting text file created by the script:

![ElectionsOutputFile](https://github.com/DeliaDavila/Election_Analysis/blob/main/Images/ElectionsOutputFile.png)


## Election Audit Results
Here are the results from the election.
### Votes cast in this congressional election
The total votes cast in all three counties of the precinct: 369,711

###  Votes by County
Overview of votes and percentage of total in each county of the precinct:
    * Arapahoe: 24,801 (6.7%)
    * Denver: 306,055 (82.8%)
    * Jefferson: 38,855 (10.5%)

### County with Best Turnout
Denver county had the best turnout. 
    * Votes cast: 306,055
    * Percentage of total votes: 82.8%

###  Votes by Candidate
    * Raymon Anthony Doane: 11,606 (3.1%) 
    * Charles Casper Stockham: 85,213 (23.0%)
    * Diana DeGette: 272,892 (73.8%)

###  Winning Candidate
Diana DeGette was declared the winner. 
    * Votes received: 272,892
    * Percentage of total votes: 73.8%

## Election Audit Summary 
### Overview
As the results show, the analysis was successful in tabulating votes for the precinct, as well as determing a winner and deciding which county had the best turnout.
I hope the Board of Elections is satisfied with the analysis. This script was written so that it can be used for other elections, so I hope you will consider me for future projects.
 
### Suggestions for future projects
The current script would be ideal for similar elections at the county level, but could also be expanded for use in other elections. The scope could be easily adjusted to tabulate votes in multiple elections. The data would just need to include additional columns for those votes and I could add additional coding to make the script loop through those additional contests and report them in new sections. It is also possible to adjust the script to count votes for a city as well as a county level.

And while I do not recommend engaging in partisan politics, I could report on votes gotten by different parties if the voting data included the party of the voters and/or the candidates. This, while it tends not to be terribly helpful in real life, would be helpful if the focus of the project were expanded to include national elections.


