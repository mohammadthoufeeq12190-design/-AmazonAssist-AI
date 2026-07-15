# 🛒 AmazonAssist AI

> **An Intelligent AI-Powered E-Commerce Customer Support Assistant built using Google Gemini AI, LangChain, FAISS Vector Database, and Streamlit.**

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![Google Gemini](https://img.shields.io/badge/Google-Gemini-blue?logo=google)
![LangChain](https://img.shields.io/badge/LangChain-Framework-green)
![FAISS](https://img.shields.io/badge/FAISS-Vector%20Database-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

# 📌 Project Overview

**AmazonAssist AI** is an intelligent e-commerce customer support chatbot designed to provide a smart, conversational shopping experience. It leverages **Google Gemini AI**, **LangChain**, and **FAISS Vector Database** to answer customer queries, recommend products, track orders, provide coupon information, and retrieve answers from support documents using **Retrieval-Augmented Generation (RAG).**

The chatbot combines conversational AI with vector search to deliver accurate, context-aware, and natural responses, making it an ideal AI assistant for modern e-commerce platforms.

---

# 🚀 Features

- 🤖 AI-powered conversational chatbot
- 🛍️ Intelligent product recommendation system
- 💰 Budget-based product recommendations
- 📦 Real-time order tracking
- 🎟️ Coupon & discount recommendation engine
- 📚 Retrieval-Augmented Generation (RAG)
- 🔍 FAISS Vector Database for semantic search
- 🧠 Conversational memory
- 💬 Session-based chat history
- ⚡ Google Gemini AI response generation
- 🖥️ Interactive Streamlit web interface

---

# 🏗️ System Architecture

<p align="center">
  <img src="assets/architecture%20(5).png" width="100%" alt="AmazonAssist AI Architecture">
</p>

---

# 🛠️ Technology Stack

| Category | Technologies |
|-----------|-------------|
| **Frontend** | Streamlit |
| **Backend** | Python |
| **AI Model** | Google Gemini AI |
| **Framework** | LangChain |
| **Vector Database** | FAISS |
| **Data Processing** | Pandas |
| **Datasets** | CSV Files |
| **Embedding Storage** | FAISS Vector Store |

---

# 📂 Project Structure

```text
AmazonAssist-AI/
│
├── app.py
├── chatbot.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   ├── products.csv
│   ├── orders.csv
│   ├── coupons.csv
│   ├── faq.txt
│   └── policies.txt
│
├── modules/
│   ├── recommendation.py
│   ├── retrieval.py
│   ├── order_tracking.py
│   ├── returns.py
│   └── coupons.py
│
├── embeddings/
│
├── vector_db/
│
└── assets/
    ├── architecture (5).png
    └── demo.png
```

---

# ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/AmazonAssist-AI.git
```

### Navigate to the Project

```bash
cd AmazonAssist-AI
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create Environment Variables

Create a `.env` file.

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

### Run the Application

```bash
streamlit run app.py
```

---

# ⚙️ How It Works

```text
User Query
      │
      ▼
Intent Detection
      │
      ▼
Decision Layer
      │
      ├── Product Recommendation
      ├── Order Tracking
      ├── Coupon Engine
      └── RAG Retrieval
      │
      ▼
Google Gemini AI
      │
      ▼
AI Response Generation
      │
      ▼
Streamlit User Interface
```

---

# 📊 Datasets

### 🛍️ products.csv

Contains product information including:

- Product Name
- Brand
- Category
- Price
- Rating
- Stock Availability

---

### 📦 orders.csv

Contains order information including:

- Order ID
- Customer Name
- Product Name
- Order Status
- Payment Method

---

### 🎟️ coupons.csv

Contains promotional coupon details including:

- Coupon Code
- Discount Percentage
- Minimum Order Amount

---

### 📚 FAQ Documents

Used for **Retrieval-Augmented Generation (RAG)** to answer customer support questions such as:

- Refund Policy
- Shipping Information
- Return Policy
- Customer Support
- Frequently Asked Questions

---

# 💬 Sample Queries

```text
Recommend a laptop

Recommend products under ₹10,000

Track ORD003

Show available coupons

What is the refund policy?

Any offers available?

Recommend a gaming mouse

What is its price?
```

---

# 🎯 Key Achievements

- Built an AI-powered e-commerce support assistant
- Implemented Retrieval-Augmented Generation (RAG)
- Integrated Google Gemini AI
- Developed a product recommendation engine
- Built an order tracking module
- Added conversational memory
- Implemented semantic search using FAISS
- Designed an interactive Streamlit interface

---

# 💡 AI Concepts Demonstrated

- Retrieval-Augmented Generation (RAG)
- Large Language Models (LLMs)
- Vector Databases
- Semantic Search
- Prompt Engineering
- Conversational AI
- Recommendation Systems
- Context-Aware Responses

---

# 📸 Demo

<p align="center">
  <img src="assets/demo.png" width="100%" alt="AmazonAssist AI Demo">
</p>

---

# 🚀 Future Improvements

- MySQL Database Integration
- User Authentication
- Voice-Based Chatbot
- Multi-Language Support
- Advanced Recommendation Engine
- Docker Deployment
- Cloud Deployment
- Admin Dashboard
- Analytics & Monitoring

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository.

2. Create a feature branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Added new feature"
```

4. Push to GitHub.

```bash
git push origin feature-name
```

5. Open a Pull Request.

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

**Syed Thoufeeq**

AI Engineer | Machine Learning | Deep Learning | Generative AI

---

## ⭐ If you found this project helpful, consider giving it a Star on GitHub!
