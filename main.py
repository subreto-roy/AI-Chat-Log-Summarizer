from sklearn.feature_extraction.text import TfidfVectorizer
from collections import defaultdict


stop_words = [
    "the", "is", "and", "a", "an", "to", "of", "in", "for", "on", 
    "you", "can", "about", "it", "its", "i", "we", "our", "me", "us"
]
topic_keywords = {
            'python programming': ['python', 'code', 'programming', 'script', 'syntax'],
            'machine learning': ['machine learning', 'ml', 'ai', 'model', 'training'],
            'deep learning': ['deep learning', 'neural network', 'cnn', 'rnn', 'lstm'],
            'web development': ['web', 'html', 'css', 'javascript', 'frontend', 'backend'],
            'data analysis': ['data', 'analysis', 'statistics', 'pandas', 'numpy'],
            'cloud computing': ['cloud', 'aws', 'azure', 'gcp', 'deployment'],
            'cybersecurity': ['security', 'encryption', 'malware', 'hacking', 'firewall'],
            'mobile development': ['android', 'ios', 'flutter', 'swift', 'react native'],
            'devops': ['devops', 'docker', 'kubernetes', 'ci/cd', 'pipeline'],
            'software testing': ['testing', 'qa', 'unittest', 'pytest', 'bug'],
            'natural language processing': ['nlp', 'text', 'language model', 'tokenization'],
            'computer vision': ['opencv', 'image', 'detection', 'recognition'],
            'education': ['school', 'teacher', 'student', 'class', 'homework', 'exam'],
            'study tips': ['study', 'revision', 'concentration', 'learning', 'memorize'],
            'career guidance': ['career', 'job', 'resume', 'cv', 'interview', 'internship'],
            'medical': ['doctor', 'medicine', 'treatment', 'disease', 'hospital', 'symptoms'],
            'mental health': ['stress', 'anxiety', 'therapy', 'counseling', 'depression'],
            'fitness': ['exercise', 'workout', 'gym', 'diet', 'yoga', 'nutrition'],
            'travel': ['travel', 'trip', 'flight', 'hotel', 'tourism', 'vacation'],
            'food and cooking': ['recipe', 'cook', 'kitchen', 'meal', 'restaurant', 'cuisine'],
            'sports': ['football', 'cricket', 'tennis', 'match', 'score', 'tournament'],
            'relationships': ['relationship', 'friend', 'love', 'partner', 'marriage'],
            'business': ['startup', 'business', 'entrepreneur', 'pitch', 'investment'],
            'finance': ['money', 'bank', 'loan', 'investment', 'tax', 'budget', 'savings'],
            'marketing': ['marketing', 'advertising', 'brand', 'campaign', 'seo', 'social media'],
            'general information': ['what is', 'explain', 'define', 'meaning', 'overview'],
            'technical help': ['how to', 'help', 'error', 'issue', 'problem', 'fix', 'solution'],
            'entertainment': ['movie', 'music', 'song', 'tv', 'series', 'actor', 'celebrity'],
            'news and events': ['news', 'event', 'update', 'breaking', 'headline', 'report'],
            'legal': ['law', 'legal', 'contract', 'court', 'agreement', 'rights'],
            'government services': ['passport', 'visa', 'id', 'registration', 'license', 'tax'],
            'student life': ['student', 'exam', 'assignment', 'homework', 'study', 'class', 'semester'],
            'education system': ['education', 'school', 'university', 'college', 'curriculum', 'grades'],
            'career guidance': ['career', 'job', 'internship', 'resume', 'cv', 'interview', 'future'],
            'teaching': ['teacher', 'classroom', 'lesson', 'teach', 'instruction', 'syllabus', 'grade'],
            'online education': ['online class', 'zoom', 'virtual learning', 'elearning', 'remote learning'],
            'content writing': ['writing', 'blog', 'content', 'article', 'editor', 'grammar', 'publish'],
            'creative writing': ['story', 'poem', 'novel', 'character', 'plot', 'dialogue'],
            'technical writing': ['documentation', 'manual', 'guide', 'technical writing', 'specifications'],
            'business management': ['business', 'management', 'operations', 'strategy', 'growth', 'scaling'],
            'company operations': ['company', 'startup', 'organization', 'employees', 'workflow'],
            'product development': ['product', 'design', 'features', 'feedback', 'launch', 'testing'],
            'entrepreneurship': ['founder', 'entrepreneur', 'startup', 'venture', 'pitch', 'innovation'],
            'online marketing': ['seo', 'social media', 'facebook ads', 'content marketing', 'influencer'],
            'traditional marketing': ['advertising', 'print', 'tv', 'flyers', 'billboard'],
            'brand strategy': ['branding', 'logo', 'identity', 'brand awareness', 'campaign'],
            'agriculture': ['farming', 'crop', 'soil', 'harvest', 'irrigation', 'seeds', 'organic'],
            'agribusiness': ['agriculture business', 'market', 'supply chain', 'fertilizer', 'yield'],
            'scientific research': ['research', 'study', 'experiment', 'hypothesis', 'data collection'],
            'academic research': ['journal', 'publication', 'citation', 'peer review', 'thesis'],
            'innovation': ['innovation', 'technology', 'prototype', 'patent', 'development'],
            'financial planning': ['budget', 'expense', 'income', 'investment', 'loan', 'saving'],
            'business analytics': ['analysis', 'dashboard', 'metrics', 'report', 'kpi'],
            'technical help': ['how to', 'fix', 'error', 'issue', 'problem', 'support'],
            'general information': ['what is', 'explain', 'define', 'meaning', 'overview'],
            'health & wellness': ['stress', 'health', 'diet', 'exercise', 'mental health'],
            'news & updates': ['news', 'update', 'event', 'announcement', 'trend']
}

#File load
with open("chat.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

chat = {"User": [], "AI": []}
for line in lines:
    line = line.strip()
    if line.startswith("User:"):
        chat["User"].append(line.replace("User:", "").strip())
    elif line.startswith("AI:"):
        chat["AI"].append(line.replace("AI:", "").strip())

documents = chat["User"] + chat["AI"]
total_messages = len(documents)

# TF-IDF
vectorizer = TfidfVectorizer(stop_words=stop_words)
tfidf_matrix = vectorizer.fit_transform(documents)
scores = tfidf_matrix.sum(axis=0).A1
words = vectorizer.get_feature_names_out()
word_score_pairs = list(zip(words, scores))
sorted_keywords = sorted(word_score_pairs, key=lambda x: x[1], reverse=True)
top_keywords = [word.capitalize() for word, score in sorted_keywords[:5]]

# Topic select
matched_topics = defaultdict(int)
for topic, keywords in topic_keywords.items():
    for word in top_keywords:
        if word.lower() in keywords:
            matched_topics[topic] += 1

top_topic = sorted(matched_topics.items(), key=lambda x: x[1], reverse=True)
if top_topic:
    summary_line = f"The user asked mainly about {top_topic[0][0]}."
else:
    summary_line = "The conversation was general in nature."


print("Summary:")
print(f"- The conversation had {total_messages} exchanges.")
print(f"- {summary_line}")
print(f"- Most common keywords: {', '.join(top_keywords)}")
