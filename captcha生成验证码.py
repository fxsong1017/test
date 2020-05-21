from captcha.image import ImageCaptcha
import random
import os

# 验证码备选字符集
vocabulary = {
    'number': [str(i) for i in range(10)],
    'uppercase': [chr(i) for i in range(65, 91)],
    'lowercase': [chr(i) for i in range(97, 123)],
}

NUM_IMAGES = 1  # 生成验证码图片的数量
CAPTCHA_LENGTH = 4  # 验证码长度
SAVE_DIR = "./captcha/images/"

# 根据需要选择 captcha 字符集
captcha_set = vocabulary['number']
              # + vocabulary['lowercase'] \
              # + vocabulary['uppercase']

if __name__ == '__main__':
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)

    for i in range(NUM_IMAGES):
        random_captcha_str = []
        # 生成 captcha 随机字符串
        for j in range(CAPTCHA_LENGTH):
            random_captcha_str.append(
                random.choice(captcha_set))

        # 生成 captcha 图片并保存
        captcha = ''.join(random_captcha_str)
        image = ImageCaptcha()
        image.generate(captcha)
        image.write(captcha, SAVE_DIR + captcha + '.png')