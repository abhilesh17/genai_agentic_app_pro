
from transformers import pipeline

class SummarizerTool:
    def __init__(self):
        self.summarizer = pipeline("summarization")

    def summarize(self, text):
        summary = self.summarizer(text, max_length=100, min_length=30, do_sample=False)
        return summary[0]['summary_text']
