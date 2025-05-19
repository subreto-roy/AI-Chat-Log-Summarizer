with open("chat.txt", "r") as file:
    lines = file.readlines()

chat = {"User": [], "AI": []}

for line in lines:
    line = line.strip()
    if line.startswith("User:"):
        chat["User"].append(line.replace("User:", "").strip())
    elif line.startswith("AI:"):
        chat["AI"].append(line.replace("AI:", "").strip())
        
print("User Messages:")
for msg in chat["User"]:
    print("-", msg)

print("\nAI Messages:")
for msg in chat["AI"]:
    print("-", msg)
