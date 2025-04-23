# AI Chat Assistant with Groq and Chainlit

A powerful AI chat assistant built using Groq's API with Llama 2 model, featuring streaming responses and a beautiful web interface powered by Chainlit.

## Features

- 🤖 AI-powered chat assistant using Groq's Llama 2 model
- 🌊 Real-time streaming responses
- 💬 Interactive web interface with Chainlit
- 🔄 Support for both streaming and non-streaming modes
- 📝 Conversation history management
- 🔒 Secure API key management with environment variables

## Prerequisites

- Python 3.11+
- Groq API key
- UV package manager

## Installation

1. Clone the repository:

```bash
git clone https://github.com/MuhammadRaffey/Agents-sdk-streaming
cd Agents-sdk-streaming
```

2. Install dependencies using UV:

```bash
uv sync
```

3. Create a `.env` file in the root directory and add your Groq API key:

```
GROQ_API_KEY=your_api_key_here
```

## Usage

### Running the Chat Interface

To start the Chainlit web interface:

```bash
uv run chainlit run src/practice/main.py
```

The application will start a local server, and you can access the chat interface through your web browser.

### Running in Console Mode

To run the assistant in console mode (streaming):

```bash
python src/practice/main.py
```

## Project Structure

```
.
├── src/
│   └── practice/
│       └── main.py
├── .env
└── README.md
```

## Configuration

The application can be configured through the following environment variables:

- `GROQ_API_KEY`: Your Groq API key (required)

## Development

The project uses:

- Groq API for AI model access
- Chainlit for the web interface
- Python-dotenv for environment management
- UV for package management

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
