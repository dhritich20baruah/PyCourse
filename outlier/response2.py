import os
from dotenv import load_dotenv
from typing import Literal, Optional

from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

# Load environment variables (for OpenAI API key)
load_dotenv()

# --- 1. Define Pydantic Models for Structured Output ---

class SentimentAnalysis(BaseModel):
    """Pydantic model for sentiment analysis output."""
    sentiment: Literal["Positive", "Negative"] = Field(description="The overall sentiment of the message.")

class NegativeCategory(BaseModel):
    """Pydantic model for negative sentiment categorization."""
    category: Literal["Product Issue", "Service Complaint", "General Dissatisfaction"] = Field(
        description="The category of the negative sentiment."
    )

class FullAnalysis(BaseModel):
    """Pydantic model for the final combined output."""
    original_message: str
    sentiment: Literal["Positive", "Negative"]
    negative_category: Optional[Literal["Product Issue", "Service Complaint", "General Dissatisfaction"]] = None
    explanation: Optional[str] = Field(None, description="A brief explanation for the classification.")


# --- 2. Initialize LLM ---
# You can choose different models like "gpt-3.5-turbo", "gpt-4", etc.
# "gpt-3.5-turbo" is a good balance of cost and performance for this.
llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-0125") # Using a specific turbo model for consistency

# --- 3. Create Output Parsers ---
sentiment_parser = PydanticOutputParser(pydantic_object=SentimentAnalysis)
negative_category_parser = PydanticOutputParser(pydantic_object=NegativeCategory)
# For a more comprehensive final output, we can also parse the explanation
full_analysis_parser = PydanticOutputParser(pydantic_object=FullAnalysis)


# --- 4. Create Prompt Templates ---

# Prompt for general sentiment analysis
sentiment_prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an expert sentiment analyst. Your task is to analyze the emotional tone of the customer message "
            "and classify it as either 'Positive' or 'Negative'. Provide your output in JSON format, "
            "adhering to the following schema: \n{format_instructions}",
        ),
        ("human", "Analyze the sentiment of this customer message: \n\n'{customer_message}'"),
    ]
).partial(format_instructions=sentiment_parser.get_format_instructions())


# Prompt for categorizing negative sentiment
negative_category_prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an expert in categorizing customer complaints. The following message has already been identified as 'Negative'. "
            "Your task is to further categorize this negative message into one of three categories: "
            "'Product Issue', 'Service Complaint', or 'General Dissatisfaction'. "
            "Provide your output in JSON format, adhering to the following schema: \n{format_instructions}",
        ),
        (
            "human",
            "Categorize this negative customer message: \n\n'{customer_message}'\n\n"
            "Consider these definitions:\n"
            "- Product Issue: Problems related to the product itself (e.g., defects, features not working, quality).\n"
            "- Service Complaint: Issues related to customer service, support, delivery, or company policies.\n"
            "- General Dissatisfaction: Vague unhappiness, frustration not clearly tied to a specific product or service interaction."
        ),
    ]
).partial(format_instructions=negative_category_parser.get_format_instructions())


# --- Alternative: A single prompt for combined analysis (can be less reliable for complex logic) ---
# This is an option if you want to try and get everything in one call,
# but can sometimes lead to the LLM not following all instructions perfectly.
# Two-step is generally more robust for conditional logic.

combined_prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an AI assistant designed to analyze customer messages from social media. "
            "First, determine if the message sentiment is 'Positive' or 'Negative'. "
            "If the sentiment is 'Negative', further categorize it into one of: 'Product Issue', 'Service Complaint', or 'General Dissatisfaction'. "
            "If 'Positive', the category should be null or not present. "
            "Provide a brief explanation for your classification. "
            "Your output must be in JSON format, adhering to the following schema: \n{format_instructions}"
        ),
        ("human", "Analyze this customer message: \n\n'{customer_message}'"),
    ]
).partial(format_instructions=full_analysis_parser.get_format_instructions())


# --- 5. Create Chains ---
sentiment_chain = sentiment_prompt_template | llm | sentiment_parser
negative_category_chain = negative_category_prompt_template | llm | negative_category_parser
combined_analysis_chain = combined_prompt_template | llm | full_analysis_parser


# --- 6. Create the Pipeline Function ---

def analyze_customer_message_two_step(message: str) -> dict:
    """
    Analyzes a customer message for sentiment and, if negative, categorizes it.
    Uses a two-step approach for robustness.
    """
    print(f"\n--- Analyzing (Two-Step): '{message}' ---")
    try:
        # Step 1: Get sentiment
        sentiment_result = sentiment_chain.invoke({"customer_message": message})
        sentiment = sentiment_result.sentiment
        print(f"Initial Sentiment: {sentiment}")

        analysis_output = {
            "original_message": message,
            "sentiment": sentiment,
            "negative_category": None, # Default to None
            "explanation": f"The message was classified as {sentiment}." # Basic explanation
        }

        # Step 2: If negative, get category
        if sentiment == "Negative":
            category_result = negative_category_chain.invoke({"customer_message": message})
            analysis_output["negative_category"] = category_result.category
            analysis_output["explanation"] = f"The message is {sentiment}, categorized as '{category_result.category}'."
            print(f"Negative Category: {category_result.category}")

        return analysis_output

    except Exception as e:
        print(f"Error during two-step analysis: {e}")
        return {
            "original_message": message,
            "sentiment": "Error",
            "negative_category": None,
            "explanation": f"An error occurred during analysis: {str(e)}"
        }

def analyze_customer_message_one_step(message: str) -> dict:
    """
    Analyzes a customer message for sentiment and, if negative, categorizes it.
    Uses a single combined prompt.
    """
    print(f"\n--- Analyzing (One-Step): '{message}' ---")
    try:
        # Get combined analysis
        analysis_result: FullAnalysis = combined_analysis_chain.invoke({"customer_message": message})
        return analysis_result.model_dump() # Convert Pydantic model to dict

    except Exception as e:
        print(f"Error during one-step analysis: {e}")
        return {
            "original_message": message,
            "sentiment": "Error",
            "negative_category": None,
            "explanation": f"An error occurred during analysis: {str(e)}"
        }


# --- 7. Test the Pipeline ---
if __name__ == "__main__":
    if not os.getenv("OPENAI_API_KEY"):
        print("OPENAI_API_KEY not found. Please set it in your .env file.")
    else:
        customer_messages = [
            "I absolutely love your new product! It's changed my workflow completely for the better.",
            "The app keeps crashing every time I try to upload a photo. It's so frustrating!",
            "I waited on hold for 45 minutes just to be told they can't help me. Terrible service!",
            "I'm just not feeling this new update, things were better before.",
            "Thanks for the quick delivery! Everything arrived perfectly.",
            "The website is confusing and I can't find what I'm looking for. I'm so annoyed.",
            "My package arrived damaged and the contents were broken. This is unacceptable.",
            "Your customer support team was fantastic and resolved my issue quickly!",
            "I'm generally unhappy with the direction the company is taking.",
            "This is the best purchase I've made all year!",
            "The battery life on this device is a joke. It barely lasts a few hours."
        ]

        print("\n--- Testing Two-Step Pipeline ---")
        results_two_step = []
        for msg in customer_messages:
            result = analyze_customer_message_two_step(msg)
            results_two_step.append(result)
            print(f"Result: {result}")

        print("\n\n--- Testing One-Step Pipeline ---")
        results_one_step = []
        for msg in customer_messages:
            result = analyze_customer_message_one_step(msg)
            results_one_step.append(result)
            print(f"Result: {result}")

        print("\n\n--- Summary of Two-Step Results ---")
        for r in results_two_step:
            print(f"Message: \"{r['original_message']}\" -> Sentiment: {r['sentiment']}, Category: {r.get('negative_category', 'N/A')}")

        print("\n\n--- Summary of One-Step Results ---")
        for r in results_one_step:
            print(f"Message: \"{r['original_message']}\" -> Sentiment: {r['sentiment']}, Category: {r.get('negative_category', 'N/A')}, Explanation: {r.get('explanation')}")