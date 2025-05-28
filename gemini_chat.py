import os
import google.generativeai as genai
from dotenv import load_dotenv


def initialize_gemini():
    """Initialize the Gemini API with the API key from environment variables."""
    # Load environment variables from .env file
    load_dotenv()
    
    # Get API key from environment
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("Error: GEMINI_API_KEY not found in environment variables.")
        print("Please add your Gemini API key to the .env file:")
        print("GEMINI_API_KEY=your_api_key_here")
        return None
    
    # Configure the API
    genai.configure(api_key=api_key)
    return True


def get_model_config():
    """Get model configuration from user input (optional feature)."""
    print("\n--- Model Configuration (Optional) ---")
    print("Press Enter to use default values or specify custom parameters:")
    
    # Temperature configuration
    temp_input = input("Temperature (0.0-2.0, default 0.7): ").strip()
    temperature = 0.7  # default
    if temp_input:
        try:
            temperature = float(temp_input)
            if not 0.0 <= temperature <= 2.0:
                print("Temperature out of range, using default 0.7")
                temperature = 0.7
        except ValueError:
            print("Invalid temperature, using default 0.7")
    
    # Top-p configuration
    top_p_input = input("Top-p (0.0-1.0, default 0.8): ").strip()
    top_p = 0.8  # default
    if top_p_input:
        try:
            top_p = float(top_p_input)
            if not 0.0 <= top_p <= 1.0:
                print("Top-p out of range, using default 0.8")
                top_p = 0.8
        except ValueError:
            print("Invalid top-p, using default 0.8")
    
    print(f"Using temperature: {temperature}, top-p: {top_p}")
    
    return {
        'temperature': temperature,
        'top_p': top_p,
        'max_output_tokens': 1000
    }


def main():
    """Main chat function implementing the interactive Gemini chatbot."""
    print("=== Context-Aware Gemini Chat ===")
    print("Type 'quit' or 'exit' to end the conversation\n")
    
    # Initialize Gemini API
    if not initialize_gemini():
        return
    
    # Get model configuration
    config = get_model_config()
    
    # Initialize the model with configuration
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=genai.types.GenerationConfig(
            temperature=config['temperature'],
            top_p=config['top_p'],
            max_output_tokens=config['max_output_tokens']
        )
    )
    
    # Start a chat session to maintain context
    chat = model.start_chat(history=[])
    
    print("\n--- Starting Conversation ---")
    turn_count = 1
    
    while True:
        # Get user input
        print(f"\nTurn {turn_count}:")
        user_input = input("You: ").strip()
        
        # Check for exit conditions
        if user_input.lower() in ['quit', 'exit', '']:
            print("Goodbye!")
            break
        
        try:
            # Send message to Gemini with full conversation context
            print("Gemini is thinking...")
            response = chat.send_message(user_input)
            
            # Print the response
            print(f"Gemini: {response.text}")
            
            # Store the final response for the last output requirement
            final_response = response.text
            
            turn_count += 1
            
        except Exception as e:
            print(f"Error communicating with Gemini: {e}")
            print("Please check your API key and internet connection.")
            break
    
    # Print the final response as required
    if 'final_response' in locals():
        print("\n--- Final Gemini Response ---")
        print(final_response)


if __name__ == "__main__":
    main()
