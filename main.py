# Chatbot introduction
print("I'm Noel, a chatbot")
print("Feel free to ask me some questions or hold a conversation with me")

print("---------------------------------------------------------------------")
print()

# First question, Asks the user for a number 
def main_question(): 
    starter_input = input("Enter an even number for a topic: ")
    starter = int(starter_input)
    print("---------------------------------------------------------------------")
    print()
    if (starter % 2 == 0):
        topic_route()
    else:
        main_question()

# Main topics and subtopics		
topics = {
    "entertainment": ["soccer", "basketball", "football", "movies", "anime"],
    "school": ["tuition", "grades", "studying", "stem", "humanities", "admission"],
    "health": ["vaping", "smoking", "staying healthy", "habits"],
    "technology": ["artificial intelligence", "machine learning", "chatgpt", "deep learning", "natural language processing"],
    "food": ["asian", "italian", "mexican"],
	"holiday": ["christmas", "mother's day", "thanksgiving", "new years"],
	"games": ["roblox", "minecraft", "call of duty", "fortnite", "overwatch 2"]
}

# Responses for each topic and subtopic
sub_topic_responses = {
    "entertainment": {
        "soccer": ["I love soccer! Who's your favorite team?", "I'm a big soccer fan too. Who do you root for?", "Soccer is such an exciting sport. Who's your favorite player?"],
        "basketball": ["Basketball is a great sport. Do you have a favorite team?", "I'm a big basketball fan. Who's your favorite player?", "I love watching basketball games. Who's your go-to team?"],
        "football": ["Football season is the best season. Who's your favorite team?", "I'm a big football fan. Who do you root for?", "Who's your favorite football player?"],
        "movies": ["What's your favorite movie?", "I love going to the movies. What's your favorite genre?", "Do you have a favorite actor or actress?"],
        "anime": ["Do you watch a lot of anime?", "What's your favorite anime?", "I love discussing anime with other fans. Who's your favorite character?"]
    },
    "school": {
        "tuition": ["What's your major?", "How do you feel about the cost of tuition?", "Have you thought about scholarships or financial aid?"],
        "grades": ["How do you feel about your grades?", "Do you have any strategies for studying and improving your grades?", "What's your favorite subject?"],
        "studying": ["How do you like to study?", "Do you have any study tips?", "What's your favorite way to relax after a long study session?"],
        "stem": ["What's your favorite stem subject?", "Do you have any career aspirations in stem?", "What do you like about stem subjects?"],
        "humanities": ["What's your favorite humanities subject?", "Do you have any career aspirations in the humanities?", "What do you like about humanities subjects?"],
        "admission": ["Are you in college?", "What's your dream school?", "How do you feel about the admissions process?"]
    },
    "health": {
        "vaping": ["Do you vape?", "What do you like about vaping?", "Have you considered the health risks of vaping?"],
        "smoking": ["Do you smoke?", "What do you like about smoking?", "Have you considered the health risks of smoking?"],
        "staying healthy": ["Do you have any healthy habits?", "What's your favorite way to stay active?", "Do you have any healthy recipes you enjoy?"],
        "habits": ["What are your daily habits?", "Do you have any healthy habits you'd like to improve?", "What are some unhealthy habits you'd like to break?"]
    },
    "technology": {
        "artificial intelligence": ["What do you think about artificial intelligence?", "Do you think artificial intelligence will replace human jobs?", "What's your favorite application of artificial intelligence?"],
        "machine learning": ["What do you think about machine learning?", "Do you think machine learning will replace human jobs?", "What's your favorite application of machine learning?"],
        "chatgpt": ["What do you think about chatgpt?", "Do you think chatgpt will replace human jobs?", "What's your favorite application of chatgpt?"],
        "deep learning":["How interesting do you find deep learning?", "Would you want to learn the pre-requisities for deep learning?", "Whats your favorite application of deep learning?"]},
	"food": {
		"asian": ["Which asian countries food do you like the most?", "What's your favorite dish?"],
		"italian": ["Do you have a favorite pasta?", "Spaghetti or Pizza?", "What's your favorite topping on pizza?", "What's your favorite pasta sauce"], 
		"mexican": ["Do you have a favorite dish?", "What's your favorite mexican dressing/sauce?"],
		
	}, 
	"holiday": {
		"christmas": ["Is christmas your favorite holiday?", "Do you like giving or receiving gifts?", "What's the best gift that you've given to someone?", "Why do you celebrate Christmas?"],
		"mother's day": ["What did you do to surprise your mom?", "What's your favorite memory with your mom"],
		"thanksgiving": ["What are you thankful for?", "Rate thanksgiving on a scale from 1-10", "Are you excited to see family?"],
		"new years": ["Where did you ring in the new year", "Rate the previous year on a scale from 1-10", "What are your new year resolutions?"],
	},
	"games": {
		"roblox": ["What's your favorite game to play", "Who do you play roblox with? ", "Gemerally, what genre of games do you play"],
		"minecraft": ["What is your longest survival world?", "What is the best thing that you've built in minecraft", "Would you play solo or with friends", "What's your favorite mini-gane"],
		"call of duty": ["Which version was your favorite?", "What's your favorite gun", "What's  your favorite game mode"],
		"fornite": ["Which YouTuber do you like to watch?", "What's your favorite game-mode", "What's the rarest skin that you have?"],
		"overwatch 2": ["Did you play Overwatch 1", "Which character do you main?", "Do you mainly play DPS, Tank, or Support?"],
		
	}
}		
		
def topic_route():
    first_topic = input("What main topic do you want to talk about? " + str(list(topics.keys())))
    if first_topic in topics:
        sub_topic_route(first_topic)
    else: 
        print("Sorry, I don't understand yout input. Please choose a topic form the list")
        topic_route()

def sub_topic_route(main_topic):
    print("Here are the subtopics for " + main_topic + ": " + str(topics[main_topic]))
    sub_topic = input("Which subtopic would you like to discuss? ")
    if sub_topic in topics[main_topic]:
        print("Let's talk about " + sub_topic + "!")
    else:
        print("Sorry, I don't understand your input. Please choose a subtopic from the list.")
        sub_topic_route(main_topic)

# Main loop that controls the chatbot


want_to_exit = ''
while want_to_exit != "Y": 
    main_question()
    want_to_exit = input("Do you want to exit the chatbot? (Y/N)")
if want_to_exit == "Y":
	print("It was nice talking to you! Have a great day! Bye!")
else:
	main_question()
	

