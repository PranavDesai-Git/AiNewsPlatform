<div align="center">
  <img src="https://i.ibb.co/zTF2kXVj/Olla-News-1-removebg-preview.png" width="200" />
  <h1>OllaNews</h1>
  <p><i>"News without the BS"</i></p>

  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
  ![Django](https://img.shields.io/badge/django-%23092e20.svg?style=for-the-badge&logo=django&logoColor=white)
  ![Ollama](https://img.shields.io/badge/Ollama-LLM-blue?style=for-the-badge)
</div>

---

## Overview
Ollanews is a news reader that allows you to search for topics of news, fetch articles by strippping away all the ads and also provide an ai summary for the artilces

### ️ How it Works
```mermaid
flowchart TD
    D[User requests summary] --> A[RSS News]
    A -->|fetched| B(Converted into text)
    B --> C(Summarized by Ollama)
    C --> U(Sent to the user)
    U --> D
```

---
### Modules Developed
#### Frontend
- Landing Page: Simple search bar interface built with Django templates and CSS. It captures user-defined news topics and sends them to the backend via a GET request.
- Article List View: A feed displaying the title, source, and publication date of the top 10 articles retrieved from the RSS engine. Each entry includes a button to trigger the summarization process.
- Summary Display: An asynchronous UI component that uses JavaScript (Fetch API) to request and display the 3B model's output without reloading the entire page.
Backend
- RSS Aggregator: A Python module using feedparser to connect to Google News and other RSS XML endpoints. It filters results based on the user's search query.
- HTML Sanitizer: A cleaning script using BeautifulSoup to strip all <script>, <style>, and <div> tags, leaving only raw <p> tag content to reduce the token count for the LLM.
- Ollama API Client: A local HTTP request handler that sends the sanitized text to the Ollama server (running Llama 3B) using a specific system prompt to enforce a concise summary format.
- Django Controller: The central views.py logic that coordinates the flow: receiving the search query, calling the aggregator, passing text to the AI client, and returning a JSON response to the frontend.
