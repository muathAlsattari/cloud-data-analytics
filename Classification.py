from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

texts = ["machine learning research", "sports news update"]
labels = ["technology", "sports"]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

clf = MultinomialNB()
clf.fit(X, labels)

new_text = "AI breakthrough"
pred = clf.predict(vectorizer.transform([new_text]))
print(pred[0])  
