simple_string = "Hellow, world!"
byte_string = b"Hellow, world!"
byte_array_string = bytearray(byte_string)

print(byte_string)
print(type(simple_string))
print(type(byte_string))
print(type(byte_array_string))

name = "John"
byte_name = name.encode("UTF-8")
print(byte_name)
print(type(byte_name))
