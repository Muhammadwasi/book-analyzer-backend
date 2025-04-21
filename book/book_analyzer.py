
from client.grok import GroqClient
from book.prompts import get_first_prompt_with_text, get_subsequent_prompt_with_text
from collections import defaultdict
from book.utils import extract_json, split_into_max_token_chunks

def analyze_book_using_llm(text: str) -> dict:
    chunks = split_into_max_token_chunks(text=text, max_tokens=20000)
    
    analyzed_chunks = analyze_chunks_using_llm(chunks)
    
    analyzed_chunks_json = extract_json_from_llm_response(analyzed_chunks)
        
    return merge_jsons(analyzed_chunks_json)

def analyze_chunks_using_llm(chunks):
    responses = []
    groq = GroqClient()
    if chunks:    
        response = groq.ask_as_user(get_first_prompt_with_text(chunks[0]))
        responses.append(response)
        for chunk in chunks[1:]:
            response = groq.ask_as_user(get_subsequent_prompt_with_text(chunk))
            responses.append(response)

    return responses

def merge_jsons(analyzed_chunks_json):
    interaction_map = defaultdict(lambda: defaultdict(int))

    for chunk in analyzed_chunks_json:
        for char in chunk["character_interactions"]:
            name = char["character_name"]
            for interaction in char["interacted_with"]:
                partner = interaction["name"]
                interaction_map[name][partner] += interaction["count"]

    merged = []
    for char, partners in interaction_map.items():
        merged.append({
            "character_name": char,
            "interacted_with": [{"name": p, "count": c} for p, c in partners.items()],
            "total_interactions": sum(partners.values())
        })
    
    return {"character_interactions": merged}

def extract_json_from_llm_response(analyzed_chunks):
    analyzed_chunks_json = []
    for analyzed_chunk in analyzed_chunks:
        analyzed_chunks_json.append(extract_json(analyzed_chunk))
    return analyzed_chunks_json