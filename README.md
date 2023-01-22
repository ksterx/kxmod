# kxmod

This is a repository of utilities.

`convert`: Convert files between different formats.

## Installation

```bash
pip install -e .
```

## Usage

### Bot
Send messages to Slack/LINE.
```python
from kxmod.service import SlackBot

bot = SlackBot()

bot.say('Hello World!')
bot.upload("cat", "cat.jpg")

@bot.listen
def hello_world():
    return "Hello World!"
```
