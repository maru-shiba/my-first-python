import datetime
import os

# 1. 日記の入力
today = datetime.date.today()
print("--- " + str(today) + " のメダカ観察記録 ---")
condition = input("今日のメダカの様子は？: ")
color = input("今日のウロコの色つやは？: ")

# 2. 保存する日記の1行を作成
log_entry = str(today) + " | 状態: " + condition + " | 色: " + color

# 3. README.md を読み込んで日記コーナーを書き換える
with open("README.md", "r", encoding="utf-8") as f:
    lines = f.readlines()

# READMEの中身を更新（「## 🐟 最新のメダカ観察ログ」という行を探して、その次を書き換える）
with open("README.md", "w", encoding="utf-8") as f:
    for line in lines:
        f.write(line)
        if "## 🐟 最新のメダカ観察ログ" in line:
            f.write("> **" + log_entry + "** \n")
            f.write("> (※Pythonプログラムにより自動更新中！)\n")

# --- 修正版：GitHubへ自動送信 ---
print("\n--- GitHubへ自動送信中... ---")
import subprocess

# 1. 「今のフォルダにあるもの全部」を対象にする
subprocess.run(["git", "add", "."], shell=True)

# 2. メッセージをつけて確定
subprocess.run(["git", "commit", "-m", "Auto-update medaka log"], shell=True)

# 3. 強制的に送信
subprocess.run(["git", "push", "origin", "main"], shell=True)

print("\nすべて完了！今度こそGitHubを確認してみてね。")
