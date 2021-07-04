import hashlib

str="GAURAV"  #u can take input from user also

enc=str.encode()
hash=hashlib.md5(enc)
finalhash=hash.hexdigest()

print("md5 hash for given str is : ",finalhash+ "\n")

hash=hashlib.sha1(str.encode())
print("sha1 hash for str is : ",hash.hexdigest()+"\n")


hash=hashlib.sha224(str.encode())
print("sha224 hash for str is : ",hash.hexdigest()+"\n")


hash=hashlib.sha256(str.encode())
print("sha256 hash for str is : ",hash.hexdigest()+"\n")


hash=hashlib.sha384(str.encode())
print("sha384 hash for str is : ",hash.hexdigest()+"\n")

hash=hashlib.sha512(str.encode())
print("sha512 hash for str is : ",hash.hexdigest()+"\n")

