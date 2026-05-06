text = input("Enter text: ")

# Mood detection
if "happy" in text.lower() or "good" in text.lower():
    mood = "Positive 🙂"
elif "sad" in text.lower() or "bad" in text.lower():
    mood = "Negative 😢"
else:
    mood = "Neutral 😐"

# Message type
if "?" in text:
    message_type = "Question"
else:
    message_type = "Statement"

# Simple response system
if mood == "Positive 🙂":
    advice = "Keep it up!"
elif mood == "Negative 😢":
    advice = "Stay strong, things will get better."
else:
    advice = "Noted."

print("\n--- AI RESPONSE ---")
print("Mood:", mood)
print("Type:", message_type)
print("Advice:", advice)
