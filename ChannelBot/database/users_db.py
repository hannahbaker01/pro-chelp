from ChannelBot.database import get_databse

users = get_databse('users')

async def num_users():
    return users.count_documents({})

async def add_channel(userid, channelid):
    users.update_one(
        {'id': userid},
        {'$addToSet': {'channels': channelid}},
        upsert=True
    )

async def remove_channel(userid, channelid):
    users.update_one(
        {'id': userid},
        {'$pull': {'channels': channelid}}
    )

async def get_channels(userid):
    user = users.find_one({'id': userid})
    if user and 'channels' in user:
        return True, user['channels']
    return False, []