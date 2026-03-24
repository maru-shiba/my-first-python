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

# 4. GitのコマンドをPythonから自動で実行する（少し強力な書き方に変更）
print("\n--- GitHubへ自動送信中... ---")

# 1つずつ確実に実行し、結果を画面に出すようにします
import subprocess


subprocess.run(["git", "add", "."])  
subprocess.run(["git", "commit", "-m", "Auto-update medaka log"])
subprocess.run(["git", "push", "origin", "main"])

print("\nすべて完了！今度こそGitHubを確認してみてね。")