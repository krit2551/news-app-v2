from flask import Flask, render_template

app = Flask(__name__)

# คลังข้อมูลข่าวสาร (เหมือนเราจำลองการดึงข้อมูลจาก SQL มาเก็บไว้ในตัวแปร Python)
ALL_NEWS = [
    {
        "id": 1,
        "title": "ดาบพิฆาตอสูร (鬼滅の刃) (Kimetsu no Yaiba)",
        "post_date": "4 มิถุนายน 2026",
        "category": "anime",
        "category_color": "#2ecc71",
        "detail": "เป็นซีรีส์หนังสือการ์ตูนของประเทศญี่ปุ่น เขียนเรื่องโดย โคโยฮารุ โกโตเกะ เนื้อหากล่าวถึงคามาโดะ ทันจิโร่ เด็กหนุ่มผู้กลายเป็นนักล่าอสูรหลังจากครอบครัวของตนถูกอสูรฆ่าตายทั้งหมด...",
        "read_more_url": "https://th.wikipedia.org/wiki/%E0%B8%94%E0%B8%B2%E0%B8%9A%E0%B8%9E%E0%B8%B4%E0%B8%86%E0%B8%B2%E0%B8%95%E0%B8%AD%E0%B8%AA%E0%B8%B9%E0%B8%A3",
        "image_src": "https://images.unsplash.com/photo-1578632767115-351597cf2477?w=500"
    },
    {
        "id": 2,
        "title": "อาเนีย ฟอร์เจอร์ (SPY×FAMILY)",
        "post_date": "4 มิถุนายน 2026",
        "category": "anime",
        "category_color": "#2ecc71",
        "detail": "ตัวละครเอกสุดน่ารักจากมังงะและอนิเมะเรื่อง SPY×FAMILY เธอเป็นเด็กหญิงวัยอนุบาลผู้มีพลังจิตอ่านใจคนได้ โดยเธอเป็นลูกบุญธรรมของ ลอยด์ ฟอร์เจอร์ และ ยอร์ ฟอร์เจอร์...",
        "read_more_url": "https://th.wikipedia.org/wiki/%E0%B8%AA%E0%B8%A4%E0%B8%B2%E0%B8%A2%C3%97%E0%B9%81%E0%B8%9F%E0%B8%A1%E0%B8%B4%E0%B8%A5%E0%B8%B5",
        "image_src": "https://images.unsplash.com/photo-1607604276583-eef5d076aa5f?w=500"
    },
    {
        "id": 3,
        "title": "เด้งโดด เปลี่ยนโหมดเป็นบีเวอร์ (Hoppers)",
        "post_date": "5 มิถุนายน 2026",
        "category": "local",
        "category_color": "#e67e22",
        "detail": "เป็นภาพยนตร์แอนิเมชันอเมริกัน แนววิทยาศาสตร์และตลก ผลิตโดยพิกซาร์แอนิเมชันสตูดิโอส์ สำหรับวอลต์ดิสนีย์พิกเชอส์ ออกฉายใน ค.ศ. 2026 กำกับโดยแดเนียล ชอง และเขียนบทโดยชองร่วมกับเจสซี แอนดรูส...",
        "read_more_url": "https://th.wikipedia.org/wiki/%E0%B9%80%E0%B8%94%E0%B9%80%E0%B8%9A%E0%B8%B4%E0%B8%A5%E0%B9%82%E0%B8%94%E0%B8%94",
        "image_src": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=500"
    }
]

@app.route('/')
def home():
    # หน้าแรกให้ส่งข่าวทั้งหมดไปแสดงผล
    return render_template('index.html', articles=ALL_NEWS, current_tab='all')

@app.route('/category/<cat_name>')
def category(cat_name):
    # หน้าหมวดหมู่ ให้กรองเอาเฉพาะข่าวที่ตรงกับหมวดหมู่ที่กดเลือก
    filtered_news = [article for article in ALL_NEWS if article['category'] == cat_name]
    return render_template('index.html', articles=filtered_news, current_tab=cat_name)

if __name__ == '__main__':
    app.run(debug=True)
