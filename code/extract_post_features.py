import os
import re
import pandas as pd
from textblob import TextBlob

def load_post(filepath: str) -> str:
    """Load the raw LinkedIn post text."""
    
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def extract_features(text: str) -> dict:
    """Extract text-based features from the LinkedIn post."""
    
    word_count = len(text.split())
    sentence_count = len(re.split(r'[.!?]', text))
    character_count = len(text)
    hashtag_count = len(re.findall(r"#\w+", text))
    emoji_count = sum(1 for char in text if not char.isascii())
    
    lower_text = text.lower()
    
    cta_keywords = ["find out more", "learn more", "apply", "register", "join", "download","contact us"]
    contains_apply_cta = int(any(k in lower_text for k in cta_keywords))
    
    # Offer features
    mentions_grant = int("grant" in lower_text)
    mentions_program = int("program" in lower_text)
    
    # Topics
    mentions_ai = int("artificial intelligence" in lower_text or "ai" in lower_text)
    mentions_data = int("data" in lower_text)
    mentions_climate = int("climate" in lower_text)
    
    # Sentiment
    blob = TextBlob(text)
    tone_polarity = blob.sentiment.polarity

    if tone_polarity > 0.1:
        tone = "positive tone"
    elif tone_polarity < -0.1:
        tone = "negative tone"
    else:
        tone = "neutral tone"
        
    return {
        "word_count": word_count,
        "sentence_count": sentence_count,
        "character_count": character_count,
        "hashtag_count": hashtag_count,
        "emoji_count": emoji_count,
        "contains_apply_cta": contains_apply_cta,
        "mentions_grant": mentions_grant,
        "mentions_program": mentions_program,
        "mentions_ai": mentions_ai,
        "mentions_data": mentions_data,
        "mentions_climate": mentions_climate,
        "tone_polarity": tone_polarity,
        "tone": tone
    }
    
def main():
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    text_origin = os.path.join(script_dir, "../data/raw/post_text.txt")
    output = os.path.join(script_dir, "../outputs/post_features.csv")
    
    post_text = load_post(text_origin)
    features = extract_features(post_text)
    
    df = pd.DataFrame([features])
    df.to_csv(output, index=False)
    
    print(f"Features extracted from the post and saved to {output}")
    
if __name__ == "__main__":
    main()
