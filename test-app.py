import streamlit as st
import torch as nn
import requests
from transformers import pipeline

############ 1. PAGE LAYOUT, TITLE
st.set_page_config(
    layout="centered", page_title='Simple Sentiment Analysis App Using\n\
        Hugging Face Model Library', page_icon="(y)"
)

c1,c2,c3 = st.columns([1,3,1])

with c1:
    st.write("")
with c2:
    st.image("images/emotions.png")
with c3:
    st.write("")

# prepare a list of top sentiment analysis models including default
models = ["distilbert-base-uncased-finetuned-sst-2-english",#default
          "bhadresh-savani/distilbert-base-uncased-emotion",#emotions
          "ProsusAI/finbert",#finance
          "finiteautomata/bertweet-base-sentiment-analysis",#tweets
          "cardiffnlp/twitter-roberta-base-sentiment"#tweet2
]
model_pointers = ["default: distilbert-base-uncased-finetuned-sst-2-english",
                  "emotion: bhadresh-savani/distilbert-base-uncased-emotion",
                  "finance: ProsusAI/finbert",
                  "tweets: finiteautomata/bertweet-base-sentiment-analysis",
                  "tweets2: cardiffnlp/twitter-roberta-base-sentiment"
]

#Prompt User for input text for sentiment analysis, keep input and model selection in form to delay page refresh
with st.form(key="init_form"):
    input_text = st.text_area("Input a sentence on which to perform sentiment\
                           analysis", value="I love Streamlit and I love Data Science!")
    choice = st.selectbox("Choose Model", model_pointers)

    # The index of choice in model_pointers will access the models list
    # and select the Hugging Face model path at index.  
    user_picked_model = models[model_pointers.index(choice)]
    with st.spinner("Downloading Model"):
        sentiment_pipeline = pipeline(model=user_picked_model)

    analyze = st.form_submit_button("Analyze")

if analyze:
    with st.spinner("Analyzing..."):
        sentiment_pipeline = pipeline(model=user_picked_model)
        sentiment_results=sentiment_pipeline(input_text)
        st.write(f"Sentiment: {sentiment_results[0]['label']}")
        st.write(f"Score: {sentiment_results[0]['score']}")
else:
    st.write("no input detected")

