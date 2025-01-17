import os
from transformers import pipeline
import gradio as gr

# Load the summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_long_text(text, max_length=130, min_length=30):
    # Input validation
    if not text.strip():
        return "Error: Input text cannot be empty."

    # Token limit for BART model
    token_limit = 1024
    if len(text.split()) > token_limit:
        # Chunking the text if it exceeds the token limit
        chunks = []
        words = text.split()
        for i in range(0, len(words), token_limit):
            chunks.append(' '.join(words[i:i + token_limit]))
        
        # Summarize each chunk and combine results
        summaries = []
        for chunk in chunks:
            try:
                summary = summarizer(chunk, max_length=max_length, min_length=min_length)
                summaries.append(summary[0]['summary_text'])
            except Exception as e:
                return f"Error during summarization: {str(e)}"
        
        return " ".join(summaries)

    try:
        # Generate summary for the provided text
        summary = summarizer(text, max_length=max_length, min_length=min_length)
        return summary[0]['summary_text']
    except Exception as e:
        return f"Error during summarization: {str(e)}"

def summarization_gradio_interface():
    interface = gr.Interface(
        fn=summarize_long_text,
        inputs=[
            gr.Textbox(label="Input Text", placeholder="Enter Text...", lines=10),
            gr.Slider(label="Max Summary Length", minimum=100, maximum=500, value=130),
            gr.Slider(label="Min Summary Length", minimum=100, maximum=300, value=30)
        ],
        outputs="text",
        title="Text Summarizer",
        description="Summarize text effectively using Hugging Face Transformers",
        live=True,
        theme="default"
    )
    interface.launch(share=True)

if __name__ == "__main__":
    summarization_gradio_interface()
