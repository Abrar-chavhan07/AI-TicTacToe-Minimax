
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# Sample dataset
data = {
    "text": [
        "I am very happy today",
        "This is the best day ever",
        "I feel sad and depressed",
        "I am very angry right now",
        "I love this place",
        "I hate everything",
        "This makes me joyful",
        "I feel terrible today",
        "I am excited about the future",
        "This is frustrating"
    ],
    "emotion": [
        "happy",
        "happy",
        "sad",
        "angry",
        "happy",
        "angry",
        "happy",
        "sad",
        "happy",
        "angry"
    ]
}

df = pd.DataFrame(data)

# Create ML pipeline
model = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('classifier', MultinomialNB())
])

# Train model
model.fit(df["text"], df["emotion"])

# Test input
while True:
    text = input("Enter a sentence: ")
    
    if text == "exit":
        break
    
    prediction = model.predict([text])
    print("Detected Emotion:", prediction[0])
