# File for testing code ideas
import hashlib

def hash_item(hash_item):
    encoded_string = hash_item.encode('utf-8')
    hash_object = hashlib.sha256()
    hash_object.update(encoded_string)
    hex_hash = hash_object.hexdigest()
    return hex_hash

username = input("Username ")
password = input("Password ")
hash_pass = hash_item(password)
csv_name = f"docs/{username}.csv"

print(username, hash_pass,csv_name)