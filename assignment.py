import os
import fitz  
import pandas as pd


CATEGORIES = {
    "Deep Learning": [
        "neural network", "deep learning", "CNN", "RNN", "transformer", 
        "self-supervised learning", "representation learning", "GNN"
    ],
    "Computer Vision": [
        "image processing", "object detection", "segmentation", "vision",
        "scene understanding", "convolutional neural networks"
    ],
    "Reinforcement Learning": [
        "reinforcement learning", "Q-learning", "policy gradient", "Markov decision process",
        "agent", "reward function", "actor-critic"
    ],
    "Natural Language Processing": [
        "language model", "NLP", "BERT", "text generation", "transformer",
        "word embeddings", "machine translation", "semantic analysis"
    ],
    "Optimization": [
        "gradient descent", "convex optimization", "loss function", "optimizer",
        "backpropagation", "stochastic gradient descent", "Lagrangian"
    ]
}


PDF_DIR = r"D:\NeurIPS_Papers"


OUTPUT_DIR = r"C:\Users\asgha\Desktop\Asssignment02"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "annotated_papers.csv")

def extract_text_from_pdf(pdf_path):
    """Extracts the title and abstract from the first page of a PDF."""
    try:
        doc = fitz.open(pdf_path)
        text = doc[0].get_text("text")  
        lines = text.split("\n")
        
        title = lines[0] if lines else "Unknown Title"
        abstract = " ".join(lines[1:5]) if len(lines) > 1 else "No Abstract Found"
        return title.strip(), abstract.strip()
    except Exception as e:
        print(f"Error processing {pdf_path}: {e}")
        return None, None  

def classify_paper(title, abstract):
    """Classifies a research paper based on keywords in title and abstract."""
    text = f"{title} {abstract}".lower()
    for category, keywords in CATEGORIES.items():
        if any(keyword in text for keyword in keywords):
            return category
    return None  

def process_pdfs():
    """Reads all PDFs in the folder, extracts content, classifies, and saves results."""
    papers = []

   
    for file_name in os.listdir(PDF_DIR):
        if file_name.endswith(".pdf"):
            pdf_path = os.path.join(PDF_DIR, file_name)
            print(f"Processing: {file_name}")
            
            title, abstract = extract_text_from_pdf(pdf_path)
            if title and abstract:
                category = classify_paper(title, abstract)
                if category:  
                    papers.append({"title": title, "abstract": abstract, "category": category})

 
    df = pd.DataFrame(papers)
    df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8")
    
    print(f"\n Annotated papers saved to: {OUTPUT_FILE}")

if __name__ == "__main__":
    process_pdfs()
