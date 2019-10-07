import hashlib
print ("code by Tariq")
print ("Encryption")
text = str(input("Enter Text"))
hash_type = str(input("Enter Hash Type : "))
text = text.encode ('utf-8')
hash_hash = hashlib.new(hash_type)
hasher =hash_hash.hexdigest()
print (hasher)