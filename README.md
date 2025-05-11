# 🎭 Real Recognize Real – Lightweight Deepfake Detection Platform

**Finalist – Deepfake Detection Challenge 2025 @ UM6P 🇲🇦**

**Real Recognize Real** is a complete, locally deployable deepfake detection platform designed for accessibility, speed, and robustness. Built with a lightweight EfficientNet-B0 model and a full-stack web interface, it empowers users to verify manipulated images and videos — even on modest hardware.

---

## 🚀 Features

- ✅ **Locally Deployable** — no GPU or cloud required
- 🎯 **EfficientNet-B0** backbone (fast + compact: ~15MB)
- 🖼️ **Image, batch, and video support** via frame sampling
- 🧠 **Adversarial robustness**: patch attacks, data poisoning & evasion tested
- 🌐 **REST API (Flask)** + **Web UI (Django)**
- 📊 Real-time prediction with confidence scores
- 📚 Full technical documentation & training notebook

---

## 🗂️ Project Structure

```
├── frontend/    # Django web interface (user upload + result view)
├── backend/     # Flask API for inference (/predict, /batch, /video)
├── model/       # Trained PyTorch model (EfficientNet-B0)
├── notebook/    # Colab notebook for training & evaluation
├── docs/        # PDF documentation of full architecture & results
└── README.md    # You are here
```

---

## 📸 Demo

[![Watch the demo video](https://img.youtube.com/vi/YOUR_VIDEO_ID_HERE/0.jpg)](https://www.youtube.com/watch?v=YOUR_VIDEO_ID_HERE)

---

## 🧪 Model Performance

| Metric | Value |
|-------------|------------|
| Accuracy | 82.18% |
| F1-Score | 0.8168 |
| Precision | 0.7986 |
| Recall | 0.8358 |
| Inference | ~70ms (T4) |
| Model Size | ~15MB |

The model was trained on the **Deepfake Faces Kaggle dataset**, balanced to 34K images.

---

## 📦 Local Setup

### 🔧 Requirements

- Python 3.8+
- PyTorch
- OpenCV
- Django
- Flask
- ngrok (optional, for tunneling)

### 🔄 Installation

```bash
git clone https://github.com/your-username/real-recognize-real.git
cd real-recognize-real

# Install dependencies
pip install -r requirements.txt

# Launch backend API (Flask)
cd backend/
python app.py

# Launch frontend (Django)
cd ../frontend/
python manage.py runserver
```

Use ngrok if you want public access to the Flask API.

---

## 🧪 Colab Notebook

You can train or fine-tune the model using the Colab Notebook. It includes:
- Dataset preparation & balancing
- EfficientNet-B0 model setup
- Training curves
- Evaluation metrics & Grad-CAM visualizations

---

## 🛡️ Adversarial Attack Research

Explore adversarial attacks on face recognition and deepfake systems:

🧪 GitHub Repository Includes:
- Patch-based attacks
- Data poisoning experiments
- Evasion attacks
- Real-world implications for AI security

---

## 📖 Documentation

Comprehensive PDF documentation includes:
- Architecture diagrams
- Model pipeline
- API endpoints
- Dataset description
- Evaluation
- Adversarial defense research

📄 [Read the Docs](#)

---

## 🧩 Future Work

- Integrate NLP/text-based fake news detection
- Add multimodal credibility scoring (image + context)
- Optimize for mobile edge deployment (e.g., TensorFlow Lite)
- Expand dataset for improved generalization

---

## 🤝 Contributing

Pull requests, ideas, and forks are welcome!

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a pull request

---

## 👤 Author

**Mouaad Ait Ahlal**
- 📧 mouadaitahlal@gmail.com
- 🔗 GitHub – [@mouaad11](https://github.com/mouaad11)

---

## 📜 License

MIT License — feel free to use and adapt for non-commercial or educational purposes. Attribution appreciated.
