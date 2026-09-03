import json
import os
import random
import urllib.request

def send_discord_message():
    webhook_url = os.environ.get("DISCORD_WEBHOOK_URL")
    
    # ▼ あなたの GitHub Pages の URL に書き換えてください（最後のスラッシュ / を忘れずに）
    app_url = "https://daichi-ishihara-kyoto.github.io/Task-Everyday/"

    if not webhook_url:
        print("Webhook URLが設定されていません。")
        return

    # tasks.json から課題を読み込む
    try:
        with open("tasks.json", "r", encoding="utf-8") as f:
            tasks = json.load(f)
    except Exception as e:
        print("tasks.json の読み込みに失敗しました:", e)
        return

    if not tasks:
        print("課題リストが空です。")
        return

    # 1つランダムに選ぶ
    selected = random.choice(tasks)

    # Discordに送るメッセージの組み立て（Embed形式）
    payload = {
        "username": "ガネーシャ",
        "avatar_url": "https://i.imgur.com/4M34hi2.png",
        "embeds": [
            {
                "title": f"🐘 今日のガネーシャの課題：【{selected['task']}】",
                "description": f"{selected['detail']}\n\n[🔄 別のお告げを引き直す（Webアプリを開く）]({app_url})",
                "color": 15844367
            }
        ]
    }

    headers = {"Content-Type": "application/json"}
    req = urllib.request.Request(
        webhook_url,
        data=json.dumps(payload).encode("utf-8"),
        headers=headers
    )

    try:
        with urllib.request.urlopen(req) as response:
            print("通知完了:", response.status)
    except Exception as e:
        print("送信エラー:", e)

if __name__ == "__main__":
    send_discord_message()
