from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 模擬資料庫：暫存書本閱讀心得記錄
# 欄位：title (書名), author (書作者), content (心得內容), note (筆記/紀錄)
books = [
    {
        "title": "原子習慣",
        "author": "詹姆斯‧克利爾 (James Clear)",
        "content": "每天進步 1%，一年後就會進步 37 倍。這本書改變了我對習慣養成的看法，關鍵在於打造微小的系統而非死守目標。",
        "note": "核心四大法則：讓提示顯而易見、讓習慣有吸引力、讓行動輕而易舉、讓獎賞令人滿足。"
    },
    {
        "title": "被討厭的勇氣",
        "author": "岸見一郎、古賀史健",
        "content": "阿德勒心理學以對話形式展開，探討人際關係的本質，讀完之後大幅降低了對他人評價的焦慮感。",
        "note": "課題分離是解脫的第一步：分清楚這是誰的課題，不去干涉別人的課題，也不讓別人干涉自己的課題。"
    }
]

# 首頁：列出所有閱讀心得
@app.route("/")
def index():
    return render_template("index.html", books=books)

# 新增心得：顯示表單 (GET) 與接收資料 (POST)
@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        author = request.form.get("author", "").strip()
        content = request.form.get("content", "").strip()
        note = request.form.get("note", "").strip()

        # 確認四個欄位皆有填寫後加入清單
        if title and author and content and note:
            books.append({
                "title": title,
                "author": author,
                "content": content,
                "note": note
            })
            return redirect(url_for("index"))

    return render_template("create.html")

if __name__ == "__main__":
    app.run(debug=True)