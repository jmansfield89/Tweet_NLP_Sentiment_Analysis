# Tweet_NLP_Sentiment_Analysis
Run a sentiment analysis on the replies to a tweet

Objective: Understand public reaction of a Tweet by analyzing the sentiment of each reply.

Analysis: This app runs sentiment analysis on 10,948 replies to a Facebook Tweet announcing their rebranding to Meta on 10/28/2021. Link to Tweet: https://twitter.com/Meta/status/1453795115701440524

Results: Most frequent sentiment category for the replies to this Tweet: Neutral

Notes:<br>
-The VADER model was used to analyze the sentiment of each reply: https://github.com/cjhutto/vaderSentiment<br>
-Due to Twitter developer policies, I am not able to share the data set of downloaded Tweet replies so my DATA EXTRACTION and DATA CLEANSING steps are not shown at this time but will be added soon!

Plans for Version 2.0: <br>
-Formulate method for cleaning Tweet replies, such as removing those that are from bots or are spam.<br>
-Analyze the sentiment of replies using the BERTweet model, which would be more appropriate for this project since it was trained on a corpus of Tweets: https://github.com/VinAIResearch/BERTweet
