from PIL import Image

def get_chr(code):
    return chr(int(code, 2))

def main():
    img = Image.open("source/output.png")
    pixels = img.load()
    curren_code = ''
    data = ''
    index = 0
    with open('source/Output_Text.txt', 'w') as out_file: 
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                index += 1
                if len(curren_code) == 0:
                    if pixels[i, j][3] == 253:
                        out_file.write(data)
                        out_file.close()
                        return
                    else:
                        curren_code += str(255 - pixels[i, j][3])
                elif (len(curren_code) == 17):
                    curren_code += str(255 - pixels[i, j][3])
                    data += get_chr(curren_code)
                    curren_code = ""
                else:
                    curren_code += str(255 - pixels[i, j][3])
                    

if __name__ == "__main__":
    main()
                