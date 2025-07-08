import langchain
from langchain.llms import GPT
from langchain.chains import LLMChain

# Define the sentiment analysis prompt
def sentiment_analysis(message):
    prompt = f"Classify the sentiment of the following message as either Positive or Negative: {message}"
    return prompt

# Define the categorization prompt for negative sentiments
def categorize_negative_sentiment(message):
    prompt = f"Classify the negative sentiment of the following message into one of three categories: 'Product Issue', 'Service Complaint', or 'General Dissatisfaction': {message}"
    return prompt

# Define the sentiment analysis chain
def analyze_sentiment(message):
    llm = GPT()
    sentiment_chain = LLMChain(llm, prompt=sentiment_analysis(message))
    sentiment_output = sentiment_chain.run(message)
    sentiment = sentiment_output.strip()
    
    if sentiment == "Negative":
        categorize_chain = LLMChain(llm, prompt=categorize_negative_sentiment(message))
        categorize_output = categorize_chain.run(message)
        category = categorize_output.strip()
        return {"sentiment": sentiment, "category": category}
    else:
        return {"sentiment": sentiment}

# Test the sentiment analysis pipeline
messages = [
    "I love the new features of your product!",
    "I'm really disappointed with the customer service I received.",
    "Your product is okay, but I'm not impressed.",
    "I've been having issues with the product's performance."
]

for message in messages:
    output = analyze_sentiment(message)
    print(f"Message: {message}")
    print(f"Sentiment: {output['sentiment']}")
    if "category" in output:
        print(f"Category: {output['category']}")
    print()