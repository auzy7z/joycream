user_memory = {}

def update_memory(user_id, username):
    user_memory[user_id] = username

def get_memory(user_id):
    return user_memory.get(user_id, "User tidak dikenal")
