import pandas as pd
import os
from extract_post_features import extract_features, load_post

def calculate_post_score(features: dict) -> float:
    """Calculating a performance score based on extracted features."""
    
    score = 0.0
    
    # Text length - Reasonable length (50-300 words) gets a boost
    if 50 <= features["word_count"] <= 300:
        score += 1.0
        
    # Emojis - Posts with emojis tend to perform better
    if features["emoji_count"] > 0:
        score += features["emoji_count"] * 0.5
        
    # Hashtags - Using 1-3 relevant hashtags can increase visibility
    if 1 <= features["hashtag_count"] <= 3:
        score += 0.5
        
    # CTA - Presence of a call-to-action can boost engagement
    if features["contains_apply_cta"]:
        score += 1.0
        
    # Offers - Mentioning grants or programs can increase relevance
    if features["mentions_grant"]:
        score += 0.5
    if features["mentions_program"]:
        score += 0.5
        
    # Topics - Mentioning trending topics like AI, data, or climate can boost interest
    if features["mentions_ai"]:
        score += 0.5
    if features["mentions_data"]:
        score += 0.5
    if features["mentions_climate"]:
        score += 0.5
        
    # Tone - Positive tone can enhance engagement
    if features["tone"] == "positive tone":
        score += 0.5
    elif features["tone"] == "negative tone":
        score -= 0.5
        
    return score

def main():
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    text_origin = os.path.join(script_dir, "../data/raw/post_text.txt")
    output = os.path.join(script_dir, "../outputs/post_performance_score.csv")
    
    # Load the post text
    post_text = load_post(text_origin)
    
    # Extract features
    features = extract_features(post_text)
    
    # Calculate the performance score
    score = calculate_post_score(features)
    features["performance_score"] = score
    
    # Save to CSV
    df = pd.DataFrame([features])
    df.to_csv(output, index=False)
    
    print(f"Post Score calculated and saved to {output}: {score:.2f}")

if __name__ == "__main__":
    main()