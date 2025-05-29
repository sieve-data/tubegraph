# Tubegraph

- Any youtube channel mapped
- Forked from [Quartz](https://github.com/jackyzha0/quartz)

---

## 🔗 Web (Quartz) App

To run the Tubegraph web application locally:

### 1. Install dependencies

```bash
npm install
npx quartz build --serve
```

### 3. Set up environment variables

Create a `.env` file in the root of the project and add your Sieve API key:

```
SIEVE_KEY=your_sieve_api_key_here
```

Then open [http://localhost:3000](http://localhost:3000) in your browser to view the app.

---

## 🧠 Backend (Sieve Functions)

The backend logic for segment download and processing lives in the `sieve-functions/` directory.

### 1. Set up environment variables

Create a `.env` file inside the `sieve-functions/` directory:

```
OPENAI_API_KEY=
YOUTUBE_API_KEY=
GEMINI_API_KEY=
GITHUB_TOKEN=
```

### 2. Install dependencies

Navigate into the `sieve-functions/` directory and run:

```bash
pip install -r requirements.txt
```

### 3. Deploy your Sieve function

First, log in using your Sieve API key:

```bash
sieve login
```

Then deploy the function:

```bash
sieve deploy create_video.py
```

---

## ✅ Summary

- Web UI is built with **Quartz**
- Video downloading and processing is powered by a **Sieve function** (`create_video.py`)
