import os
from PIL import Image

def resize_image(image_path):
    """画像を横幅500ピクセル以下にリスケールする関数"""
    with Image.open(image_path) as img:
        # 現在の画像の横幅を取得
        width, height = img.size
        if width > 1000:
            # 横幅が500ピクセルを超える場合にリスケール
            new_width = 1000
            new_height = int((new_width / width) * height)
            # リサイズ
            img = img.resize((new_width, new_height), Image.ANTIALIAS)
            # 上書き保存
            img.save(image_path)

def resize_images_in_folder(folder_path):
    """フォルダ内のすべての画像ファイルをリスケールする関数"""
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # 画像ファイルの拡張子をチェック（.jpg, .jpeg, .png, .bmp, .gif など）
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
                image_path = os.path.join(root, file)
                print(f"Found image: {image_path}")  # 見つかった画像のパスを表示
                resize_image(image_path)

# カレントディレクトリからスタートする
folder_path = os.getcwd()  # カレントディレクトリを取得
resize_images_in_folder(folder_path)
