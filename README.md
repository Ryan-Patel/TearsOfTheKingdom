Two notebooks:
TOTK_LDA is a notebook where I do some preprocessing on reviews for the game The Legend of Zelda: Tears of The Kingdom. Then I run the text through
MALLETS LDA topic model to identify areas of the game that players talk about in positive and negative reviews,

TOTK_aspect_sentiment_analysis: With the same dataset I use 'yangheng/deberta-v3-base-absa-v1.1' - an aspect based sentiment classifier
to determine the sentiment of a selection of aspects. These are informed bythe topic keywords from the LDA (plus some of my own imagination). The 
results are visualised indicating areas of the game that are heavily criticised and could be addressed in future installments.
