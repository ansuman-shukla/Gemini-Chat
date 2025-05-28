# Context-Aware Gemini Chat

A simple interactive chatbot using Google Gemini API that preserves conversation context across multiple turns.

## Setup

1. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

2. **Add your Gemini API key:**
   - Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Add it to `.env` file:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```

## Usage

Run the chat application:
```powershell
python gemini_chat.py
```

- Set optional model parameters (temperature, top-p) when prompted
- Chat with Gemini across multiple turns with preserved context
- Type `quit` or `exit` to end the conversation

## Features

- 🤖 **Context preservation** - Gemini remembers the entire conversation
- 🎛️ **Configurable parameters** - Adjust temperature and top-p values
- 💬 **Multiple turns** - Unlimited conversation length
- 📝 **Console interface** - Simple text-based interaction
