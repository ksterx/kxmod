import glob
import os

import cv2
import tqdm


class ImgConverter:
    def __init__(self, from_ext, to_ext, mode='d'):
        self.mode = mode
        self.from_ext = from_ext
        self.to_ext = to_ext

    def __call__(self, img_path):
        if self.from_ext == 'png' and self.to_ext == 'jpg':
            self.png2jpg(img_path)

        elif self.from_ext == 'jpg' and self.to_ext == 'png':
            self.jpg2png(img_path)

    def png2jpg(self,img_path):
        img = cv2.imread(img_path)
        cv2.imwrite(img_path[:-4] + '.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 100])

    def jpg2png(self, img_path):
        img = cv2.imread(img_path)
        cv2.imwrite(img_path[:-4] + '.png', img)


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

    if mode == 'a':
        dst_ext = input('To PNG/JPG: ')
        img_path = input('Path: ')
        image = cv2.imread(img_path)
        converted_image = cv2.imwrite()

    elif mode == 'd':
        img_dir = input('Directory path: ')
        from_ext = input('From png/jpg: ')
        to_ext = input('To png/jpg: ')
        converter = ImgConverter(from_ext=from_ext, to_ext=to_ext)

        for img_path in tqdm.tqdm(glob.glob(img_dir + f'/*.{from_ext.lower()}')):
            converter(img_path)
