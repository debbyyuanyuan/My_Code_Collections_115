import yt_dlp
import static_ffmpeg
import sys
import os


# 老師的關鍵提示：這行代碼會自動處理 FFmpeg 的安裝路徑
# 解決了手動設定環境變數的麻煩，確保高品質影音能順利合併
static_ffmpeg.add_paths()


def download_youtube_video(url, output_folder="downloads"):
	"""
	使用 yt_dlp 下載 YouTube 影片並自動處理影音合併
	"""


	# 1. 確保儲存資料夾存在
	if not os.path.exists(output_folder):
		os.makedirs(output_folder)
		print(f"✅ 已建立資料夾: {output_folder}")


	# 2. 設定 yt_dlp 配置參數
	ydl_opts = {
		# 格式策略：下載最佳影像 + 最佳音訊
		'format': 'bestvideo+bestaudio/best',


		# 設定儲存路徑與檔名格式
		'outtmpl': f'{output_folder}/%(title)s.%(ext)s',


		# 強制合併為 mp4 格式（需 FFmpeg 支援）
		'merge_output_format': 'mp4',


		# 設定進度回調函數，讓用戶看得到進度
		'progress_hooks': [my_hook],


		# 遇到錯誤跳過（例如播放清單中某影片失效）
		'ignoreerrors': True,


		# 設置 User-Agent 模擬真人瀏覽行為，避免被阻擋
		'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
	}


	print(f"\n🔍 正在分析網址: {url}")


	try:
		# 建立下載執行個體
		with yt_dlp.YoutubeDL(ydl_opts) as ydl:
			# 開始下載並獲取影片資訊
			info_dict = ydl.extract_info(url, download=True)
			
			if info_dict:
				video_title = info_dict.get('title', '未知標題')
				print(f"\n\n🎊 下載任務完成！")
				print(f"📌 影片標題: {video_title}")
				print(f"📂 儲存路徑: {output_folder}/")


	except Exception as e:
		print(f"\n❌ 下載過程中發生錯誤: {e}")


def my_hook(d):
	"""
	顯示下載進度的監控函數
	"""
	if d['status'] == 'downloading':
		# 取得進度、速度與剩餘時間
		percent = d.get('_percent_str', '0%')
		speed = d.get('_speed_str', 'N/A')
		eta = d.get('_eta_str', 'N/A')


		# 動態更新同一行文字
		sys.stdout.write(f"\r⏳ 下載進度: {percent} | 速度: {speed} | 預計時間: {eta}  ")
		sys.stdout.flush()


	elif d['status'] == 'finished':
		print("\n🛠️ 下載已完成，正在使用 FFmpeg 進行影音封裝/合併...")


if __name__ == "__main__":
	print("========================================")
	print("   Python YouTube Pro 下載器 (自動合併版)")
	print("========================================")


	# 使用者輸入網址
	target_url = input("請輸入影片網址: ").strip()


	if target_url:
		download_youtube_video(target_url)
	else:
		print("⚠️ 錯誤：網址不能為空。")