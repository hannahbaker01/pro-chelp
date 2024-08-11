from pyrogram import Client, filters
from pyrogram.types import Message
from .database import get_databse
from Config import OWNER_ID

users_database = get_databse('users')

@Client.on_message(~filters.service, group=1)
async def users_mongodb(_, msg: Message):
    if msg.from_user:
        user_id = int(msg.from_user.id)
        users_database.update_one(
            {'id': user_id},
            {'$set': {'id': user_id}},
            upsert=True
        )

@Client.on_message(filters.user(OWNER_ID) & filters.command("stats"))
async def _stats(_, msg: Message):
    users_count = users_database.count_documents({})
    await msg.reply(f"Total Users: {users_count}", quote=True)