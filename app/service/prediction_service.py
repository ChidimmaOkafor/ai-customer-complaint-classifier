import joblib
from pathlib import Path
import logging
logger = logging.getLogger(__name__)


BASE_DIR = Path(__file__).resolve().parent.parent.parent


CATEGORY_MODEL_PATH = BASE_DIR / "models" / "category_model.joblib"

CATEGORY_VECTORIZER_PATH = BASE_DIR / "models" / "category_vectorizer.joblib"

def load_model(model_path):
    try:
        if not model_path.exists():
            raise FileNotFoundError(f"Model file not found: {model_path}")

        model = joblib.load(model_path)
        logger.info("Model loaded successfully: %s", model_path.name)
        return model

    except Exception as e:
        logger.error("Model loading failed: %s - %s", model_path.name, e)
        raise


category_model = load_model(CATEGORY_MODEL_PATH)
category_vectorizer = load_model(CATEGORY_VECTORIZER_PATH)

def predict_category(text: str):
    if not text or not text.strip():
        raise ValueError("Message text cannot be empty.")
    X = category_vectorizer.transform([text])


    prediction = category_model.predict(X)[0]

    confidence = None
    if hasattr(category_model, "predict_proba"):
        confidence = float(max(category_model.predict_proba(X)[0]))

    return {
        "category": prediction,
        "confidence": confidence,
    }




def predict_message(text: str):
    try:
        category= predict_category(text)
        

        logger.info("Prediction completed successfully")

        return {
        "predicted_category": category["category"],
        "confidence": category["confidence"],
        
        }
    except Exception as e:
        logger.error("Prediction failed: %s", e)
        raise
if __name__ == "__main__":
    result = predict_message("I cannot access my account")
    print(result)