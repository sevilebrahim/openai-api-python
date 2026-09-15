# OpenAI API Project with Python 🤖

What happens when a Python program can send a question to an AI model and receive an answer back?

That is the idea behind this project.

This project connects a Python application to the OpenAI API. The user enters a question in the terminal, the program sends it to the selected model, and the generated response is displayed directly in the console.

The goal of this project was to understand how an external AI service can be connected to a Python program and turned into a simple interactive application.

### The Basic Flow

```text
User Question
      ↓
Python Program
      ↓
OpenAI API
      ↓
AI Model
      ↓
Generated Response
```

The program waits for the user to enter a question, sends that text through the API, and prints the model's response.

Even though the code is small, it introduces an important idea: Python does not always have to do everything locally. It can communicate with an external service, send data, receive a result, and use that result inside the application.

### Technologies

* Python
* OpenAI API
* OpenAI Python Library

### Example

A user can enter something like:

```text
Enter your question: What is machine learning?
```

The application then sends the question to the API and displays the generated answer.

### Running the Project

Install the OpenAI library:

```bash
pip install openai
```

Before running the program, add your OpenAI API key as an environment variable.

Then run:

```bash
python openai_api.py
```

### Keeping the API Key Safe

The API key should never be written directly inside the source code or uploaded to GitHub.

Using an environment variable keeps the secret separate from the project code and helps prevent accidentally exposing the key publicly.

### What I Learned

This project was my introduction to connecting Python with an AI API.

While building it, I practiced working with external services, sending user input to an API, receiving structured responses, and displaying the result inside a Python program.

It also gave me a first look at how AI-powered features can be added to ordinary Python applications without building the entire AI system from scratch.

### Future Ideas

This project could grow into a more complete AI assistant by adding conversation history, a graphical interface, voice input, text-to-speech, or different AI-powered commands.

For now, it is a simple starting point for experimenting with AI and Python together.
