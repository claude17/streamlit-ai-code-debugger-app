# AI Code Debugger App
A Streamlit app that analyzes screenshots of code with Gemini and returns debugging hints or a corrected solution.

---

## Table of Contents

- [About the Project](#about-the-project)
- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [Dependencies](#dependencies)
- [Installation & Setup](#installation--setup)
- [Folder Structure](#folder-structure)
- [Contributions](#contributions)
- [How to Contribute](#how-to-contribute)
- [License](#license)
- [Contact](#contact)

---

## About the Project

AI Code Debugger App is a lightweight Streamlit application built to help developers understand code issues from screenshots. Users upload up to three images of code, choose whether they want hints or a full solution, and receive AI-generated guidance powered by Google's Gemini API.

---

## Project Overview

This project is designed for quick debugging support when code is captured as an image rather than copied as text. The app keeps the workflow simple:

1. Upload one to three screenshots of code.
2. Choose between hints or a solution with code.
3. Submit the request and review the generated analysis.

The interface is intentionally minimal so the focus stays on the code being reviewed.

---

## Key Features

- Image-based code review — upload screenshots of code in `jpg`, `jpeg`, or `png` format.
- Multiple response modes — choose between debugging hints or a full solution with code.
- Gemini-powered analysis — generates responses using Google's generative AI models.
- Simple Streamlit interface — clean, fast, and easy to use in the browser.
- Input validation — prevents submission unless an image and output mode are selected.

---

## Tech Stack

**Frontend/UI:** Streamlit

**Backend Logic:** Python

**AI Model:** Google Gemini via `google-genai`

**Configuration:** `python-dotenv`

**Media Handling:** Pillow

**Tools:** Git · VS Code

---

## Dependencies

Key dependencies used by the app:

```json
{
  "streamlit": "^1.56.0",
  "google-genai": "^1.73.1",
  "python-dotenv": "^1.2.2",
  "pillow": "^12.2.0",
  "requests": "^2.33.1"
}
```

---

## Installation & Setup

1. Clone the repository and install dependencies:

```bash
git clone https://github.com/claude17/streamlit-ai-code-debugger-app.git
cd streamlit-ai-code-debugger-app
pip install -r requirements.txt
```

2. Create a `.env` file in the project root and add your Gemini API key:

```env
GEMINI_API_KEY=your_gemini_api_key
```

3. Run the application:

```bash
streamlit run app.py
```

4. Open the local URL shown in the terminal, then upload code screenshots and choose a response mode.

---

## Folder Structure

```plaintext
streamlit-ai-code-debugger-app/
├── app.py
├── api_call.py
├── requirements.txt
└── README.md
```

---

## Contributions

Contributions are welcome. If you improve the prompt quality, refine the UI, or expand the debugging workflow, please open a pull request.

---

## How to Contribute

1. Fork the repository.
2. Create a feature branch.
3. Make your changes and test the app locally.
4. Open a pull request with a clear summary of the update.

---

## License

No license file is included in this repository yet. Add one if you want to define how others may use or distribute the project.

---

## Contact

If you'd like to collaborate or suggest improvements, open an issue or pull request on the repository.
