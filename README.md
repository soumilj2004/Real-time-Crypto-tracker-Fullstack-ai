# Real-Time Crypto Tracker with AI Market Assistant

A professional-grade web dashboard that tracks real-time cryptocurrency prices and provides AI-powered market insights. Inspired by TradingView, this project includes dynamic charting, dark/light mode, historical data visualization, and an integrated AI assistant using Mistral via Ollama.

---

## Features

- **Real-Time Price Tracking**  
  Displays live prices for multiple assets including Bitcoin (BTC), Ethereum (ETH), and Apple (AAPL).

- **Interactive Charting**  
  View multiple assets on a single responsive chart with up-to-date prices.

- **Historical Data Visualization**  
  Automatically loads the last 3 hours of price history for selected assets.

- **Interval Customization**  
  Choose update intervals such as 15 seconds or 30 seconds.

- **Dark and Light Mode**  
  Toggle between themes for a better visual experience.

- **AI-Powered Market Insights**  
  Ask natural language questions such as “Why is ETH falling today?” and get real-time responses powered by Ollama (Mistral model).

- **Symbol Tracking Control**  
  Use checkboxes and a "Track" button to manage which assets appear on the dashboard.

---
### Images
<img width="779" height="776" alt="image" src="https://github.com/user-attachments/assets/4d97d95e-6ae9-4cad-a352-c4c766ab0f67" />
<img width="526" height="851" alt="image" src="https://github.com/user-attachments/assets/8d1f9548-1bc5-4cba-90d6-37ef11508ef3" />

---
## Technologies Used

### Frontend
- HTML, CSS, JavaScript
- Chart.js for rendering dynamic price charts

### Backend
- FastAPI for RESTful API endpoints
- httpx for asynchronous API requests
- CoinGecko API for crypto market data
- Ollama (Mistral) for local LLM inference

---

## 📁 Folder Structure

```text
price-tracker/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   ├── routes/
│   ├── services/
│   ├── db/
│   └── utils/
│
└── frontend/
    ├── index.html
    ├── style.css
    ├── script.js
    └── chart.js
```

---

## Getting Started

### 1. Clone the Repository
\`\`\`bash
git clone https://github.com/soumilj2004/Real-time-Crypto-tracker-backend-ai.git
cd Real-time-Crypto-tracker-backend-ai
\`\`\`

### 2. Set Up Backend (WSL or Linux)
\`\`\`bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
\`\`\`

### 3. Set Up Frontend
Open \`frontend/index.html\` in your browser directly or use a development server (e.g., Live Server in VSCode).

### 4. Run Ollama Locally
\`\`\`bash
ollama run mistral
\`\`\`
Make sure it is accessible on \`http://localhost:11434\`.

---

## Example Questions for AI Assistant

- Why is Bitcoin down today?
- What is the current trend of Ethereum?
- Can you summarize Apple stock movement this week?

---

## License

This project is licensed under the MIT License.

---

## Author

**Soumil Jain**  
Portfolio: [https://github.com/soumilj2004](https://github.com/soumilj2004)

---

## Acknowledgments

- [CoinGecko API](https://www.coingecko.com/)
- [Ollama](https://ollama.com/)
- [Chart.js](https://www.chartjs.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
EOF

# Commit and push to GitHub
git add README.md
git commit -m "Add professional README"
git push
