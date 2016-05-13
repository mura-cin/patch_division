from PIL import Image

patch_size = (20, 20)           # パッチの大きさ

img = Image.open('path/to/image')

for i in range(0, img.size[1]-patch_size[1], patch_size[1]):
    for j in range(0, img.size[0]-patch_size[0], patch_size[0]):
        crop_img = img.crop((i, j, i+patch_size[1], j+patch_size[0]))
        crop_img.save(img.filename.replace('.', '{0}_{1}.'.format(j, i)))

