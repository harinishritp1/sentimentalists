import spacy
from data_preparation import get_text_from_indiankanoon_url
from spacy import displacy
from legal_ner import extract_entities_from_judgment_text

legal_nlp=spacy.load('en_legal_ner_trf')
judgment_text = get_text_from_indiankanoon_url('https://indiankanoon.org/doc/542273/')

preamble_spiltting_nlp = spacy.load('en_core_web_sm')
run_type='sent' ###  trade off between accuracy and runtime
do_postprocess=True 
combined_doc = extract_entities_from_judgment_text(judgment_text,legal_nlp,preamble_spiltting_nlp,run_type,do_postprocess)
