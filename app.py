# LIBRARY IMPORTS
import streamlit as st
import pandas as pd
import sys
from streamlit import cli as stcli
import plotly.express as px


# GLOBAL VARIABLES
# Create variable for Tweet being analyzed in this app
tweet_url = 'https://twitter.com/Meta/status/1453795115701440524'


# FUNCTIONS
def data_import():
    """
    Imports data from "df_redacted.csv" as a dataframe.
    """
    df_redacted = pd.read_csv('df_redacted.csv')
    return df_redacted


def data_manipulation(df_redacted):
    """
    Manipulates the data imported from the CSV file to prepare for bar chart.
    """

    # Create new dataframe, reset the index, and rename columns
    sentiment_counts = pd.DataFrame(df_redacted['sentiment_score'].value_counts(dropna=False))
    sentiment_counts = sentiment_counts.reset_index()
    sentiment_counts.columns = ['Sentiment', 'Count']

    # Find sentiment category with the highest count
    sentiment = sentiment_counts.loc[sentiment_counts['Count'].idxmax(), 'Sentiment']

    return sentiment_counts, sentiment


def display_header(sentiment):
    """
    Displays the header section of the app.
    """
    st.header('This app runs a sentiment analysis of the replies to a Facebook Tweet '
              'announcing their rebranding to Meta.')
    st.header('RESULT: {}'.format(sentiment))


def display_chart(sentiment_counts):
    """
    Displays the chosen chart for the data.
    """
    # Display count for each sentiment category
    fig = px.bar(sentiment_counts,
                 x='Sentiment',
                 y='Count',
                 title='Tweet Replies Count by Sentiment Category')
    fig.update_layout(title_x=0.5)
    st.plotly_chart(fig, use_container_width=True)


def display_footer(tweet_url, sentiment):
    """
    Displays the footer section of the app.
    """
    st.markdown('**Objective:** Understand public sentiment of a Tweet by analyzing the sentiment of each reply.')
    st.markdown('**Analysis:** This app runs sentiment analysis on 10,948 replies to a Facebook Tweet announcing '
                'their rebranding to Meta on 10/28/2021. Link to Tweet: {}'.format(tweet_url))
    st.markdown('**Results:** Most frequent sentiment category for the replies to this Tweet: **{}**'.format(sentiment))
    st.markdown('**Notes:** ')
    st.markdown('- The VADER model was used to analyze the sentiment of each reply: '
                'https://github.com/cjhutto/vaderSentiment')
    st.markdown('- Due to Twitter developer policies, I am not able to share the data set of downloaded Tweet replies '
                'so my DATA EXTRACTION and DATA CLEANSING steps are not shown at this time but will be added soon!')
    st.markdown('**Plans for Version 2.0:**')
    st.markdown('- Formulate method for cleaning Tweet replies, such as removing those that are from bots or are spam.')
    st.markdown('- Analyze the sentiment of replies using the BERTweet model, which would be more appropriate for this '
                'project since it was trained on a corpus of Tweets: https://github.com/VinAIResearch/BERTweet')


def main():
    """
    Main function for the app which calls all other functions to display the app.
    """
    # DATA IMPORT
    df_redacted = data_import()

    # DATA MANIPULATION
    sentiment_counts, sentiment = data_manipulation(df_redacted)

    # DISPLAY DATA
    display_header(sentiment)
    display_chart(sentiment_counts)
    display_footer(tweet_url, sentiment)


if __name__ == '__main__':
    if st._is_running_with_streamlit:
        main()
    else:
        sys.argv = ['streamlit', 'run', sys.argv[0]]
        sys.exit(stcli.main())
