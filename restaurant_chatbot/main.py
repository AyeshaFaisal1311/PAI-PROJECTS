from flask import Flask, render_template, request
from nltk.chat.util import Chat, reflections

app=Flask(__name__)

pairs = [
    # Greetings
    [r"(?i)hello|hi|hey|salaam|assalam.*", 
     ["Hello! Welcome to Food Haven. How can I assist you today?"]],
    
    [r"(?i)how are you.*", 
     ["I'm just a chatbot, but I'm here to help! How can I assist you?"]],
    
    # Menu inquiries
    [r"(?i).*menu.*|.*dishes.*|.*food.*", 
     ['''We offer Biryani, Zinger Burger, Fries, Pepsi,
       Karahi, Handi, and more. Which item would you like to know more about?''']],
    
    # Specific dishes and prices
    [r"(?i).*biryani.*", 
     ["Biryani is Rs. 350."]],
    
    [r"(?i).*zinger.*|.*burger.*", 
     ["Zinger Burger is Rs. 450."]],
    
    [r"(?i).*fries.*", 
     ["Fries are Rs. 150."]],
    
    [r"(?i).*pepsi.*|.*drink.*", 
     ["Pepsi is Rs. 80."]],
    
    [r"(?i).*karahi.*", 
     ["Chicken Karahi is Rs. 1200 (full) and Rs. 650 (half)."]],
    
    [r"(?i).*handi.*", 
     ["Boneless Handi is Rs. 950 (half) and Rs. 1600 (full)."]],
    
    # Prices
    [r"(?i).*price.*|.*cost.*", 
     ["Please mention the dish you want the price for, like Biryani, Karahi, etc."]],
    
    # Opening hours
    [r"(?i).*timing.*|.*open.*|.*closing.*|.*hours.*", 
     ["We are open every day from 11 AM to 11 PM."]],
    
    # Location
    [r"(?i).*address.*|.*location.*|.*where.*", 
     ["Our restaurant is located at 123 Main Street, Lahore, Pakistan."]],
    
    # Delivery
    [r"(?i).*deliver.*|.*home delivery.*", 
     ["Yes, we offer home delivery within a 10 km radius. Please call 0300-1234567 to place an order."]],
    
    # Reservations
    [r"(?i).*reservation.*|.*book.*table.*", 
     ["You can reserve a table by calling us at 0300-1234567 or via our website."]],
    
    # Payment methods
    [r"(?i).*payment.*|.*card.*|.*cash.*", 
     ["We accept cash, credit/debit cards, and mobile wallets like Easypaisa and JazzCash."]],
    
    # Thank you
    [r"(?i).*thank.*|.*thanks.*", 
     ["You're welcome! Is there anything else you'd like to know?"]],
    
    # Goodbye
    [r"(?i).*bye.*|.*goodbye.*|.*exit.*", 
     ["Goodbye! Hope to serve you again soon."]],
    
    # Unknown fallback
    [r"(.*)", 
     ["Sorry, I didn't understand that. Please ask about our menu, prices, timings, or location."]]
]

chatbot = Chat(pairs, reflections)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_input = request.args.get('msg')
    response = chatbot.respond(user_input)
    return str(response)

if __name__ == "__main__":
    app.run(debug=True)
