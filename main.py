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
user_messages = len(chat["User"])
ai_messages = len(chat["AI"])

print("\n--- Message Count Summary ---")
print(f"Total Messages: {total_messages}")
print(f"User Messages: {user_messages}")
print(f"AI Messages: {ai_messages}")
