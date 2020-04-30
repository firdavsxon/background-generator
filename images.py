from PIL import Image, ImageFilter, ImageEnhance

img = Image.open('./Pokedox/pikachu.jpg')
print(img.format, img.mode, img.size)

# img1= img.filter(ImageEnhance.Contrast(img))
# img1.save('sharp.png', 'png')
filtered_img = img.convert('L')

rezise = filtered_img.resize((300, 300))
rezise.save('small.png', 'png')
rezise.show()
# out = img.point(lambda i: i * 1.3)
# out.show()
# enh = ImageEnhance.Contrast(img)
# enh.enhance(1.3).show("50% more contrast")
#



