import pandas as pd
import re
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
from absa_funcs import counter_dictionary, sentiment_classification
from ast import literal_eval

tokenizer = AutoTokenizer.from_pretrained("yangheng/deberta-v3-base-absa-v1.1", use_fast=False)
model = AutoModelForSequenceClassification.from_pretrained("yangheng/deberta-v3-base-absa-v1.1")
classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)

def sentiment_classification(sentence_list, sentence_aspects, aspects_within, agg_term_dict):
    index_list = [i for i, values in enumerate(agg_term_dict.values()) for a in aspects_within if a in values]
    unique_asps = [a for a in aspects_within if all(a not in values for values in agg_term_dict.values())]

    
    
    for a in unique_asps:#iter through list of unique aspects
        count = 0
        for i, aspects in enumerate(sentence_aspects): #index value for the list of aspects and list of setences
            if not aspects:
                continue
        
            if a in aspects: #if aspect in the list
                classifier_output = classifier(sentence_list[i], text_pair=a)
                count += point_mapper[classifier_output[0]['label']]
            else:
               pass
        if count > 0:
            aspect_dict[a]['Positive'] +=1
        elif count == 0:
            aspect_dict[a]['Neutral'] +=1
        elif count <0 :
            aspect_dict[a]['Negative'] +=1


    for ind in list(set(index_list)):
        count = 0 
        aggregated_asps = list(agg_term_dict.values())[ind]
        for a in aggregated_asps:
            for i, aspects in enumerate(sentence_aspects):
                if not aspects:
                    continue
                
                if a in aspects:
                    classifier_output = classifier(sentence_list[i], text_pair=a)
                    count += point_mapper[classifier_output[0]['label']]
                else:
                   pass
        if count > 0:
            aspect_dict[aggterm_keys[ind]]['Positive'] +=1
        elif count == 0:
            aspect_dict[aggterm_keys[ind]]['Neutral'] +=1
        elif count <0 :
            aspect_dict[aggterm_keys[ind]]['Negative'] +=1


aspects = [# aspects]
 aggterms = [# list of tuples of of (aspect,[synonymous terms/phrases])]

aggterm_dict = dict(aggterms)

synonym_set = set([synonym for _, synonyms in aggterms for synonym in synonyms])

core_aspects = [agg[0] for agg in aggterms] + [aspect for aspect in  aspects if aspect not in synonym_set]

aggterm_keys = list(aggterm_dict.keys())
aspect_dict = counter_dictionary(core_aspects)
point_mapper = {'Negative': -1, 'Positive': 1, 'Neutral': 0}


df = pd.read_csv('totk_ aspects.csv',index_col=0)
df['sent_tokenized_reviews'] = df.sent_tokenized_reviews.apply(lambda x: literal_eval(x))
df['aspects_within'] = df.aspects_within.apply(lambda x: literal_eval(x))
df['sentence_aspects'] = df.sentence_aspects.apply(lambda x: literal_eval(x))

counter_dictionary(core_aspects)

(
    df.apply(lambda df_: sentiment_classification(df_.sent_tokenized_reviews,df_.sentence_aspects,df_.aspects_within, aggterm_dict),axis=1)
)

(pd.DataFrame.from_dict(aspect_dict, orient='index').reset_index().rename({'index':'Aspect'},axis='columns')).to_csv(' aspect_sentiments.csv')

print('analysis complete')