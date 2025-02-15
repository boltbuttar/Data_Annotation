# **📄 Automated Research Paper Annotation – NeurIPS Paper Categorization**  

🚀 **Welcome to the Automated Research Paper Annotation Project!**  
This script processes **NeurIPS research papers (PDFs)**, extracts **titles & abstracts**, and classifies them into **five AI-related categories**. It’s designed to automate research paper analysis and help organize scientific documents efficiently.  

---

## **📌 How It Works (Step-by-Step Guide)**  

### **1️⃣ Setup the Environment**  
Before running the script, you need to install the required dependencies.  

### **2️⃣ Install Required Libraries**  
Run the following command to install the required libraries:  
```bash
pip install pandas pymupdf
```
- `pandas` → For handling structured data (CSV files).  
- `pymupdf` (also known as `fitz`) → For **extracting text from PDFs**.  

---

### **3️⃣ Organize Your Files**  
1. **Place your NeurIPS research papers (PDFs) in the folder:**  
   📂 `D:\NeurIPS_Papers`  
2. **Set the output directory where the results will be saved:**  
   📂 `C:\Users\asgha\Desktop\Asssignment02`  

---

### **4️⃣ Run the Script**  
Once everything is set up, **run the script**:  
```bash
python annotation_script.py
```
This will:
- **Scan the folder `D:\NeurIPS_Papers`** for all PDFs.  
- **Extract the title & abstract** from the first page of each PDF.  
- **Classify each paper** into one of the five AI categories.  
- **Save the results** in `C:\Users\asgha\Desktop\Asssignment02\annotated_papers.csv`.  

---

## **📂 Output File: `annotated_papers.csv`**  
| **Title**                           | **Abstract**                               | **Category**               |
|-------------------------------------|-------------------------------------------|----------------------------|
| Deep Learning in AI                | CNNs are used for various AI tasks.       | Deep Learning              |
| Object Detection Methods           | A new approach to image segmentation.     | Computer Vision            |
| Policy Gradient for RL             | Reinforcement learning with policies.     | Reinforcement Learning     |

---

## **📚 Categories Used in This Project**  
| **Category**                     | **Keywords Used for Classification** |
|----------------------------------|-------------------------------------|
| 🧠 **Deep Learning**              | neural network, CNN, RNN, transformer, self-supervised learning, representation learning, GNN |
| 👀 **Computer Vision**            | image processing, object detection, segmentation, vision, scene understanding, convolutional neural networks |
| 🎮 **Reinforcement Learning**      | reinforcement learning, Q-learning, policy gradient, Markov decision process, agent, reward function, actor-critic |
| 🗣 **Natural Language Processing** | language model, NLP, BERT, text generation, transformer, word embeddings, machine translation, semantic analysis |
| 📊 **Optimization**               | gradient descent, convex optimization, loss function, optimizer, backpropagation, stochastic gradient descent, Lagrangian |

---

## **⚠️ Challenges You May Face & How to Solve Them**
### **1️⃣ PDF Text Extraction Issues**  
- Some research papers **may not have selectable text** (e.g., scanned PDFs).  
✅ **Solution:** Use **OCR (Optical Character Recognition)** tools like `Tesseract-OCR` to extract text from images.  

### **2️⃣ Misclassification of Papers**  
- Some research papers might **not be classified correctly** due to missing keywords.  
✅ **Solution:** **Expand the keyword list** in the script based on **real-world paper topics**.  

### **3️⃣ Large Dataset Processing Speed**  
- If you process **hundreds of PDFs**, it may take time.  
✅ **Solution:** Use **multithreading** (e.g., `ThreadPoolExecutor`) to process multiple PDFs simultaneously.  

### **4️⃣ CSV Encoding Issues**  
- Some characters (like **special symbols in paper titles**) may cause encoding problems.  
✅ **Solution:** Save CSV files using **UTF-8 encoding** (`encoding="utf-8"`).  

---

## **🎯 Next Steps**
✅ **Run the script** and check the `annotated_papers.csv`.  
✅ **Upload the code to GitHub** for documentation.  
✅ **Write a blog on Medium** to explain your experience.  
✅ **Share your work on LinkedIn** with your insights!  

---

## **👨‍💻 Contributing**
If you have improvements for classification logic or new category suggestions, feel free to submit a **pull request**! 🚀  

---

## **📩 Contact & Support**
If you have any issues or need help, feel free to open an **issue** on GitHub or reach out. 🚀  

---

### **🎉 Happy Research Paper Classification!**  
Let me know if you need any modifications. 🚀
