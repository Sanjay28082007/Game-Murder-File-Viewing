import os

filename = "Files/evidence/photo/photo.bmp"

with open(filename, 'rb') as photo:
    file_header = photo.read(14)
    if file_header[:2] == b'BM':
        print(f"It is a valid Bitmap file")
        size_bytes = file_header[2:6]
        size_of_file = int.from_bytes(size_bytes, "little")
        size_in_disk = os.path.getsize(filename)
        if size_of_file == size_in_disk:
            print(f"The size in disk is {size_of_file}")
            reserved_bytes = file_header[6:10]
            print(reserved_bytes)
            offset = file_header[10: 14] # 138
            offset_line = int.from_bytes(offset, "little", signed=True)
            photo.seek(offset_line,  1)
            details = photo.read()
            with open("pixels.txt", 'w') as output_file:
                output_file.write(str(details))
        else:
            print(f"This does not equal to the size in disk")
    else:
        print(f"This is not a valid bitmap file")



