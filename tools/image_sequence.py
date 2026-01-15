import cv2
import numpy as np

def draw_label(img, text):
    """画像に背景付きのテキストを描画する関数"""
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1.5        # 文字の大きさ
    thickness = 3           # 文字の太さ
    margin = 10             # 文字周りの余白
    
    # テキストのサイズを取得
    (text_width, text_height), baseline = cv2.getTextSize(text, font, font_scale, thickness)
    
    # 背景ボックスの座標（左上）
    # 文字が見やすいように、少し透過した黒背景風（今回は完全に塗りつぶし）にします
    box_coords = ((0, 0), (text_width + margin * 2, text_height + margin * 2 + baseline))
    
    # 黒い四角形を描画（塗りつぶし）
    cv2.rectangle(img, box_coords[0], box_coords[1], (0, 0, 0), -1)
    
    # 白い文字を描画
    cv2.putText(img, text, (margin, text_height + margin), font, font_scale, (255, 255, 255), thickness, cv2.LINE_AA)

# --- メイン処理 ---

video_path = '/home/harukiogawa/ダウンロード/rl-video-step-0.mp4'
#video_path = '/path/to/default.mp4'
cap = cv2.VideoCapture(video_path)

# 時間設定（秒）
# もし0秒が真っ暗なら、0.1秒など少しずらすと何かが映る場合があります
times = [2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4] 
frames = []

for t in times:
    # 指定時間のフレームへ移動
    cap.set(cv2.CAP_PROP_POS_MSEC, t * 1000)
    ret, frame = cap.read()
    
    if ret:
        # ラベルを描画（関数呼び出し）
        draw_label(frame, f"t={t}s")
        frames.append(frame)

cap.release()

# --- 画像の結合処理 ---

if len(frames) >= 8:
    # 1段目（0~4秒）を横に結合
    row1 = cv2.hconcat(frames[0:4])
    
    # 2段目（5~9秒）を横に結合
    row2 = cv2.hconcat(frames[4:8])
    
    # 上下を結合（ここが余白ゼロのポイントです）
    final_img = cv2.vconcat([row1, row2])
    
    # 保存
    cv2.imwrite('image_sequence.png', final_img)
    print("画像を保存しました: image_sequence.png")
else:
    print(f"フレーム数が足りません: {len(frames)}枚")