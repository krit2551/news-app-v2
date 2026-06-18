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
        "image_src": "https://lh3.googleusercontent.com/d/1MqLDcJb0FeEj9W5DrWY83abMEVI9ZepW"

    },
    {
        "id": 2,
        "title": "อาเนีย ฟอร์เจอร์ (SPY×FAMILY)",
        "post_date": "4 มิถุนายน 2026",
        "category": "anime",
        "category_color": "#2ecc71",
        "detail": "ตัวละครเอกสุดน่ารักจากมังงะและอนิเมะเรื่อง SPY×FAMILY เธอเป็นเด็กหญิงวัยอนุบาลผู้มีพลังจิตอ่านใจคนได้ โดยเธอเป็นลูกบุญธรรมของ ลอยด์ ฟอร์เจอร์ และ ยอร์ ฟอร์เจอร์...",
        "read_more_url": "https://th.wikipedia.org/wiki/%E0%B8%AD%E0%B8%B2%E0%B9%80%E0%B8%99%E0%B8%B5%E0%B8%A2_%E0%B8%9F%E0%B8%AD%E0%B8%A3%E0%B9%8C%E0%B9%80%E0%B8%88%E0%B8%AD%E0%B8%A3%E0%B9%8C",
        "image_src": "https://lh3.googleusercontent.com/d/151TYWInHApCUrM0CCoLGihMkZXY62KDn"
    },
    {
        "id": 3,
        "title": "เด้งโดด เปลี่ยนโหมดเป็นบีเวอร์ (Hoppers)",
        "post_date": "5 มิถุนายน 2026",
        "category": "local",
        "category_color": "#e67e22",
        "detail": "เป็นภาพยนตร์แอนิเมชันอเมริกัน แนววิทยาศาสตร์และตลก ผลิตโดยพิกซาร์แอนิเมชันสตูดิโอส์ สำหรับวอลต์ดิสนีย์พิกเชอส์ ออกฉายใน ค.ศ. 2026 กำกับโดยแดเนียล ชอง และเขียนบทโดยชองร่วมกับเจสซี แอนดรูส...",
        "read_more_url": "https://th.wikipedia.org/wiki/%E0%B9%80%E0%B8%94%E0%B9%89%E0%B8%87%E0%B9%82%E0%B8%94%E0%B8%94_%E0%B9%80%E0%B8%9B%E0%B8%A5%E0%B8%B5%E0%B9%88%E0%B8%A2%E0%B8%99%E0%B9%82%E0%B8%AB%E0%B8%A1%E0%B8%94%E0%B9%80%E0%B8%9B%E0%B9%87%E0%B8%99%E0%B8%9A%E0%B8%B5%E0%B9%80%E0%B8%A7%E0%B8%AD%E0%B8%A3%E0%B9%8C",
        "image_src": "https://lh3.googleusercontent.com/d/1BSe2W1RESnai7heMT0etmU8fbGWK1MyX"

    },
    {
        "id": 4,
        "title": "ทอมแอนด์เจอร์รี่ (Tom & Jerry)",
        "post_date": "18 มิถุนายน 2026",
        "category": "local",
        "category_color": "#e67e22",
        "detail": "เป็นการ์ตูนชุดอเมริกันแนวตลกเจ็บตัว และเป็นสื่อแฟรนไชส์ของเมโทร-โกลด์วิน-เมเยอร์ ปัจจุบันย้ายมาสังกัด บริษัท เทอร์เนอร์เอ็นเตอร์เทนเมนต์...",
        "read_more_url": "https://th.wikipedia.org/wiki/%E0%B8%97%E0%B8%AD%E0%B8%A1%E0%B9%81%E0%B8%AD%E0%B8%99%E0%B8%94%E0%B9%8C%E0%B9%80%E0%B8%88%E0%B8%AD%E0%B8%A3%E0%B9%8C%E0%B8%A3%E0%B8%B5%E0%B9%88",
        "image_src": "https://share.google/images/mLStes9aJzwcQzfqr"
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
