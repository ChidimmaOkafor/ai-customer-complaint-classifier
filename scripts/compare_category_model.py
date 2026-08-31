import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report

#Load dataset 
df=pd.read_csv("../data/cleaned_customer_complaints_dataset.csv")
df["message"]

X = df["message"]
y = df["category"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify = y)
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

model = LogisticRegression(random_state=42)
model.fit(X_train_tfidf, y_train)
y_pred = model.predict(X_test_tfidf)
accuracy = accuracy_score(y_test, y_pred)
print("Logistic Regrssion")
print("Logistic Regression Accuracy:", accuracy)
print(classification_report(y_test, y_pred))

nb_model = MultinomialNB()
nb_model.fit(X_train_tfidf, y_train)
y_pred_nb = nb_model.predict(X_test_tfidf)
accuracy_nb = accuracy_score(y_test, y_pred_nb)
print("Naive Bayes")
print("Naive Bayes Accuracy:", accuracy_nb)
print(classification_report(y_test, y_pred_nb))

probabilites = model.predict_proba(X_test_tfidf)
print(probabilites[0])

confindence = max(probabilites[0])
print("confindence:", confindence)



joblib.dump(model,"../models/category_model.joblib")
joblib.dump(vectorizer,"../models/category_vectorizer.joblib")

print("\ncategory model saved successfully!")