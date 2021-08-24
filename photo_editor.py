from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw


def add_text(text):
    template = Image.open('pic/template.jpg')
    mem = Image.open('pic/mem.jpg').convert('RGBA')

    width = 610
    height = 569
    resized_mem = mem.resize((width, height), Image.ANTIALIAS)

    text_position = (0, 0)
    text_color = (266,0,0)


    strip_width, strip_height = 700, 1300

    def findLen(text_len):
        counter = 0    
        for i in text_len:
            counter += 1
        return counter

    font_width = 60
    
    if findLen(text) >= 25:
        font_width = 50

    background = Image.new('RGB', (strip_width, strip_height)) #creating the black strip
    draw = ImageDraw.Draw(template)

    if '\n' in text:  
        split_offers = text.split('\n')

        for i in range(2):
            if i == 1:
                strip_height += 110
                font_width -= 20
            font = ImageFont.truetype("fonts/font.ttf", font_width) 
            text_width, text_height = draw.textsize(split_offers[i], font)

            position = ((strip_width-text_width)/2,(strip_height-text_height)/2)
            draw.text(position, split_offers[i], font=font)
    else:
        font = ImageFont.truetype("fonts/font.ttf", font_width)
        text_width, text_height = draw.textsize(text, font)
        strip_height = 1330
        position = ((strip_width-text_width)/2,(strip_height-text_height)/2)
        draw.text(position, text, font=font)

    template.paste(resized_mem, (54, 32),  resized_mem)
    template.save("pic/paste/ok.jpg")
        
