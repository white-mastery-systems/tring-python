# TTS Client

A simple and efficient Text-to-Speech (TTS) client for Tring TTS Service that allows users to convert text into spoken audio.

## Features
- **Customizable Voices**: Choose from different voices and languages.
- **Easy Integration**: Simple API for easy integration into your applications.
- **Cross-Platform**: Works on Windows, macOS, and Linux.

## Installation

pip
```bash
pip install git+https://github.com/white-mastery-systems/tring-python.git
```

## Usage

```bash
from tring.tts import generate

generate("Hi, this is Kevin here. How can I help you?", 'kevin', 1.25, "sample.wav")
```
