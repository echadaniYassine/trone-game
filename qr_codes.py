import qrcode
import os
from PIL import Image, ImageDraw, ImageFont
import arabic_reshaper
from bidi.algorithm import get_display

base_url = "https://trone-game.vercel.app"

html_dir = "public/questions"
qr_dir = "public/qr_codes"
os.makedirs(html_dir, exist_ok=True)
os.makedirs(qr_dir, exist_ok=True)

questions = [
    "نشيد المساء",
    "ما اسم العالم الذي أضاف الصفر إلى النظام العددي؟",
    "ما الدولة التي تحتوي على أكبر عدد من الجزر؟",
    "من هو مؤسس علم الاجتماع؟",
    "في أي سنة تم نفي الملك محمد الخامس إلى كورسيكا؟",
    "ما اسم الاتفاق الذي تم بموجبه تقسيم فلسطين عام 1947؟",
    "ما اسم المنظمة التي تأسست عام 1964 لتمثيل الشعب الفلسطيني؟",
    "من هو قائد معركة الكرامة سنة 1968؟",
    "كم عدد آيات سورة البقرة؟",
    "a c f g o ؟ ما هو الحرف التالي في الترتيب؟",
    "ما هو التفسير الصحيح لمعنى 'الكوثر' في القرآن؟",
    "من هو الصحابي الذي كتب صلح الحديبية؟",
    "ما هي السورة التي نزلت كاملة دفعة واحدة؟",
    "من هو أول من جهر بالقرآن في مكة؟",
    "من هو اللاعب الذي سجل أكبر عدد من الأهداف في تاريخ كأس العالم؟",
    "ما اسم أول دولة عربية شاركت في كأس العالم؟",
    "ما النادي الأكثر تتويجاً بدوري أبطال أوروبا؟",
    "نشيد الطبيعة",
    "إذهب عند المأطرة مريم مراكشي",
    "لديك 3 مفاتيح و3 أبواب مغلقة، لكن لا تعلم أي مفتاح يفتح أي باب. كم محاولة تحتاجها لتتأكد؟",
    "ما هو الحدث الذي يشير إليه الفلسطينيون باسم 'النكبة'؟",
    "ما هي المدينة الفلسطينية التي تعتبر العاصمة حسب اتفاقيات أوسلو؟",
    "ما اسم الجدار الذي بنته إسرائيل في الضفة الغربية، وما هو طوله التقريبي؟",
    "ما هي ثلاث مدن مغربية مصنفة ضمن التراث العالمي لليونسكو؟",
    "ما هي الكتب السماوية التي نزلت قبل القرآن؟",
    "ما الفرق بين الإسراء والمعراج؟",
    "ما هو أطول نهر في المغرب، وما طوله التقريبي؟",
    "ما هو أول مسجد بُني في المغرب؟",
    "إذهب عند المأطر ياسين الشداني",
    "ما هي الدول العربية التي يمر بها خط الاستواء؟",
    "إذهب عند المأطر مهدي الناصري",
    "ما هو الشيء الذي له أوراق وليس بنبات، وله جلد وليس بحيوان؟",
    "كيف توزّع 10 تفاحات على 9 أشخاص بالتساوي؟",
    "نشيد الصباح",
    "3 8 15 24 35 ؟ ما هو الرقم التالي في السلسلة؟",
    "تحدي البالون المزدوج: اثنان من الفريق يضغطان بالونًا بين ظهريهما ويجب أن يسيروا 5 خطوات دون أن يسقط.",
    "إذهب عند المأطر أمين",
    "ما هي الرسالة التي يحملها نشيد الصباح؟",
]


try:
    font_title = ImageFont.truetype("arial.ttf", 40)
    font_question_num = ImageFont.truetype("arialbd.ttf", 50)  # Arial Bold font for bold text
except IOError:
    font_title = ImageFont.load_default()
    font_question_num = ImageFont.load_default()

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">

<head>
    <meta charset="UTF-8" />
    <title>🛡️ طريق العرش - السؤال رقم {num}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="style.css">
    <script src="https://cdn.tailwindcss.com"></script>
</head>

<body class="min-h-screen flex items-center justify-center p-4">

    <div id="stars"></div>
    <div id="stars2"></div>
    <div id="stars3"></div>

    <div class="main-content max-w-xl w-full">

        <div class="card-container rounded-2xl p-8 text-center fade-in">
            
            <p class="text-sm font-bold text-yellow-400/70 mb-4 tracking-wider">السؤال رقم {num}</p>

            <div class="mb-4">
                <svg class="w-20 h-20 mx-auto crown-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
                    fill="url(#gold-gradient)">
                    <defs>
                        <linearGradient id="gold-gradient" x1="0%" y1="0%" x2="0%" y2="100%">
                            <stop offset="0%" style="stop-color:#FFDF00;stop-opacity:1" />
                            <stop offset="100%" style="stop-color:#F0C400;stop-opacity:1" />
                        </linearGradient>
                    </defs>
                    <path
                        d="M19.467 5.414C19.854 5.795 20 6.305 20 6.839V17a3 3 0 0 1-3 3H7a3 3 0 0 1-3-3V6.839c0-.534.146-1.044.533-1.425L9.5 1h5l4.967 4.414zM12 13a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm-4-2a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm8 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2zM12 2l-3.5 3h7L12 2z" />
                </svg>
            </div>
            
            <h2 class="text-2xl md:text-3xl font-bold text-cyan-300 mb-6 question-title-glow">
                سؤال العرش
            </h2>

            <p class="text-xl md:text-2xl font-medium leading-relaxed text-white mb-8">
                {question}
            </p>

            <div class="rounded-xl p-4 mt-4 border border-teal-500/30 bg-teal-500/10">
                <p class="text-teal-300 font-semibold text-lg">
                    🎯 تذكر: كل خطوة تقربك من العرش... فكر بذكاء وانطلق للفوز!
                </p>
            </div>
        </div>

    </div>
</body>

</html>
"""

for i, question in enumerate(questions, 1):
    # Generate HTML question file
    html_filename = f"question_{i}.html"
    html_path = os.path.join(html_dir, html_filename)
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(HTML_TEMPLATE.format(num=i, question=question))

    question_url = f"{base_url}/questions/{html_filename}"

    # Generate QR code image
    qr_img = qrcode.make(question_url).convert("RGB")

    # Settings for final image size and QR scale
    canvas_width = 400
    canvas_height = 500
    qr_scale = 0.7  # 70% of original QR size

    # Resize QR code to smaller size
    qr_new_size = (int(qr_img.width * qr_scale), int(qr_img.height * qr_scale))
    qr_img = qr_img.resize(qr_new_size, Image.LANCZOS)

    # Define colors (matching Tailwind-inspired)
    background_color = (31, 41, 55)  # bg-gray-800 dark
    border_color = (251, 191, 36)    # gold
    text_color_title = (251, 191, 36)  # gold
    text_color_num = (0, 0, 0)  # white for question number text

    # Create new canvas with gradient background
    new_img = Image.new("RGB", (canvas_width, canvas_height), color=background_color)
    draw = ImageDraw.Draw(new_img)

    # Draw vertical gradient background on full canvas
    for y in range(canvas_height):
        r = int(31 + (y / canvas_height) * (251 - 31))
        g = int(41 + (y / canvas_height) * (191 - 41))
        b = int(55 + (y / canvas_height) * (36 - 55))
        draw.line([(0, y), (canvas_width, y)], fill=(r, g, b))

    # Title text positioning (top)
    title_text = "السباق نحو العرش"
    reshaped_title = arabic_reshaper.reshape(title_text)
    bidi_title = get_display(reshaped_title)
    bbox_title = draw.textbbox((0, 0), bidi_title, font=font_title)
    title_width = bbox_title[2] - bbox_title[0]
    title_height = bbox_title[3] - bbox_title[1]
    title_x = (canvas_width - title_width) // 2
    title_y = 30

    # Draw shadow for title
    shadow_color = (133, 94, 0)
    for offset in [(1, 1), (1, 0), (0, 1)]:
        draw.text((title_x + offset[0], title_y + offset[1]), bidi_title, font=font_title, fill=shadow_color)

    # Draw title text
    draw.text((title_x, title_y), bidi_title, font=font_title, fill=text_color_title)

    # Calculate QR code position: centered vertically in remaining space between title and question number area
    qr_x = (canvas_width - qr_new_size[0]) // 2

    # Calculate approximate question number height
    bbox_num_example = draw.textbbox((0, 0), get_display(arabic_reshaper.reshape("🧠 السؤال رقم 1")), font=font_question_num)
    question_num_height = bbox_num_example[3] - bbox_num_example[1]

    qr_top_limit = title_y + title_height + 20
    qr_bottom_limit = canvas_height - question_num_height - 40  # leave space at bottom for question number
    qr_y = qr_top_limit + (qr_bottom_limit - qr_top_limit - qr_new_size[1]) // 2

    # Draw rounded border around QR code
    border_thickness = 4
    border_rect = [
        qr_x - border_thickness // 2,
        qr_y - border_thickness // 2,
        qr_x + qr_new_size[0] + border_thickness // 2,
        qr_y + qr_new_size[1] + border_thickness // 2,
    ]

    draw.rounded_rectangle(
        border_rect,
        outline=border_color,
        width=border_thickness,
        radius=10
    )

    # Paste QR code
    new_img.paste(qr_img, (qr_x, qr_y))

    # Question number text positioning (bottom)
    raw_text = f"السؤال رقم {i}"
    reshaped = arabic_reshaper.reshape(raw_text)
    bidi_text = get_display(reshaped)
    bbox_num = draw.textbbox((0, 0), bidi_text, font=font_question_num)
    num_width = bbox_num[2] - bbox_num[0]
    num_height = bbox_num[3] - bbox_num[1]
    num_x = (canvas_width - num_width) // 2
    num_y = canvas_height - num_height - 30  # 30 px padding from bottom

    # Draw question number text (bold)
    draw.text((num_x, num_y), bidi_text, font=font_question_num, fill=text_color_num)

    # Save styled QR code image
    qr_path = os.path.join(qr_dir, f"qr_{i}.png")
    new_img.save(qr_path)

    print(f"✅ QR {i} جاهز: {qr_path} → {question_url}")
