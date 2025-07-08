import os
from typing import Dict, List, Optional, Tuple
from enum import Enum
from pydantic import BaseModel, Field
from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from langchain.schema import BaseOutputParser
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain.callbacks import StreamingStdOutCallbackHandler
import json

# Define Enums for sentiment and categories
class Sentiment(str, Enum):
    POSITIVE = "Positive"
    NEGATIVE = "Negative"

class NegativeCategory(str, Enum):
    PRODUCT_ISSUE = "Product Issue"
    SERVICE_COMPLAINT = "Service Complaint"
    GENERAL_DISSATISFACTION = "General Dissatisfaction"

# Pydantic models for structured output
class SentimentAnalysisResult(BaseModel):
    sentiment: Sentiment = Field(description="The overall sentiment of the message")
    confidence: float = Field(description="Confidence score between 0 and 1")
    explanation: str = Field(description="Brief explanation of the sentiment classification")
    negative_category: Optional[NegativeCategory] = Field(
        default=None,
        description="Category of negative sentiment if applicable"
    )
    category_explanation: Optional[str] = Field(
        default=None,
        description="Explanation for the negative category classification"
    )

class SentimentAnalysisPipeline:
    def __init__(self, api_key: Optional[str] = None, model_name: str = "gpt-3.5-turbo"):
        """
        Initialize the sentiment analysis pipeline.
        
        Args:
            api_key: OpenAI API key (if not provided, will look for OPENAI_API_KEY env var)
            model_name: Name of the OpenAI model to use
        """
        if api_key:
            os.environ["OPENAI_API_KEY"] = api_key
            
        self.llm = ChatOpenAI(
            model_name=model_name,
            temperature=0.1,  # Low temperature for consistent classification
            max_tokens=500
        )
        
        # Create output parser
        self.parser = PydanticOutputParser(pydantic_object=SentimentAnalysisResult)
        
        # Create prompts
        self.sentiment_prompt = self._create_sentiment_prompt()
        self.categorization_prompt = self._create_categorization_prompt()
        
        # Create chains
        self.sentiment_chain = LLMChain(
            llm=self.llm,
            prompt=self.sentiment_prompt,
            output_parser=self.parser
        )
    
    def _create_sentiment_prompt(self) -> PromptTemplate:
        """Create the prompt template for sentiment analysis."""
        template = """You are an expert sentiment analysis system for customer messages from social media platforms.

Analyze the following customer message and determine:
1. The overall sentiment (Positive or Negative)
2. A confidence score (0-1)
3. A brief explanation for your classification
4. If negative, categorize it as one of: 'Product Issue', 'Service Complaint', or 'General Dissatisfaction'
5. If negative, provide an explanation for the category

Customer Message: {message}

{format_instructions}

Important guidelines:
- 'Product Issue': Problems with product quality, features, defects, or functionality
- 'Service Complaint': Issues with customer service, support, delivery, or company processes
- 'General Dissatisfaction': General unhappiness, vague complaints, or issues not clearly fitting other categories
"""
        
        return PromptTemplate(
            input_variables=["message"],
            template=template,
            partial_variables={"format_instructions": self.parser.get_format_instructions()}
        )
    
    def _create_categorization_prompt(self) -> PromptTemplate:
        """Create a focused prompt for negative sentiment categorization."""
        template = """Given this negative customer message, categorize it into one of these categories:
1. 'Product Issue': Problems with product quality, features, defects, or functionality
2. 'Service Complaint': Issues with customer service, support, delivery, or company processes  
3. 'General Dissatisfaction': General unhappiness or vague complaints

Message: {message}

Provide the category and a brief explanation."""
        
        return PromptTemplate(
            input_variables=["message"],
            template=template
        )
    
    def analyze_sentiment(self, message: str) -> SentimentAnalysisResult:
        """
        Analyze the sentiment of a single message.
        
        Args:
            message: The customer message to analyze
            
        Returns:
            SentimentAnalysisResult object containing the analysis
        """
        try:
            result = self.sentiment_chain.run(message=message)
            return result
        except Exception as e:
            print(f"Error analyzing sentiment: {e}")
            # Return a default result in case of error
            return SentimentAnalysisResult(
                sentiment=Sentiment.NEGATIVE,
                confidence=0.5,
                explanation="Error in analysis",
                negative_category=NegativeCategory.GENERAL_DISSATISFACTION,
                category_explanation="Could not properly analyze the message"
            )
    
    def analyze_batch(self, messages: List[str]) -> List[SentimentAnalysisResult]:
        """
        Analyze sentiment for a batch of messages.
        
        Args:
            messages: List of customer messages to analyze
            
        Returns:
            List of SentimentAnalysisResult objects
        """
        results = []
        for message in messages:
            result = self.analyze_sentiment(message)
            results.append(result)
        return results
    
    def get_summary_statistics(self, results: List[SentimentAnalysisResult]) -> Dict:
        """
        Generate summary statistics from a list of results.
        
        Args:
            results: List of SentimentAnalysisResult objects
            
        Returns:
            Dictionary containing summary statistics
        """
        total = len(results)
        positive_count = sum(1 for r in results if r.sentiment == Sentiment.POSITIVE)
        negative_count = total - positive_count
        
        negative_categories = {
            NegativeCategory.PRODUCT_ISSUE: 0,
            NegativeCategory.SERVICE_COMPLAINT: 0,
            NegativeCategory.GENERAL_DISSATISFACTION: 0
        }
        
        for result in results:
            if result.sentiment == Sentiment.NEGATIVE and result.negative_category:
                negative_categories[result.negative_category] += 1
        
        avg_confidence = sum(r.confidence for r in results) / total if total > 0 else 0
        
        return {
            "total_messages": total,
            "positive_count": positive_count,
            "negative_count": negative_count,
            "positive_percentage": (positive_count / total * 100) if total > 0 else 0,
            "negative_percentage": (negative_count / total * 100) if total > 0 else 0,
            "average_confidence": avg_confidence,
            "negative_categories": {
                "product_issues": negative_categories[NegativeCategory.PRODUCT_ISSUE],
                "service_complaints": negative_categories[NegativeCategory.SERVICE_COMPLAINT],
                "general_dissatisfaction": negative_categories[NegativeCategory.GENERAL_DISSATISFACTION]
            }
        }

# Example usage and demonstration
def main():
    # Initialize the pipeline (make sure to set your OpenAI API key)
    # os.environ["OPENAI_API_KEY"] = "your-api-key-here"
    pipeline = SentimentAnalysisPipeline()
    
    # Sample customer messages
    sample_messages = [
        "I absolutely love this product! It exceeded all my expectations and the customer service was fantastic.",
        "The product arrived broken and customer support hasn't responded to my emails for a week. Very disappointed.",
        "Not sure why everyone likes this so much. It's okay, I guess, but nothing special.",
        "This is the best purchase I've made all year! Highly recommend to everyone!",
        "The app keeps crashing every time I try to use it. This is completely unusable.",
        "Your delivery service is terrible. My package was delayed by two weeks with no explanation.",
        "Great quality and fast shipping. Will definitely order again!",
        "I'm not happy with my recent experience. Everything just feels off.",
        "The product features don't work as advertised. This is false advertising!",
        "Customer service was rude and unhelpful when I called about my issue."
    ]
    
    print("Analyzing customer messages...\n")
    print("-" * 80)
    
    results = []
    for i, message in enumerate(sample_messages, 1):
        print(f"\nMessage {i}: {message[:100]}...")
        result = pipeline.analyze_sentiment(message)
        results.append(result)
        
        print(f"Sentiment: {result.sentiment.value}")
        print(f"Confidence: {result.confidence:.2f}")
        print(f"Explanation: {result.explanation}")
        
        if result.sentiment == Sentiment.NEGATIVE:
            print(f"Category: {result.negative_category.value if result.negative_category else 'N/A'}")
            print(f"Category Explanation: {result.category_explanation}")
        
        print("-" * 80)
    
    # Print summary statistics
    print("\n\nSUMMARY STATISTICS")
    print("=" * 80)
    stats = pipeline.get_summary_statistics(results)
    print(f"Total Messages Analyzed: {stats['total_messages']}")
    print(f"Positive: {stats['positive_count']} ({stats['positive_percentage']:.1f}%)")
    print(f"Negative: {stats['negative_count']} ({stats['negative_percentage']:.1f}%)")
    print(f"Average Confidence: {stats['average_confidence']:.2f}")
    print("\nNegative Categories Breakdown:")
    print(f"  - Product Issues: {stats['negative_categories']['product_issues']}")
    print(f"  - Service Complaints: {stats['negative_categories']['service_complaints']}")
    print(f"  - General Dissatisfaction: {stats['negative_categories']['general_dissatisfaction']}")

# Additional utility functions
def export_results_to_json(results: List[SentimentAnalysisResult], filename: str):
    """Export results to a JSON file."""
    data = []
    for result in results:
        data.append({
            "sentiment": result.sentiment.value,
            "confidence": result.confidence,
            "explanation": result.explanation,
            "negative_category": result.negative_category.value if result.negative_category else None,
            "category_explanation": result.category_explanation
        })
    
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

def filter_negative_messages(results: List[SentimentAnalysisResult], 
                           messages: List[str], 
                           category: Optional[NegativeCategory] = None) -> List[Tuple[str, SentimentAnalysisResult]]:
    """Filter messages by negative sentiment and optionally by category."""
    filtered = []
    for msg, result in zip(messages, results):
        if result.sentiment == Sentiment.NEGATIVE:
            if category is None or result.negative_category == category:
                filtered.append((msg, result))
    return filtered

if __name__ == "__main__":
    main()

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = "your-api-key-here"

# Initialize the pipeline
pipeline = SentimentAnalysisPipeline()

# Analyze a single message
message = "The product quality is terrible and it broke after one day of use."
result = pipeline.analyze_sentiment(message)
print(f"Sentiment: {result.sentiment}")
print(f"Category: {result.negative_category}")

# Analyze multiple messages
messages = ["Great service!", "Product doesn't work", "Very disappointed"]
results = pipeline.analyze_batch(messages)

# Get statistics
stats = pipeline.get_summary_statistics(results)
print(f"Negative messages: {stats['negative_percentage']}%")