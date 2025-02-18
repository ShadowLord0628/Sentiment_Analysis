# Sentiment Analysis

## Overview
Sentiment Analysis is a Python-based project that utilizes **Watson AI's NLP service** to determine the sentiment of a given text. The model analyzes the text and classifies it as **positive, negative, or neutral**, along with a confidence score.

## Features
- Uses **IBM Watson's Sentiment Analysis API**
- Provides **sentiment classification** (positive, negative, neutral)
- Returns **confidence scores** for predictions
- Implements **error handling** for API failures

## Installation
### Prerequisites
Ensure you have Python **3.11** installed on your system. You will also need the following dependencies:

```bash
pip install requests
pip install flask
```

## Usage
### Import the module and analyze sentiment
```python
from sentiment_analysis import sentiment_analyzer

text = "I love programming!"
result = sentiment_analyzer(text)
print(result)
```

### Sample Output
```json
{
    "sentiment": "positive",
    "score": 0.95
}
```

## Project Structure
```
Sentiment_Analysis/
│-- SentimentAnalysis/
    |-- __init__.py # initializes the package SentimentAnalysis
    |-- sentiment_analysis.py # main sentiment analysis script
|-- static/
    |-- mywebscript.js # manages the webpage
|-- templates/
    |-- index.html # main page
|-- server.py # main flask application which deploys the web application
|-- test_sentiment_analysis.py # testing for sentiment_analysis function
│-- README.md  # Project documentation
│-- requirements.txt  # List of dependencie
```

## Error Handling
The function gracefully handles errors using Python's `requests` module. If the API request fails, it returns:
```json
{
    "error": "Request failed: <error message>",
    "sentiment": "UNDEFINED",
    "score": "UNDEFINED"
}
```

## Contributing
Feel free to submit pull requests or report issues in the **[GitHub repository](https://github.com/ShadowLord0628/Sentiment_Analysis)**.

## License
This project is licensed under the **MIT License**. See `LICENSE` for more details.

## Author
**ShadowLord0628** 

---
Happy coding! 🚀

