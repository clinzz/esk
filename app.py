from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 模擬資料庫：加上 id 欄位作為識別
books = [
    {
        "id": 1,
        "title": "原子習慣",
        "author": "詹姆斯‧克利爾 (James Clear)",
        "content": "每天進步 1%，一年後就會進步 37 倍。這本書改變了我對習慣養成的看法，關鍵在於打造微小的系統而非死守目標。",
        "note": "核心四大法則：讓提示顯而易見、讓習慣有吸引力、讓行動輕而易舉、讓獎賞令人滿足。"
    },
    {
        "id": 2,
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
            # 取現有最大的 id + 1，若清單是空的則從 1 開始
            new_id = max([b["id"] for b in books], default=0) + 1
            books.append({
                "id": new_id,
                "title": title,
                "author": author,
                "content": content,
                "note": note
            })
            return redirect(url_for("index"))

    return render_template("create.html")

# 編輯心得：取得對應書本資料並覆蓋更新
@app.route("/edit/<int:book_id>", methods=["GET", "POST"])
def edit(book_id):
    # 根據 book_id 找出該本書
    book = next((b for b in books if b["id"] == book_id), None)
    if not book:
        return redirect(url_for("index"))

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        author = request.form.get("author", "").strip()
        content = request.form.get("content", "").strip()
        note = request.form.get("note", "").strip()

        if title and author and content and note:
            book["title"] = title
            book["author"] = author
            book["content"] = content
            book["note"] = note
            return redirect(url_for("index"))

    return render_template("edit.html", book=book)

if __name__ == "__main__":
    app.run(debug=True)