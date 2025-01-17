# Text Summarizer with Hugging Face Transformers and Gradio
This project provides a powerful, user-friendly tool for summarizing lengthy texts using the state-of-the-art facebook/bart-large-cnn model from Hugging Face Transformers. It features an intuitive web interface built with Gradio, enabling users to create concise, meaningful summaries with just a few clicks.

# 🔑 Key Features
1. State-of-the-Art Summarization: Utilizes the pre-trained BART model, known for its superior performance in abstractive summarization tasks.
2. Efficient Processing of Long Texts: Automatically splits long inputs into manageable chunks (up to 1024 tokens) to adhere to the model's token limit and merges the results into a cohesive summary.
3. Customizable Output: Users can set their preferred maximum and minimum lengths for the summary, allowing flexibility in how concise or detailed the output is.
4. Interactive Web Interface: A clean, easy-to-use Gradio-based interface, enabling users to interact with the summarization tool directly in their web browsers.
5. Error Handling: Provides clear error messages for invalid or empty inputs, ensuring a smooth user experience.

# 🚀 Live Demo
https://huggingface.co/spaces/Tishika/Text-Summarization-App

# 📚 How It Works
1. Input Text: The user inputs text into the provided textbox.
2. Preprocessing: If the text exceeds the model's token limit (1024 tokens), it is split into smaller chunks while maintaining coherence.
3. Summarization: Each chunk is passed to the BART model for summarization.
4. Postprocessing: The summarized chunks are combined to produce the final summary.
5. Custom Settings: Users can adjust sliders for the maximum and minimum summary lengths to tailor the output to their needs.

# 🖼️ Application Interface
1. Input Textbox: Paste or type the text you want to summarize.
2. Max Summary Length Slider: Set the maximum number of words for the summary.
3. Min Summary Length Slider: Set the minimum number of words for the summary.
4. Output: View the generated summary in the output text box.

# 🧠 Model Details
1. Model Used: facebook/bart-large-cnn
2. Task: Abstractive text summarization.
3. Token Limit: 1024 tokens per input.

# ⚡Advanced Functionality
1. Chunking Mechanism: Handles long text inputs by splitting them into smaller chunks, ensuring the token limit is respected without losing coherence.
2. Error Handling: Provides detailed feedback for invalid inputs, ensuring a smooth user experience.
