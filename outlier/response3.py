import os
from langchain import PromptTemplate, LLMChain
from langchain.llms import OpenAI

# Set OpenAI API key
os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"

# Initialize GPT LLM
llm = OpenAI(temperature=0.7)

# Define sentiment analysis template
sentiment_template = PromptTemplate(
    input_variables=["message"],
    template="Analyze the sentiment of the following message: '{message}'. Is it Positive or Negative?"
)

# Define sentiment analysis chain
sentiment_chain = LLMChain(llm=llm, prompt=sentiment_template)

# Define negative sentiment categorization template
categorization_template = PromptTemplate(
    input_variables=["message"],
    template="The following message has a Negative sentiment: '{message}'. Categorize it as 'Product Issue', 'Service Complaint', or 'General Dissatisfaction'."
)

# Define negative sentiment categorization chain
categorization_chain = LLMChain(llm=llm, prompt=categorization_template)

def analyze_sentiment(message):
    """
    Analyze the sentiment of a customer message and categorize it if Negative.

    Args:
    message (str): Customer message from social media platforms.

    Returns:
    dict: A dictionary containing the sentiment classification and category (if Negative).
    """
    # Perform sentiment analysis
    sentiment_response = sentiment_chain.run(message=message)
    sentiment = sentiment_response.strip()

    # Initialize result dictionary
    result = {"sentiment": sentiment}

    # If sentiment is Negative, perform categorization
    if sentiment == "Negative":
        categorization_response = categorization_chain.run(message=message)
        category = categorization_response.strip()
        result["category"] = category

    return result

# Example usage
if __name__ == "__main__":
    messages = [
        "I love the new product! It's amazing!",
        "The service was terrible. I'm very dissatisfied.",
        "The product is defective. I need a replacement."
    ]

    for message in messages:
        result = analyze_sentiment(message)
        print(f"Message: {message}")
        print(f"Result: {result}")
        print("-" * 50)