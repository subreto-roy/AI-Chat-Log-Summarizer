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


total_messages = len(chat["User"]) + len(chat["AI"])


all_text = " ".join(chat["User"] + chat["AI"]).lower()
words = re.findall(r'\b\w+\b', all_text)


filtered_words = [word for word in words if word not in stop_words]
word_counts = Counter(filtered_words)
top_5 = word_counts.most_common(5)

top_words = [word for word, count in top_5]


if "python" in top_words:
    topic_summary = "The user asked mainly about Python and its uses."
elif "data" in top_words or "analysis" in top_words:
    topic_summary = "The conversation focused on data analysis and technical concepts."
else:
    topic_summary = "The conversation was general in nature."


print("\nSummary:")
print(f"- The conversation had {total_messages} exchanges.")
print(f"- {topic_summary}")
print(f"- Most common keywords: {', '.join(top_words)}.")

