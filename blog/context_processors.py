from .consumers import ONLINE_USERS

def online_status(request):
    return {
        "online_users": ONLINE_USERS
    }
