from base64 import b64encode, b64decode

# name = 'Re: Sharin no Kuni Project'
# f = open(b64encode(name.encode()), 'w')
# f.close()

text = 'UmU6IFNoYXJpbiBubyBLdW5pIFByb2plY3Q='
print(b64decode(text).decode())