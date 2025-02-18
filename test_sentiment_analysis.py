import unittest
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        # Positive Sentiment
        result_1 = sentiment_analyzer('I love working here')
        self.assertEqual(result_1['sentiment'], 'SENT_POSITIVE')

        # Negative Sentiment
        result_2 = sentiment_analyzer('I hate sitting here.')
        self.assertEqual(result_2['sentiment'], 'SENT_NEGATIVE')

        # Neutral Sentiment
        result_3 = sentiment_analyzer('I am John')
        self.assertEqual(result_3['sentiment'], 'SENT_NEUTRAL')

if __name__ == "__main__":
    unittest.main()