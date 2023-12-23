import requests

def emotion_detector(text_to_analyze):
    # Watson NLP URL and headers
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Input JSON format
    input_json = {"raw_document": {"text": text_to_analyze}}

    # Make a POST request to Watson NLP
    response = requests.post(url, headers=headers, json=input_json)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Return the 'text' attribute of the response
        return response.json()['text']
    else:
        # Return an error message if the request fails
        return f"Error: {response.status_code}"

# Test the emotion_detector function with a sample text
result = emotion_detector("I love this new technology.")
print(result)
