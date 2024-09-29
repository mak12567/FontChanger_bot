from pymongo import MongoClient
import os

# Set up MongoDB connection
DATABASE_URI = os.getenv("DATABASE_URI", "") # Your MongoDB URI from the .env file
DATABASE_NAME = os.getenv("DATABASE_NAME","")
client = MongoClient(DATABSE_URI)
db = client['DATABASE_NAME']  # Replace with your actual database name
bot_users = db['bot_users']  # Collection for storing users

def create_bot_user(user):
    user_data = {
        'telegram_id': user.id,
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'language_code': user.language_code,
    }

    try:
        # Insert or update user data in MongoDB
        bot_users.update_one(
            {'telegram_id': user.id},  # Use telegram_id as unique identifier
            {'$set': user_data},  # Update user data
            upsert=True  # Create a new document if it doesn't exist
        )
    except Exception as e:
        print(e)
