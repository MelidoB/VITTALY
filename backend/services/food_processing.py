import tensorflow as tf
import numpy as np
from io import BytesIO
from PIL import Image
from cryptography.fernet import Fernet
from services.usda_api import get_nutrition_from_usda

# Load AI Model
EfficientNetB0 = tf.keras.applications.EfficientNetB0
preprocess_input = tf.keras.applications.efficientnet.preprocess_input
decode_predictions = tf.keras.applications.efficientnet.decode_predictions
model = EfficientNetB0(weights="imagenet")

# Generate a secure key for encryption of user image
ENCRYPTION_KEY = Fernet.generate_key()
cipher = Fernet(ENCRYPTION_KEY)

def process_food_image(file):
    try:
        # Read file into memory
        image_bytes = file.file.read()

        # Encrypt image in memory
        encrypted_image = cipher.encrypt(image_bytes)

        # Decrypt it before processing
        decrypted_image = cipher.decrypt(encrypted_image)

        # Convert to an image format
        image = Image.open(BytesIO(decrypted_image)).resize((224, 224))
        image_array = np.array(image)
        image_array = np.expand_dims(image_array, axis=0)
        image_array = preprocess_input(image_array)

        # Process image with AI
        predictions = model.predict(image_array)
        decoded_predictions = decode_predictions(predictions, top=1)[0]
        detected_food = decoded_predictions[0][1]
        confidence = float(decoded_predictions[0][2])

        # Fetch nutrition info from USDA API
        nutrition = get_nutrition_from_usda(detected_food)

        # Delete image from memory
        del encrypted_image
        del decrypted_image

        return {
            "food": detected_food,
            "confidence": confidence,
            "calories": nutrition["calories"],
            "macros": {
                "protein": nutrition["protein"],
                "carbs": nutrition["carbs"],
                "fats": nutrition["fats"],
                "fiber": nutrition["fiber"],
            }
        }

    except Exception as e:
        return {"error": str(e)}
