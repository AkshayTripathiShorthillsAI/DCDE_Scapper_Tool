import torch
from transformers import AutoTokenizer, AutoModel

def create_embeddings(text, tokenizer, model):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state[:, 0, :].numpy().squeeze()

def recursive_text_splitter(text, max_chunk_size=2000, overlap=200):
    chunks = []
    def split(text, start, end):
        if end - start <= max_chunk_size:
            chunks.append(text[start:end])
            return
        mid = (start + end) // 2
        if mid > start + max_chunk_size:
            mid = start + max_chunk_size
        split(text, start, mid + overlap)
        split(text, mid, end)
    split(text, 0, len(text))
    return chunks
