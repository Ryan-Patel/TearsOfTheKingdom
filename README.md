Two notebooks:
TOTK_LDA is a notebook where I do some preprocessing on reviews for the game The Legend of Zelda: Tears of The Kingdom. Then I run the text through
MALLETS LDA topic model to identify areas of the game that players talk about in positive and negative reviews,

TOTK_aspect_sentiment_analysis: With the same dataset I use 'yangheng/deberta-v3-base-absa-v1.1' - an aspect based sentiment classifier. The topic keywords from the LDA topic model (plus some of my own imagination) informed the list of pre defined aspects. By counting the frequency of each sentiment classification for each aspects, along with a few simple visualisations we can ee a quantitative representation of areas of the game that recieved positive and negative responses.

PART II

totk_absa_aspect.py - model script
TOTK_Aspect_Detection.ipynb - EDA on the individual aspects
TOTK_ABSA_II.ipynb - Visualising results and commenting on key observations and differences with original model.

I re ran the model but with 3 main differences:
1. I ran a model for each aspect group "COMBAT", "VISUAL PRESENTATION", "AUDIO" etc. Saving the scripts containing the models in different .py files.
2. I explored a larger range of aspects for each aspect group, ensuring each group and aspects within each group were less vage and more particular/
3. Instead of running the model across the entire review text I ran it only on the sentences that aspects were found in.

This was done to speed up the model and to potentially avoid "cross-contamination" of certain aspects and sentiments.


