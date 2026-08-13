# Mood Assignment Guide — برای ایجنت خودکار

منبع تاکسونومی: `moods.yaml` (۸ اسلاگ ثابت، بدون اجازه‌ی اضافه‌کردن مقدار جدید در runtime).

## ورودی
یک فایل `references/RXXX.yaml`.

## گام ۱ — جمع‌آوری متن (به ترتیب اولویت)
1. فیلد `mood` (اگر بود) — مثل `"intimate, luxurious, calming, ritual"`
2. فیلد `style` (اگر `mood` نبود) — مثل `"Clinical-Science-Luxury"` → روی `-` اسپلیت شود
3. `concept_idea` / `reuse` — جمله‌ی توصیفی آزاد
4. فیلدهای ساختاریافته‌ی کمکی: `color_temperature`, `contrast`, `saturation`,
   `lighting.type` یا `lighting_quality`, `background.type`
5. اگر هیچ‌کدام نبود (فایل stub مثل R007/R009/R014/R016/R018) → از اسلاگ توی
   `file:` استفاده شود، مثلاً `R096_..._high-key-pureness.jpg` → `high-key-pureness`

## گام ۲ — توکنایز
متن جمع‌شده را lowercase و روی `,` `-` `space` اسپلیت کن.

## گام ۳ — امتیازدهی
هر توکن که داخل لیست `keywords` یکی از moodهای `moods.yaml` باشد، +۱ امتیاز به آن slug می‌دهد.

## گام ۴ — تصمیم نهایی
- بیشترین امتیاز برنده است.
- در تساوی، این ترتیب اولویت اعمال شود:
  `luxury-premium → moody-dramatic → clinical-fresh → natural-botanical →
  dreamy-ethereal → energetic-bold → playful-fun → warm-intimate`
- اگر امتیاز همه صفر بود (هیچ کلمه‌ای match نشد) → به‌جای حدس زدن، اسلاگ
  `unknown` (اسلاگ `default: true`) با `mood_confidence: 0` ست شود و
  `needs_review: true` خودکار فعال شود. این یعنی «داده کافی نداشتیم»، نه
  یک mood واقعی — در UI هم به‌عنوان یک چیپ جدا («نامشخص») دیده می‌شود، نه
  اینکه به‌اشتباه زیر یک mood واقعی قایم شود.

## گام ۵ — خروجی (نوشته می‌شود در همان yaml یا در build manifest)
```yaml
mood: luxury-premium
mood_confidence: 0.8        # نسبت کلمات matched به کل توکن‌ها (سقف ۱٫۰)
mood_source: agent          # manual | agent
mood_evidence: [intimate, luxurious, calming]   # برای audit
```

## قوانین مهم
- اگر `mood_source: manual` بود، هرگز override نشود.
- اگر `mood_confidence < 0.4` → `needs_review: true` ست شود تا بعداً دستی چک شود.
