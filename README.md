# Aegis text generation node

Generates text. Powered by [aitextgen](https://github.com/minimaxir/aitextgen).

## Environment
* `PORT` - port to listen on (defaults to 80)
* `DEFAULT_TEMPERATURE` - temperature to use if not provided in query (defaults to 0.7)
* `DEFAULT_MAX_LENGTH` - max length to use if not provided in query (defaults to 1024)

## Usage
POST a JSON string to this node, or provide an object with the following format (each key is optional):
```json
{
    "prompt": "Unicorns are cool because ",
    "temperature": 1.0,
    "length": 100
}
```

## TODO
* support other models such as "minimaxir/hacker-news" or "EleutherAI/gpt-neo-125M" via MODEL env variable
