import nltk
from flask import Flask, request, jsonify, render_template

# Download NLTK resources (if not already downloaded)
nltk.download('punkt')

app = Flask(__name__)

faq_data = {
    "What is your return policy?": "You can return items within 30 days of purchase.",
    "How can I track my order?": "You can track your order using the tracking link sent to your email.",
    "What payment methods do you accept?": "We accept credit cards, PayPal, bank transfers, and also Easypaisa.",
    "Do you ship internationally?": "Yes, we ship to most countries worldwide.",
    "How can I contact customer support?": "You can contact customer support via email at support@example.com.",
    "What is the estimated delivery time?": "The estimated delivery time is 5-7 working days for domestic orders and 10-15 working days for international orders.",
    "Can I change my order after it has been placed?": "Unfortunately, once an order is placed, we cannot make changes. Please contact customer support for assistance.",
    "Do you offer gift wrapping services?": "Yes, we offer gift wrapping services for an additional fee. You can select this option at checkout.",
    "What should I do if I receive a damaged item?": "If you receive a damaged item, please contact customer support within 48 hours of delivery for a replacement or refund.",
    "Do you have a loyalty program?": "Yes, we have a loyalty program that rewards you with points for every purchase, which can be redeemed for discounts on future orders.",
    "How do I unsubscribe from your newsletter?": "You can unsubscribe from our newsletter by clicking the 'unsubscribe' link at the bottom of any email.",
    "What if I forgot my password?": "If you forgot your password, you can reset it by clicking the 'Forgot Password?' link on the login page.",
    "Can I cancel my order?": "You can cancel your order within 24 hours of placing it. Please contact customer support for assistance.",
    "Do you offer discounts for bulk purchases?": "Yes, we offer discounts for bulk purchases. Please contact our sales team for more information.",
    "What are your working hours?": "Our working hours are Monday to Friday, 9 AM to 5 PM (local time).",
    "Where can I find your terms and conditions?": "You can find our terms and conditions on our website under the 'Terms of Service' section."
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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get('question')
    answer = find_best_answer(user_input)
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(port=8080, debug=True)