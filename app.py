import gradio as gr
from transformers import pipeline

model= pipeline("summarization")

def predict(promt):
    summary=model(prompt)[0]["summary_text"]
    return summary
with gr.Blocks() as demo:
    textbox=gr.TextBox(placeholder="enter text to summarize",lines=4)
    gr.Interface(fn=predict,inputs=textbox,outputs="text")
demo.launch()