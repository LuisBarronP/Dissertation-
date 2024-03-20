import spacy
import webbrowser
import subprocess

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

def preprocess_command(command):
    # Tokenising the command and lemmatising the tokens, removing stop words and punctuation
    doc = nlp(command.lower())
    tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    return " ".join(tokens)

# Rules for intent recognition and entity extraction
def identify_intent_and_entities(preprocessed_text):
    if "search" in preprocessed_text:
        intent = "dynamic_search"
    elif "pause" in preprocessed_text:
        intent = "pause"
    else:
        intent = "unknown"
    entities = {"search_query": preprocessed_text}
    return intent, entities


#preprocess_text function
def preprocess_text(text):
    preprocessed_text = preprocess_command(text)
    
    # Identifying intent and entities based on the preprocessed text
    intent, entities = identify_intent_and_entities(preprocessed_text)
    
    print(f"Identified intent: {intent}, entities: {entities}")
    return intent, entities

def execute_command(intent, entities, commands):
    # Iterate through commands to find a match for the intent
    for command, details in commands.items():
        if command.lower() == intent.lower():
            if details['action'] == 'dynamic_search':
                # Handling dynamic search, using entities for the search query and opening a web browser
                search_query = entities.get('search_query', '')
                search_url = details['base_url'].format(search_query)
                webbrowser.open(search_url)
                print(f"Searching for: {search_query}")
            elif details['action'] == 'subprocess':
                # Execute a subprocess command based on the intent
                subprocess_command = details.get('command', [])
                subprocess.run(subprocess_command, shell=True)
            return True
    print("Command not found or not understood. Please try again.")
    return False
