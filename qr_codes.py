import qrcode
import os

# رابط موقعك على Vercel (غيّره للرابط الحقيقي الخاص بك)
base_url = "https://trone-game-8pnyfe4jn-yassines-projects-040da835.vercel.app"

# Folder setup (HTML inside public/questions, QR inside public/qr_codes)
html_dir = "public/questions"
qr_dir = "public/qr_codes"
os.makedirs(html_dir, exist_ok=True)
os.makedirs(qr_dir, exist_ok=True)

questions = [
    "ما اسم العالم الذي أضاف الصفر إلى النظام العددي؟",
    "ما الدولة التي تحتوي على أكبر عدد من الجزر؟",
    "من هو مؤسس علم الاجتماع؟",
    "في أي سنة تم نفي الملك محمد الخامس إلى كورسيكا؟",
    "ما اسم الاتفاق الذي تم بموجبه تقسيم فلسطين عام 1947؟",
    "ما اسم المنظمة التي تأسست عام 1964 لتمثيل الشعب الفلسطيني؟",
    "من هو قائد معركة الكرامة سنة 1968؟",
    "كم عدد آيات سورة البقرة؟",
    "ما هو التفسير الصحيح لمعنى 'الكوثر' في القرآن؟",
    "من هو الصحابي الذي كتب صلح الحديبية؟",
    "ما هي السورة التي نزلت كاملة دفعة واحدة؟",
    "من هو أول من جهر بالقرآن في مكة؟",
    "من هو اللاعب الذي سجل أكبر عدد من الأهداف في تاريخ كأس العالم؟",
    "ما اسم أول دولة عربية شاركت في كأس العالم؟",
    "ما النادي الأكثر تتويجاً بدوري أبطال أوروبا؟",
    "لديك 3 مفاتيح و3 أبواب مغلقة، لكن لا تعلم أي مفتاح يفتح أي باب. كم محاولة تحتاجها لتتأكد؟"
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>سؤال في طريق العرش</title>
    <style>
        body {{
            font-family: 'Arial', sans-serif;
            background-color: #111;
            color: #eee;
            padding: 40px;
            text-align: center;
        }}
        .container {{
            border: 2px solid #444;
            border-radius: 15px;
            padding: 30px;
            max-width: 600px;
            margin: auto;
            background-color: #222;
            box-shadow: 0 0 20px #555;
        }}
        h1 {{
            color: gold;
            font-size: 2em;
        }}
        p {{
            font-size: 1.4em;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🛡️ سباق العقول - طريق العرش 🛡️</h1>
        <p>{question}</p>
    </div>
</body>
</html>
"""

for i, question in enumerate(questions, 1):
    html_filename = f"question_{i}.html"
    html_path = os.path.join(html_dir, html_filename)

    # Save HTML file locally
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(HTML_TEMPLATE.format(question=question))

    # URL for the QR code (relative to your Vercel domain)
    question_url = f"{base_url}/questions/{html_filename}"

    # Generate QR code for the URL
    qr = qrcode.make(question_url)
    qr_path = os.path.join(qr_dir, f"qr_{i}.png")
    qr.save(qr_path)

    print(f"✅ تم إنشاء QR: {qr_path} يشير إلى {question_url}")
