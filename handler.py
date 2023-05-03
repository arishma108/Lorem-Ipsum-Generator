import random
from flask import jsonify

def handle(event, context):
    # Get the input value of num_paragraphs
    num_paragraphs = int(event.get("num_paragraphs", 1))
    
    # Define the list of Lorem Ipsum words and phrases
    lorem_ipsum = [
        "Lorem ipsum dolor sit amet,",
        "consectetur adipiscing elit.",
        "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "Ut enim ad minim veniam,",
        "quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
        "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.",
        "Excepteur sint occaecat cupidatat non proident,",
        "sunt in culpa qui officia deserunt mollit anim id est laborum."
    ]
    
    # Generate the specified number of paragraphs of Lorem Ipsum text
    lorem_ipsum_text = "\n\n".join([" ".join(random.sample(lorem_ipsum, random.randint(5, 15))) for _ in range(num_paragraphs)])
    
    # Return the generated text as a JSON response
    return jsonify({"text": lorem_ipsum_text})
