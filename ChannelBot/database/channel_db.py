from ChannelBot.database import get_databse

channels = get_databse('channels')

async def num_channels():
    return channels.count_documents({})

async def add_channel(channelid, userid):
    if not channels.find_one({'id': channelid}):
        channels.insert_one({
            'id': channelid,
            'adminid': userid,
            'caption': None,
            'buttons': None,
            'position': None,
            'stickerid': None,
            'edit_mode': None,
            'webpage_preview': False
        })

async def remove_channel(channelid):
    channels.delete_one({'id': channelid})

async def get_channel_info(channelid):
    channel = channels.find_one({'id': channelid})
    if channel:
        return True, {
            'adminid': channel['adminid'],
            'buttons': channel['buttons'],
            'caption': channel['caption'],
            'position': channel['position'],
            'stickerid': channel['stickerid'],
            'webpage_preview': channel['webpage_preview'],
            'edit_mode': channel['edit_mode']
        }
    return False, {}

async def set_caption(channelid, caption):
    result = channels.update_one({'id': channelid}, {'$set': {'caption': caption}})
    return result.modified_count > 0

async def get_caption(channelid):
    channel = channels.find_one({'id': channelid})
    return channel['caption'] if channel and channel['caption'] else ''

async def set_buttons(channelid, buttons):
    result = channels.update_one({'id': channelid}, {'$set': {'buttons': buttons}})
    return result.modified_count > 0

async def get_buttons(channelid):
    channel = channels.find_one({'id': channelid})
    return channel['buttons'] if channel and channel['buttons'] else None

async def set_position(channelid, position):
    result = channels.update_one({'id': channelid}, {'$set': {'position': position}})
    return result.modified_count > 0

async def get_position(channelid):
    channel = channels.find_one({'id': channelid})
    return channel['position'] if channel and channel['position'] else 'below'

async def set_sticker(channelid, sticker):
    result = channels.update_one({'id': channelid}, {'$set': {'stickerid': sticker}})
    return result.modified_count > 0

async def get_sticker(channelid):
    channel = channels.find_one({'id': channelid})
    return channel['stickerid'] if channel and channel['stickerid'] else None

async def toggle_webpage_preview(channelid, value):
    result = channels.update_one({'id': channelid}, {'$set': {'webpage_preview': value}})
    return result.modified_count > 0

async def get_webpage_preview(channelid):
    channel = channels.find_one({'id': channelid})
    return channel['webpage_preview'] if channel else False

async def set_edit_mode(channelid, edit_mode):
    result = channels.update_one({'id': channelid}, {'$set': {'edit_mode': edit_mode}})
    return result.modified_count > 0

async def get_edit_mode(channelid):
    channel = channels.find_one({'id': channelid})
    return channel['edit_mode'] if channel and channel['edit_mode'] else 'media'