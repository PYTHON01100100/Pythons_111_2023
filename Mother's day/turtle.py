import matplotlib.pyplot as plt

# تهيئة الرسم
fig, ax = plt.subplots(figsize=(6, 4))  # تحديد أبعاد البطاقة

# إضافة صورة كخلفية
img = plt.imread('C:\\Users\\d7oom\\Downloads\\wp.png')
ax.imshow(img)

# رسم بطاقة التهنئة
card_width = 6
card_height = 4
ax.fill([0, card_width, card_width, 0], [0, 0, card_height, card_height], color='white')

# كتابة النص على البطاقة بالإحداثيات المحددة
ax.text(3500, 300, 'Warm Greetings to My Mother', fontsize=21, fontweight='bold')
ax.text(2900, 700, 'Thank you for being the light in my life, Mum', fontsize=19, fontweight='bold')
ax.text(2350, 500, "Happy Mother's Day to the most amazing woman I know", fontsize=19, fontweight='bold')
ax.text(3500, 900, 'From: Abdulrahman al myman', fontsize=16, fontweight='bold')  # إضافة اسمك

# إخفاء محاور الرسم
ax.axis('off')

# عرض البطاقة
plt.show()
