
---

###

````markdown
# Travel Planner

This is an intelligent travel itinerary planner built with Python and Streamlit that uses AI to generate detailed day-wise travel plans. Currently, it supports:

Travel Itinerary Generation  
Emailing the itinerary to the user  

> **Note:** This version uses only the **free email functionality** and requires no paid API services. LLM-based itinerary planning is modular but disabled until a valid API key is provided.

---

## Main Features

- Generate detailed travel plans based on user input
- Email the generated itinerary directly to the user's inbox
- Modular design allows adding PDF generation and maps later

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/agentic-ai-travel-planner.git
cd agentic-ai-travel-planner
````

### 2. Create a Virtual Environment and Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the project root with the following:

```ini
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_gmail_app_password
```

**Important:**
Use a [Gmail App Password](https://support.google.com/accounts/answer/185833?hl=en).
You must enable 2-Step Verification in your Google Account for this to work.

---

## Running the App

```bash
streamlit run main.py
```

---

## Project Structure

```bash
agentic_travel_ai/
│
├── main.py                      # Streamlit frontend
├── .env                         # Email credentials (Gmail App Password)
├── requirements.txt             # Python dependencies
│
├── prompts/
│   └── itinerary_prompt.txt     # Jinja2 prompt template for LLM
│
├── agent/
│   ├── planner.py               # (Optional) OpenAI itinerary generation logic
│   ├── email_sender.py          # SMTP-based email service
│   ├── pdf_generator.py         # (Disabled) PDF generation logic
│   └── map_embedder.py          # (Disabled) Google Maps embed URL
```

---

## Limitations (Current Version)

*  No OpenAI-based planning without valid `OPENAI_API_KEY`
*  No embedded maps or PDF download
*  Email functionality works 100% for free with Gmail App Passwords

---

## To Enable Full AI & Export Features

* Add your OpenAI API Key to `.env`:

  ```env
  OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx
  ```
* Enable PDF export by installing `wkhtmltopdf` and using `pdfkit`
* Add your Google Maps embed API key to use maps

---

## Credits

* Built with Python, Streamlit, and modular AI-based design
* Email powered by Gmail SMTP using secure App Passwords

---

## License

MIT License — use freely, modify, and share.

```

---

Let me know if you’d like a markdown badge row (Python , Streamlit , MIT ), or if you're deploying it publicly and want deployment instructions (e.g., on Streamlit Cloud or Hugging Face Spaces).
```
