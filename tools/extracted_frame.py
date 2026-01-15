import cv2

# --- 設定 ---
video_path = '/path/to/default.mp4'
save_path = 'extracted_frame.png'  # 保存するファイル名
target_time = 2.0                 # 切り出したい秒数（例: 2.0秒）

# --- メイン処理 ---
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("動画ファイルを開けませんでした。パスを確認してください。")
else:
    # 指定時間のフレームへ移動（ミリ秒単位なので1000倍する）
    cap.set(cv2.CAP_PROP_POS_MSEC, target_time * 1000)
    
    # フレームを読み込む
    ret, frame = cap.read()
    
    if ret:
        # 秒数を描画する処理（draw_label）をカットしてそのまま保存
        cv2.imwrite(save_path, frame)
        print(f"{target_time}秒の地点を画像として保存しました: {save_path}")
    else:
        print("指定した時間のフレームを取得できませんでした。")

cap.release()