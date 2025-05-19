import re
from collections import Counter


stop_words = {
    "the", "is", "and", "a", "an", "to", "of", "in", "for", "on", "you", "can", "about", "it", "its"
}

with open("chat.txt", "r") as file:
    lines = file.readlines()

chat = {"User": [], "AI": []}

for line in lines:
    line = line.strip()
    if line.startswith("User:"):
        chat["User"].append(line.replace("User:", "").strip())
    elif line.startswith("AI:"):
        chat["AI"].append(line.replace("AI:", "").strip())


# total_messages = len(chat["User"]) + len(chat["AI"])
# user_messages = len(chat["User"])
# ai_messages = len(chat["AI"])   

# print("\n--- Message Count Summary ---")
# print(f"Total Messages: {total_messages}")
# print(f"User Messages: {user_messages}")
# print(f"AI Messages: {ai_messages}")


all_text = " ".join(chat["User"] + chat["AI"]).lower()  
words = re.findall(r'\b\w+\b', all_text)  


filtered_words = [word for word in words if word not in stop_words]
word_counts = Counter(filtered_words)
top_5 = word_counts.most_common(5)

top_words = [word for word, count in top_5]
print("\nMost common words:", ", ".join(top_words))
