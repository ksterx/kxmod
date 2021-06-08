import os
import glob
import cv2
import tqdm

def png2jpg(filename):
    img = cv2.imread(filename)
    cv2.imwrite(filename[:-4] + '.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 100])

def jpg2png(filename):
    img = cv2.imread(filename)
    cv2.imwrite(filename[:-4] + '.png', img)


if __name__ == '__main__':
    print('''
    =========================================================
                        SELECT MODE
    ---------------------------------------------------------
    a: Convert a single image's extension
    d: Convert images' extension in the specified directory
    =========================================================
    ''')

    mode = input('MODE: ')
    converter = ImgConverter()

    if mode == 'a':
        dst_ext = input('To PNG/JPG: ')
        img_path = input('Path: ')
        image = cv2.imread(img_path)
        converted_image = cv2.imwrite()

    elif mode == 'd':
        img_dir = input('Directory path: ')
        from_ext = input('From PNG/JPG: ')
        dst_ext = input('To PNG/JPG: ')

    
        for img_path in tqdm.tqdm(glob.glob(img_dir + f'/*.{from_ext.lower()}')):
            png2jpg(img_path)
