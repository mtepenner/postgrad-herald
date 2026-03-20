# 📰 Postgrad Herald

Postgrad Herald is an automated editorial system that transforms real-time news data into a high-prestige, vintage-style digital newspaper. By leveraging the **OpenAI GPT-4o** model, the system adopts the persona of a Pulitzer Prize-winning journalist to rewrite top headlines into formal news stories, which are then rendered into a classic HTML "Daily Herald" layout.

## 🚀 Features
* **Real-Time News Ingestion**: Fetches the latest global headlines across Politics, Sports, and Culture via NewsAPI.
* **AI-Driven Editorial**: Uses Large Language Models to rewrite snippets into 120-word authoritative news reports.
* **Dynamic Visuals**: Automatically retrieves relevant high-quality imagery from PEXELS based on story keywords.
* **Vintage Aesthetics**: A custom CSS-styled HTML template inspired by 20th-century broadsheets, featuring market tickers and multi-column layouts.
* **Automated Publishing**: A seamless Python pipeline that handles data fetching, AI processing, and Jinja2 template rendering in one execution.

## 🛠️ Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/postgrad-herald.git
    cd postgrad-herald
    ```

2.  **Install dependencies**:
    ```bash
    pip install requests openai jinja2
    ```

3.  **Configure API Keys**:
    Open `publisher.py` and replace the placeholders with your unique keys:
    * `OPENAI_KEY`
    * `NEWS_KEY`
    * `PEXELS_KEY`

## 📖 Usage

Run the main publisher script to generate today's edition:

```bash
python publisher.py
```

The system will assemble the editorial team, fetch news, and perform the AI rewrite. Once finished, open **`herald_published.html`** in any web browser to view your formatted newspaper.

## 🧰 Technologies Used
* **Python**: Core application logic.
* **OpenAI GPT-4o**: For sophisticated text generation and persona-based rewriting.
* **Jinja2**: For HTML templating and data injection.
* **HTML/CSS**: For the "Daily Herald" visual framework.
* **NewsAPI & PEXELS API**: For live data and media sourcing.
