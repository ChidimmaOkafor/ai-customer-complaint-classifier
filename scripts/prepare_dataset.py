import pandas as pd 
import re

#read daataset
df = pd.read_csv("../data/customer_complaints_dataset.csv")
print(df.columns.tolist())
df.columns = df.columns.str.lower
#Check missing values 
print(df.isnull().sum())

#Remove rows with missing values in important columns
df = df.dropna(subset=["id", "message", "category"])

#Function to clean text 

def clean_text(text):
    text = text.lower()
    text = re.sub(r"\s+"," ", text)
    text = text.strip()
    return text

#Clean text columns 
df["message"] = df["message"].apply(clean_text)

#Standardize label
df["category"] = df["category"].str.strip().str.lower()

#check label
print(df["category"].value_counts())

#Valid labels
valid_category = {
    "Payment/Transaction"
    "Account Access"
    "Technical Issue"
    "Customer Service"
    "General Enquiry"
}

print(df["category"].unique())

#savw cleaned dataset 
df.to_csv("../data/customer_complaints_dataset.csv", index=False)

print("Dataset cleaned successfully")