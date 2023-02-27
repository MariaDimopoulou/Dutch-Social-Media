
# coding: utf-8

# In[1]:


import json
import pandas as pd

data_list = [] #I am creating an empty list to store the data from the json files.

for filename in [r'C:\Users\dimop\Desktop\Dutch Social Media\archive (2)\dutch_tweets_chunk0.json',
                 r'C:\Users\dimop\Desktop\Dutch Social Media\archive (2)\dutch_tweets_chunk1.json',
                 r'C:\Users\dimop\Desktop\Dutch Social Media\archive (2)\dutch_tweets_chunk2.json',
                 r'C:\Users\dimop\Desktop\Dutch Social Media\archive (2)\dutch_tweets_chunk3.json',
                 r'C:\Users\dimop\Desktop\Dutch Social Media\archive (2)\dutch_tweets_chunk4.json',
                 r'C:\Users\dimop\Desktop\Dutch Social Media\archive (2)\dutch_tweets_chunk5.json',
                 r'C:\Users\dimop\Desktop\Dutch Social Media\archive (2)\dutch_tweets_chunk6.json',
                 r'C:\Users\dimop\Desktop\Dutch Social Media\archive (2)\dutch_tweets_chunk7.json',
                 r'C:\Users\dimop\Desktop\Dutch Social Media\archive (2)\dutch_tweets_chunk8.json',
                 r'C:\Users\dimop\Desktop\Dutch Social Media\archive (2)\dutch_tweets_chunk9.json']:
    with open(filename) as f:
        data = json.load(f)
        data_list.extend(data)

data = pd.DataFrame(data_list) #Creating a data frame to store all the data
print(data.head()) 
print(data.shape)   


# In[72]:


import matplotlib.pyplot as plt
missing_values = data.isnull().sum() #I am finding the missing values from my dataframe.
missing_percent = (missing_values / len(data)) * 100 #Counting the missing values and turning them in percentages.
missing_df = pd.DataFrame({'column_name': missing_values.index, 'missing_percent': missing_percent.values}) #I am making a dataframe of the missing values according to the description.
print(missing_df)
plt.bar(missing_df['column_name'], missing_df['missing_percent'], color='maroon', width=0.9)
plt.xticks(rotation=90)
plt.xlabel('Information')
plt.ylabel('Percentage of Missing Values')
plt.title('Percentage of Missing Values by Information')
plt.show()


# **Explanation:** According to the bar graph, the most common missing values from our data are HISCO codes(~74% of the values are missing) and the specific location of the person that makes the tweet(~50% of the values that are related to point, latitude and longtitude are missing). 

# In[64]:


influencers=data['screen_name'].value_counts().head(10) #I am counting the names that appear most in the data set of the tweets.
print(influencers)
influencers.plot(kind='pie',autopct='%1.1f%%',startangle=90,colors = ['#F4A460', '#8B4513', '#D2B48C', '#DEB887', '#B8860B', '#CD853F', '#A0522D', '#8B0000', '#800000', '#BC8F8F'],ylabel='')
top_influencers = influencers.index.tolist()


# **Explanation:** We can see the top 10 people who tweeted the most in the period of time where we have our data. These are the most active people on Twitter in this particular period and region. s_akrati has created the most tweets ~20% of the tweets among these top-10 were theirs. 

# In[80]:


influencer_region = data_unique.loc[data_unique['screen_name'].isin(top_influencers), 'province'].value_counts()
influencer_region.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['#DEB887', '#B8860B', '#CD853F', '#A0522D', '#8B0000', '#800000', '#BC8F8F'], ylabel='')


# **Explanation:** It seems that between the top 10 influencers the 40% of them lives in Noord-Holland area and the least of them (around 10%) in the Zuid-Holland. However, there is a big percentage of people who do not show the area they live(30%). 

# In[5]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

mean_sentiment_by_date = data.groupby('weekofyear')['sentiment_pattern'].mean()
mean_sentiment_by_date.plot(figsize=(10, 6),color='#F4A460')
plt.xlabel('Date')
plt.ylabel('Mean Sentiment Score')
plt.title('Sentiment Score Over Time')
plt.show()



# **Explanation:** This is a linegraph of the sentiment score over time in the region that we are studying. around 5th and 7th week there was a huge drop while around the 15th week there was an increase which means that the sentiment was very positive at this period of time. There was another drop around 28 and 30th week which indicates that the sentiment was mostly negative on the tweets at this period of time. 
# 

# In[11]:


get_ipython().system('pip install wordcloud')


# In[27]:


import re
from wordcloud import WordCloud, STOPWORDS

text = data['text_translation'].str.cat(sep=' ') #We are choosing the column with the translated tweets.

text = text.lower()  # I am converting to lowercase
text = re.sub(r'http\S+', '', text)  # I am removing URLs
text = re.sub(r'@\S+', '', text)  #I am removing mentions
text = re.sub(r'[^\w\s]', '', text)  # I am removing punctuation
text = re.sub(r'\d+', '', text)  #I am removing numbers

wordcloud = WordCloud(width=100, height=100, background_color='white', stopwords=STOPWORDS).generate(text) #Creating the word cloud.

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()


# **Explanation:** Here we have created a word cloud which presents the most commonly used words in the tweets of the people in our data. We can see that the words that are used the most are words related to the pandemic and Covid-19.  

# In[82]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

mean_sentiment_by_day = data.groupby('weekday')['sentiment_pattern'].mean()
mean_sentiment_by_day.plot(figsize=(10, 6),color='#B8860B')
plt.xlabel('Day')
plt.ylabel('Mean Sentiment Score')
plt.title('Sentiment Score Over Days')
plt.show()


# **Explanation:** In the line graph above, we can see the sentiment score according to the week days. We are not sure the the day 0 is Monday. So, we can see that the highest sentiment score, meaning the day that has the most positive posts is the day 2 and the least postive posts are on the 5th day.

# In[100]:


top_tweets = data.loc[data['screen_name'].isin(top_influencers)]
tweets_by_day = top_tweets.groupby(['weekday', 'screen_name'])['text_translation'].count()

tweets_by_day = tweets_by_day.unstack()

tweets_by_day.plot(kind='bar', stacked=True, figsize=(10,6),color=['sienna','chocolate','navajowhite', 'olive', '#CD853F', '#A0522D','slategrey', '#8B0000', 'tan', '#BC8F8F'])
plt.xlabel('Day of the Week')
plt.ylabel('Number of Posts')
plt.title('Number of Posts by Top Influencers')
plt.show()


# **Explanation:** Here we have a stacked bar showing how many tweets per day do the top 10 post. We can see that this top 10 has a pretty steady rhythm of posting each day. Most of them post every day with the 6th day of the week being the one with the least number of posts in total for all the influencers.
