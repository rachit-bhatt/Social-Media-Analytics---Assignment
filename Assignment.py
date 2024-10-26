# Data Operation.
import pandas as pd

# Visualization.
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Deployment.
import streamlit as st

# Cache Cleaning.
import os

#region Pre-Requisites

width = 2560
height = 1600
figure_size = (25.6, 16)
df = pd.read_csv('Dataset/news.csv')

#endregion

#region Article Mapping

# Create a word-to-article mapping for visualization.
word_article_map = dict()

for idx, row in df.iterrows():

    for word in row.title.split():

        if word in word_article_map:
            word_article_map[word].append(f'{ row.title } - { row.author }')
        else:
            word_article_map[word] = [f'{ row.title } - { row.author }']

#endregion

# Display the App Title.
st.title('Yahoo Finance News Topic Explorer')

# Generate a word cloud from the cleaned titles.
all_text = ' '.join(df['title'].tolist())
wordcloud = WordCloud(width = width, height = height, background_color = 'white').generate(all_text)

plt.figure(figsize = figure_size)

plt.imshow(wordcloud, interpolation = 'bilinear')

plt.axis('off')
plt.savefig('wordcloud.png') # Saving image to load it on the deployed platform.

st.image('wordcloud.png')

st.header('Click on a word to see related articles')

# Create a dropdown or clickable word list.
selected_word = st.selectbox('Select a Word:', list(word_article_map.keys()))

# Display the related articles for the selected word.
if selected_word:
    st.write(f'Articles related to the word `{ selected_word }`:')

    for article in word_article_map[selected_word]:
        st.write(f'- { article }')

# Cleaning Cached Image.
os.remove('wordcloud.png')