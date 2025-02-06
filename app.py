import nltk
from flask import Flask, request, jsonify

# Download NLTK resources (if not already downloaded)
nltk.download('punkt')

app = Flask(__name__)

faq_data = {
    "What is your return policy?": "You can return items within 30 days of purchase.",
    "How can I track my order?": "You can track your order using the tracking link sent to your email.",
    "What payment methods do you accept?": "We accept credit cards, PayPal, and bank transfers.",
    "Do you ship internationally?": "Yes, we ship to most countries worldwide.",
    "How can I contact customer support?": "You can contact customer support via email at support@example.com."
}

def find_best_answer(user_input):
    user_input_tokens = nltk.word_tokenize(user_input.lower())
    best_match = None
    best_score = 0

    for question in faq_data.keys():
        question_tokens = nltk.word_tokenize(question.lower())
        score = len(set(user_input_tokens) & set(question_tokens))  # Simple overlap score

        if score > best_score:
            best_score = score
            best_match = question

    return faq_data.get(best_match, "I'm sorry, I don't have an answer for that.")

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get('question')
    answer = find_best_answer(user_input)
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(port=8080, debug=True)