# Statistical-Analysis-of-cricket-Commentary
This project aims to collect cricket commentary text from a website and generate some Statistical Analysis. The main objective of this project are as folows:
1.To Develop a Real-Time Data Processing System that should efficiently convert unstructured text into structured data points for further analysis.
2.To Implement Natural Language Processing (NLP) for Entity Recognition to extract key entities from live cricket commentary, including player names, team names, scores, events(boundaries, wickets, sixes),
and conditions (pitch, weather).
3.To Analyze Player Performance and Dynamics: Use the structured data to conduct detailed statistical analyses on player performances, interactions between players (e.g., bowler vs. batsman dynamics),and team 
strategies, providing insights beyond basic scorecards.

The "main.py" file is used for scraping the website. We have used "https://www.india.com/" sports website to scrape the commentary text for a match.
Th "insights.ipynb" file uses Machine Learning alogrithm to clean the text data store in "trial_comm.txt" file. I have used NLP models to preprocess the commentary data and also add variuos entity int the NLP pipeline to extract the text required for analysis.
