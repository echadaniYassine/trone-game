import qrcode
import os

# رابط موقعك الفعلي على Vercel
base_url = "https://trone-game.vercel.app"

# إعداد المجلدات
html_dir = "public/questions"
qr_dir = "public/qr_codes"
os.makedirs(html_dir, exist_ok=True)
os.makedirs(qr_dir, exist_ok=True)

# قائمة الأسئلة
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

# قالب HTML مع تصميم Tailwind وأنيميشن
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8" />
    <title>🛡️ طريق العرش - سؤال</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @keyframes fadeInUp {{
            0% {{ opacity: 0; transform: translateY(40px); }}
            100% {{ opacity: 1; transform: translateY(0); }}
        }}
        .fade-in {{
            animation: fadeInUp 0.8s ease-out forwards;
        }}
    </style>
</head>
<body class="bg-gray-900 text-gray-100 min-h-screen flex items-center justify-center px-4 py-8">
    <div class="bg-gray-800 border-2 border-yellow-500 rounded-3xl shadow-2xl max-w-xl w-full p-8 text-center fade-in">
        <h1 class="text-2xl md:text-3xl font-bold text-yellow-400 mb-6 animate-pulse">
            🛡️ سباق العقول - طريق العرش 🛡️
        </h1>
        <p class="text-xl md:text-2xl font-medium leading-relaxed text-white mb-8">{question}</p>
        <div class="rounded-xl p-4 mt-4 border border-teal-500/30 bg-teal-500/10">
            <p class="text-teal-300 font-semibold text-lg">
                🎯 تذكّر: كل خطوة تقرّبك من العرش... فكر بذكاء وانطلق للفوز!
            </p>
        </div>
    </div>
</body>
</html>
"""

# إنشاء صفحات HTML و QR لكل سؤال
for i, question in enumerate(questions, 1):
    html_filename = f"question_{i}.html"
    html_path = os.path.join(html_dir, html_filename)

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(HTML_TEMPLATE.format(question=question))

    question_url = f"{base_url}/questions/{html_filename}"
    qr_img = qrcode.make(question_url)
    qr_path = os.path.join(qr_dir, f"qr_{i}.png")
    qr_img.save(qr_path)

    print(f"✅ QR جاهز: {qr_path} → {question_url}")
