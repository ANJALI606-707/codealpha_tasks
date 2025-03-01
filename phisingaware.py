import random

def phishing_awareness():
    print("\n🎣 PHISHING AWARENESS TRAINING 🎣\n")
    
    print("💡 Quick Tips to Avoid Phishing Attacks:\n")
    tips = [
        "✔️ Always check the sender’s email address before clicking links.",
        "✔️ Never download attachments from unknown or unexpected emails.",
        "✔️ Be cautious of messages creating a sense of urgency (e.g., 'Act Now!').",
        "✔️ Banks and government agencies never ask for sensitive data via email.",
        "✔️ Use Multi-Factor Authentication (MFA) for extra security."
    ]
    
    for tip in tips:
        print(tip)

    print("\n🚨 QUIZ: Can you spot the phishing attempts?\n")

    questions = [
        {
            "question": '''You receive an email from "security@amazon-secure.com" stating:
    "Your account has been locked due to suspicious activity. Click here to restore access: 
    http://amazon-loginverify.com"
    What should you do?''',
            "options": [
                "Click the link to verify your Amazon account.",
                "Ignore the email or report it as phishing.",
                "Reply to the email asking for details."
            ],
            "correct_answer": "Ignore the email or report it as phishing."
        },
        {
            "question": '''Your IT department sends an email saying your password has expired. 
    The email asks you to click a link to reset your password. How do you respond?''',
            "options": [
                "Click the link to reset your password immediately.",
                "Check if the email sender is legitimate and visit the official IT website instead.",
                "Ignore it. Passwords never expire."
            ],
            "correct_answer": "Check if the email sender is legitimate and visit the official IT website instead."
        },
        {
            "question": '''A friend sends you a message on social media saying:
    "Hey! Is this you in the video? 😂" with a strange link. What do you do?''',
            "options": [
                "Click the link to check the video.",
                "Reply and ask your friend what the video is about.",
                "Ignore the message or confirm with your friend through another method."
            ],
            "correct_answer": "Ignore the message or confirm with your friend through another method."
        },
        {
            "question": '''A website pop-up warns: 
    "Your device has been infected! Call this number to fix it now!" What should you do?''',
            "options": [
                "Call the number immediately.",
                "Close the pop-up and run an antivirus scan.",
                "Follow the instructions in the pop-up."
            ],
            "correct_answer": "Close the pop-up and run an antivirus scan."
        },
        {
            "question": '''You receive an SMS saying:
    "Your bank account is temporarily locked. Visit http://secure-banklogin.com to unlock it now." What do you do?''',
            "options": [
                "Click the link and enter your banking details.",
                "Call your bank using their official customer support number.",
                "Reply to the SMS and ask for more details."
            ],
            "correct_answer": "Call your bank using their official customer support number."
        },
        {
            "question": '''You get a job offer via email from a company you never applied to. 
    They ask you to send your personal information to receive an offer letter. What should you do?''',
            "options": [
                "Send your details, it's a great opportunity!",
                "Ignore the email or verify the company through official channels.",
                "Reply to ask more about the job details."
            ],
            "correct_answer": "Ignore the email or verify the company through official channels."
        }
    ]

    score = 0

    for i, q in enumerate(questions, 1):
        print(f"\nQ{i}: {q['question']}\n")
        
        shuffled_options = q["options"]
        random.shuffle(shuffled_options)  # Randomize answer order

        option_mapping = {}
        for j, option in enumerate(shuffled_options, 1):
            option_mapping[str(j)] = option
            print(f"{j}. {option}")

        answer = input("\nEnter your choice (1/2/3): ").strip()

        if answer in option_mapping and option_mapping[answer] == q["correct_answer"]:
            print("\n✅ Correct!")
            score += 1
        else:
            print("\n❌ Incorrect!")

    print(f"\n🎯 Your final score: {score}/{len(questions)}")
    
    if score == len(questions):
        print("🏆 Excellent! You're a phishing awareness expert!")
    elif score >= len(questions) // 2:
        print("👍 Good job! Stay cautious and keep learning.")
    else:
        print("⚠️ You need to be more careful. Phishing attacks are dangerous!")

    print("\n🔹 Stay cautious and stay safe online! 🔹\n")

# Run the phishing awareness training
if __name__ == "__main__":
    phishing_awareness()
