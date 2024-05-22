import spacy
from django.conf import settings
from .custom_retriever import CustomRetriever

class MovieChatbot:
    def __init__(self):
        self.retriever = CustomRetriever()
        self.nlp = spacy.load('en_core_web_sm')

    def chat(self, user_input):
        keywords = self.extract_keywords(user_input)
        movies = self.retriever.retrieve(keywords)
        response = self.generate_response(movies)
        return response

    def extract_keywords(self, user_input):
        doc = self.nlp(user_input)
        
        # Extract proper nouns and noun phrases
        keywords = []
        for token in doc:
            if token.pos_ in ['PROPN', 'NOUN'] and not token.is_stop:
                keywords.append(token.text)

        # Also consider named entities
        for ent in doc.ents:
            if ent.label_ in ['PERSON', 'WORK_OF_ART', 'ORG', 'GPE']:
                keywords.append(ent.text)
        
        # Remove duplicates while preserving order
        keywords = list(dict.fromkeys(keywords))
        return ' '.join(keywords)

    def generate_response(self, movies):
        if not movies:
            return "No movies found matching your query."
        else:
            return "here are some suggestion for you"
            