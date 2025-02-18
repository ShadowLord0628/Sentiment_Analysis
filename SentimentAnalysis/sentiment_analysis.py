"""
Sentiment Analysis Module

This module provides a function to analyze sentiment using Watson AI's NLP service.
It sends a text input to the Watson API and returns the sentiment label and score.

Dependencies:
- requests: Used for making HTTP requests to the Watson API.

Usage:
>>> sentiment_analyzer("I love programming!")
{'sentiment': 'positive', 'score': 0.95}
"""

import requests  # Third-party import

def sentiment_analyzer(text_to_analyse):
    """
    Analyze sentiment using Watson AI API.

    Args:
        text_to_analyse (str): The text to be analyzed.

    Returns:
        dict: A dictionary containing the sentiment label and score.
    """
    url = """https://sn-watson-sentiment-bert.labs.skills.network
    /v1/watson.runtime.nlp.v1/NlpService/SentimentPredict"""

    headers = {
        "grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"
    }

    obj = {"raw_document": {"text": text_to_analyse}}

    try:
        res = requests.post(
            url, json=obj, headers=headers, timeout=10
        )  # Added timeout to prevent hanging
        res.raise_for_status()  # Raise exception for HTTP errors
        formatted_response = res.json()

        if res.status_code == 200:
            state = formatted_response.get("documentSentiment", {}).get("label")
            score = formatted_response.get("documentSentiment", {}).get("score")
        else:
            state = None
            score = None
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
        state = None
        score = None

    return {"sentiment": state, "score": score}
