import random
print("--- 占いの館へようこそ ---")
name = input("お名前を教えてください：")
fortunes =[
    "🌟 大吉：最高の一日！何をやってもうまくいきます。",
    "☀️ 中吉：ラッキーなことが起こりそうな予感。",
    "☁️ 小吉：いつも通りの平和な一日です。",
    "☔️ 末吉：忘れ物に注意。落ち着いて行動しましょう。",
    "🌀 凶：今日はゆっくり休むのが吉。明日はいいことあるよ！",
    ]
result = random.choice(fortunes)
print("-" * 25)
print(f"{name}さんの今日の運勢は...")
print(result)
print("-" * 25)
