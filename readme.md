<div align="center">
  <img src="https://ibb.co/NgF9Ctn0" width="100" />
  <h1>📰 OllaNews</h1>
  <p><i>News without bs</i></p>
</div>


# Project Idea

* Fetches news from RSS/Google
* Sanitizes the news
* Turns it into a plain text file
* Text file is sent to Ollama
* Ollama summarizes the thing
* Writes a file called 'summary'
* We use a HTTP POST to send it to the frontend
* Frontend is in HTML/CSS/JS
* Backend written in Python Django


![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092e20.svg?style=for-the-badge&logo=django&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-LLM-blue?style=for-the-badge)
---

### Modules Split

#### HTML Frontend [Sadiyah]
* **Landing page:** A page with a textbox in the middle and a button saying "go" kinda like google homepage. In the textbox the user can type the topic of news.
* **News list page:** Once the user hits go it gives you top 10 news regarding that in the past few days (this is a dynamic page, it will receive a JSON file with a bunch of news articles). There is also a button that says "summarize" which will do a HTTP request to the backend and will retrieve a JSON file with the summary. The summary should be displayed on top of the news feed.
* **News read page:** The user can also click on a specific news article and when they click that it sends a HTTP request which retrieves the news article in plain text with everything stripped down. There is also a summarize button here.

#### Python Backend [Pranav]
* Fetch data using some library
* Sanitize it
* Send it to a local LLM probably Ollama 3B model
* Write a HTTP server to respond to frontend (Django)

---

### Timeline

* **Deadline:** 29th March
* **Today:** 25th

#### 25th & 26th
- [ ] Landing page
- [ ] Fetching module
- [ ] Sanitization module

#### 26th & 27th
- [ ] Ollama setup
- [ ] HTTP server with Django
- [ ] News list page
- [ ] News read page

#### 28th
- [ ] Polish/buffer
