import gradio as gr
# Creating a gradio app using the inferene API
App = gr.Interface.load("huggingface/AmpomahChief/sentiment_analysis_on_covid_tweets",
  title="COVID 19 tweets sentiment analysis", description ="This is a sentiment analysis on COVID 19 tweets using pretrained model on hugging face",
 allow_flagging=False, examples=[["Input your text here"]]
)

App.launch()