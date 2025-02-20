import google.generativeai as genai

# Configure API Key
GOOGLE_API_KEY = "api key"
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize Model
model = genai.GenerativeModel('gemini-2.0-flash')

# Directions Text
directions = """To reach the Colosseum from Rome's Fiumicino Airport (FCO), your options are diverse.
Take the Leonardo Express train from FCO to Termini Station, then hop on metro line A towards Battistini and alight at Colosseo station.
Alternatively, hop on a direct bus, like the Terravision shuttle, from FCO to Termini, then walk a short distance to the Colosseum on Via dei Fori Imperiali.
If you prefer a taxi, simply hail one at the airport and ask to be taken to the Colosseum.
The taxi will likely take you through Via del Corso and Via dei Fori Imperiali.
A private transfer service offers a direct ride from FCO to the Colosseum, bypassing the hustle of public transport.
If you're feeling adventurous, consider taking the train from FCO to Ostiense station,
then walking through the charming Trastevere neighborhood, crossing Ponte Palatino to reach the Colosseum, passing by the Tiber River and Via della Lungara.
Remember to validate your tickets on the metro and buses, and be mindful of pickpockets, especially in crowded areas.
No matter which route you choose, you're sure to be awed by the grandeur of the Colosseum."""

# Prompt for extracting street names and transport forms
directions_prompt = f"""
From the given text, extract the following entities and return a list of them.
Entities to extract: street name, form of transport.
Text: {directions}
Return your answer as two lists:
Street = [street names]
Transport = [forms of transport]
"""

# Generate response
response = model.generate_content(directions_prompt)
print("Extracted Information:\n")
print(response.text)

# URL Extraction Example
url_text = """
Gemini API billing FAQs

This page provides answers to frequently asked questions about billing for the Gemini API. For pricing information, see the pricing page https://ai.google.dev/pricing.
For legal terms, see the terms of service https://ai.google.dev/gemini-api/terms#paid-services.

What am I billed for?
Gemini API pricing is based on total token count, with different prices for input tokens and output tokens. For pricing information, see the pricing page https://ai.google.dev/pricing.

Where can I view my quota?
You can view your quota and system limits in the Google Cloud console https://console.cloud.google.com/apis/api/generativelanguage.googleapis.com/quotas.

Is GetTokens billed?
Requests to the GetTokens API are not billed, and they don't count against inference quota."""

url_prompt = f"""
From the given text, extract the following entities and return a list of them.
Entities to extract: URLs.
Text: {url_text}
Do not duplicate entities.
Return your answer in a structured format:
"""

# Generate URL extraction response
url_response = model.generate_content(url_prompt)
print("\nExtracted URLs:\n")
print(url_response.text)
