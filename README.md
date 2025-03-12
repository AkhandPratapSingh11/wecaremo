# EmoCare - AI-Powered Conversational Wellness Assistant

## 📌 Project Overview
EmoCare is an AI-driven conversational wellness assistant designed to provide **emotional support and personalized wellness suggestions**. It leverages **Natural Language Processing (NLP)** and **Generative AI** to understand human emotions, enabling meaningful and supportive conversations. The model is built using **Groq's AI API** for intelligent responses.

## 🌟 Features
- **Conversational AI Chatbot**: Understands emotions and provides empathetic responses.
- **Sentiment Analysis**: Analyzes user messages to detect emotions.
- **Wellness Recommendations**: Suggests relaxation techniques, mental health tips, and activities based on sentiment analysis.
- **Memory Retention**: Stores past conversations for context-aware interactions.
- **Streamlit-Based UI**: Simple and interactive frontend for seamless user experience.

## 🚀 Tech Stack
### **Backend**
- **Python**
- **FastAPI** (for API endpoints)
- **Groq AI API** (for chatbot responses)
- **LangChain** (for enhanced NLP and memory retention)
- **SQLite** (for user session storage)

### **Frontend**
- **Streamlit** (for an intuitive UI)

### **Other Tools**
- **Docker** (for containerization)
- **GitHub** (for version control)
- **Postman** (for API testing)

## 📂 Project Structure
```
├── backend
│   ├── chatbot.py
│   ├── memory.py
│   ├── model.py
│   ├── wellness_suggestion.py
│   ├── __init__.py
│
├── frontend
│   ├── frontend.py
│   ├── __init__.py
│
├── main.py
├── requirements.txt
├── README.md
```

## ⚙️ Installation & Setup
### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/AkhandPratapSingh11/wecaremo.git
cd emocare
```

### 2️⃣ **Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### 3️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Set Up Environment Variables**
Create a `.env` file in the root directory:
```ini
GROQ_API_KEY=your_groq_api_key_here
```

### 5️⃣ **Run the Application**
```bash
streamlit run main.py
```

## 📸 Screenshots
*(Upload UI snapshots here)*

## 🔗 Demo
[Live Demo](#) *(If hosted online)*

## 🛠️ Future Enhancements
- [ ] Multi-lingual support 🌍
- [ ] Integration with voice recognition 🎙️
- [ ] More detailed sentiment tracking 📊

## 📜 License
This project is licensed under the **MIT License**.

## 🙌 Contributors
- **Akhand Pratap Singh** ([@your-github](https://github.com/your-username))
- And other collaborators...

---
💡 *Feel free to contribute! Fork the repo, create a pull request, and help improve EmoCare.* 🚀

