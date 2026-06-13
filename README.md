# AmazonAssist AI

## Overview

AmazonAssist AI is an intelligent e-commerce customer support chatbot built using Python, Streamlit, FAISS Vector Database, LangChain, and Google Gemini AI.

The chatbot helps customers with product recommendations, order tracking, refund-related queries, coupons, and general support questions through a conversational interface.

---

## Features

### Product Recommendation System

* Recommends products from the product database.
* Supports budget-based recommendations.
* Displays product name, brand, price, and rating.

### Order Tracking System

* Tracks orders using Order IDs.
* Shows order status and payment details.

### Coupon & Discount Engine

* Displays available discount coupons.
* Shows minimum order requirements.

### RAG-Based Question Answering

* Retrieves information from FAQs and support documents.
* Uses FAISS Vector Search for relevant context retrieval.

### Gemini AI Integration

* Generates natural and professional responses.
* Improves customer support experience.

### Conversational Memory

* Remembers previously recommended products.
* Supports follow-up questions.

### Chat History

* Stores conversation history within the current session.

---

## Technologies Used

### Frontend

* Streamlit

### Backend

* Python

### AI & Machine Learning

* Google Gemini API
* LangChain
* FAISS Vector Database
* Embeddings

### Data Processing

* Pandas
* CSV Files

---

## Project Architecture

User Query

↓

Intent Router

↓

Decision Layer

* Product Recommendation Engine
* Order Tracking System
* Coupon Engine
* RAG Retrieval System

↓

Gemini AI Response Generation

↓

Streamlit User Interface

---

## Datasets

### products.csv

Contains:

* Product Name
* Brand
* Category
* Price
* Rating
* Stock

### orders.csv

Contains:

* Order ID
* Customer Name
* Product Name
* Order Status
* Payment Method

### coupons.csv

Contains:

* Coupon Code
* Discount Percentage
* Minimum Order Amount

### FAQ Documents

Used for Retrieval-Augmented Generation (RAG).

---

## Sample Queries

* Recommend a laptop
* Recommend products under ₹10,000
* Track ORD003
* What is the refund policy?
* Any offers available?
* What is its price?

---

## Key Achievements

* Built a complete AI-powered customer support assistant.
* Implemented Retrieval-Augmented Generation (RAG).
* Integrated Google Gemini AI.
* Created a product recommendation engine.
* Developed an order tracking system.
* Added conversational memory.
* Built an interactive Streamlit web application.

---

## Future Improvements

* MySQL Database Integration
* User Authentication
* Voice-Based Chatbot
* Multi-Language Support
* Advanced Recommendation Engine
* Cloud Deployment

---

## Conclusion

AmazonAssist AI demonstrates the practical application of Generative AI, RAG, Vector Databases, and Conversational AI in an e-commerce environment. The project showcases skills in AI Engineering, Machine Learning, Data Processing, Prompt Engineering, and Full-Stack AI Development.
