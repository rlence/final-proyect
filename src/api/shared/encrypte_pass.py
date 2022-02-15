import bcrypt

def encryp_pass(password):
    hash_pass = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hash_pass.decode()

def compare_pass(password, hash_pass):
    return bcrypt.checkpw(password.encode('utf-8'), hash_pass.encode('utf-8'))