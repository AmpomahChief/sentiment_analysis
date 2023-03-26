# NATURAL LANGUAGE PROCESSING (NLP) — SENTIMENT ANALYSIS

## INTRODUCTION ON NLP.

Natural language processing (NLP) is a branch of artificial intelligence concerned with giving computers the ability to understand text and spoken words in much the same way human beings can.

NLP combines computational linguistics — rule-based modeling of human language — with statistical, machine learning, and deep learning models. Together, these technologies enable computers to process human language in the form of text or voice data and to ‘understand’ its full meaning, complete with the speaker or writer’s intent and sentiment.

NLP drives computer programs that translate text from one language to another, respond to spoken commands, and summarize large volumes of text rapidly — even in real time. There’s a good chance you’ve interacted with NLP in the form of voice-operated GPS systems, digital assistants, speech-to-text dictation software, customer service chatbots, and other consumer conveniences. But NLP also plays a growing role in enterprise solutions that help streamline business operations, increase employee productivity, and simplify mission-critical business processes.

## PROJECT OVERVIEW.

Before we talk about the project and what it is about, let’s take some time to have a look at what sentiment analysis entails.

Sentiment analysis (or opinion mining) is a natural language processing (NLP) technique used to determine whether data is positive, negative or neutral. Sentiment analysis is often performed on textual data to help businesses monitor brand and product sentiment in customer feedback, and understand customer needs.

Sentiment analysis is the process of detecting positive or negative sentiment in text. It’s often used by businesses to detect sentiment in social data, gauge brand reputation, and understand customers.

This a sentiment analysis project to monitor public sentiment towards COVID-19 vaccinations now and especially in the future when COVID-19 vaccines are offered to the public. The anti-vaccination sentiment could pose a serious threat to the global efforts to get COVID-19 under control in the long term.

The objective of this challenge is to develop a machine learning model to assess if a Twitter post related to vaccinations is positive, neutral, or negative. This solution could help governments and other public health actors monitor public sentiment towards COVID-19 vaccinations and help improve public health policy, vaccine communication strategies, and vaccination programs across the world.

The data set for this project comes from tweets collected and classified through Crowdbreaks.org [Muller, Martin M., and Marcel Salathe. “Crowdbreaks: Tracking Health Trends Using Public Social Media Data and Crowdsourcing.” Frontiers in public health 7 (2019).]. Tweets have been classified as pro-vaccine (1), neutral (0) or anti-vaccine (-1). The tweets have had usernames and web addresses removed.

The objective of this challenge is to develop a machine learning model to assess if a twitter post that is related to vaccinations is positive, neutral, or negative.

Variable definition:

tweet_id: Unique identifier of the tweet

safe_tweet: Text contained in the tweet. Some sensitive information has been removed like usernames and urls

label: Sentiment of the tweet (-1 for negative, 0 for neutral, 1 for positive)

agreement: The tweets were labeled by three people. Agreement indicates the percentage of the three reviewers that agreed on the given label. You may use this column in your training, but agreement data will not be shared for the test set.

# DATA PROCESSING

## EXPLORATORY DATA ANLYSIS

After the data is loaded, it is checked for any inconsistences. With this data set a few null values were found (3) and removed from the data. Since the null values were too small it is okay to remove them completely.

## SPLITTING THE DATA SET

Before the model can be trained, the train data set must be split into train and evaluation (eval) parts. The ratio for splitting the data set is a random process and the train split must contain most of the data set. Here the split was done in the proportion of train split (80%) and eval split (20%).

## TOKENIZING

Tokenization is breaking the raw text into small chunks. Tokenization breaks the raw text into words, sentences called tokens. These tokens help in understanding the context or developing the model for the NLP. The tokenization helps in interpreting the meaning of the text by analyzing the sequence of the words.

Natural language processing is one of the fields in programming where the natural language is processed by the software.

Now that have an idea of what tokenizing is, we must perform the process on our data set to help the model understand the tweets. Tokenizing is done on the ‘safe text’ column of the data set. To perform the tokenizing, you would have to import the tokenizing library from transformers. These are libraries provided by hugging. E.g (from transformers import AutoTokenizer)

## MODEL TRAINING

In NLP pretrained models from huggingface is used for the training. Some of the pretrained models include, cardiffnlp/twitter-reberta-base-sentiment, finiteatomato/bertweet-base-sentiment-analysis, bert-base-cased, etc. There are thousands more models which can found on huggingface platform.

For this project two models were trained, the pretrained models used were bert-base-cased and cardiffnlp/twitter-reberta-base-sentiment for 3 epoch and 15 epoch respectively. An epoch is when all the training data is used at once and is defined as the total number of iterations of all the training data in one cycle for training the machine learning model. Another way to define an epoch is the number of passes a training dataset takes around an algorithm.
