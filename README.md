# 🛡️ Elastic Agent Malware Bypass (PoC Project)
> Author: @m-mjd  
> Status: In development (two fully working variants)

---

## 🧠 Description (English)

This is a **proof-of-concept (PoC)** project that demonstrates how to **bypass Elastic Agent's EDR mechanisms** using high-speed, parallelized execution of a malware payload extracted from a password-protected ZIP archive.

---

### 🧩 Targeted System

> ⚠️ **This project has been tested exclusively on Elastic Agent.**  
> It is **specifically designed** to bypass Elastic Agent’s default EDR behavior and **does not guarantee results on other EDR platforms**.

The method exploits **latency in Elastic Agent’s real-time analysis**, by rapidly executing threads that outrun the agent’s detection and response. Payloads are executed from the system TEMP directory to further reduce traceability.

---

## 🔍 Key Features

- Malware `.exe` stored in a **password-protected ZIP file**
- Extracted to a **TEMP directory**, executed **with admin privileges**
- Implements **multi-threaded and nested-thread design**
    - Thousands of primary threads are created
    - Each primary thread may spawn deeper internal processes or task flows
    - Enables **multi-layer parallelism** that maximizes CPU usage and disrupts typical inspection cycles
- Some threads execute harmless "dummy" tasks to further mislead behavior-based monitoring
- Designed to execute faster than EDR systems like Elastic Agent can react

---

## 📁 File Overview

| File     | Threads Used | Description                      |
|----------|---------------|----------------------------------|
| `ap.py`  | 30,000         | Full-force version, includes dummy threads for load |
| `app.py` | 300            | Lightweight version for controlled testing |

> The final version will combine these two approaches into one unified and optimized script.

---

## ⚙️ Execution Technique

This tool uses **multi-level threading**, not just concurrency but **parallel spawning inside threads**. Each thread that performs payload operations runs fully isolated and races ahead of EDR’s detection logic. This increases the chances of successfully executing the payload before monitoring systems engage.

---

## 📦 Payload Info

- ZIP File: `Internet.Download.Manager.6.42.27.zip`
- Password: `soft98.ir`
- Target EXE: `Internet.Download.Manager.6.42.27/Patch/Patch.exe`

---

## ⚠️ Legal & Ethical Disclaimer

> This project is strictly for **research and educational purposes only**.  
> The author does **not condone or support any illegal activity**, and takes **no responsibility for misuse** of the provided code.

---

## 🧿 توضیحات فارسی

این پروژه یک نمونه‌ی آزمایشی (PoC) برای بای‌پس کردن EDR در **Elastic Agent** است که با استفاده از **اجرای هم‌زمان (multi-threaded) و تو در تو (nested-threaded)** یک فایل اجرایی از داخل یک فایل ZIP رمزدار انجام می‌شود.

---

### 🎯 سیستم هدف

> ⚠️ **این ابزار فقط روی Elastic Agent تست شده و مخصوص آن طراحی شده است.**  
> عملکرد آن روی سایر EDRها تضمین نمی‌شود.

این تکنیک با تکیه بر تاخیر Elastic Agent در بررسی‌های بلادرنگ، اجرای فایل مخرب را با سرعتی بیشتر از توان شناسایی آن انجام می‌دهد. اجرای فایل از TEMP هم شناسایی آن را سخت‌تر می‌کند.

---

## 🚀 ویژگی‌ها

- اجرای فایل `.exe` از یک فایل ZIP رمزدار  
- استخراج فایل به پوشه‌ی `TEMP` و اجرای آن با دسترسی ادمین  
- ساختار تردها به صورت **تودرتو و چندمرحله‌ای**:
    - تردهای اولیه ایجاد می‌شوند که هرکدام ممکن است عملیات جداگانه‌ای داشته باشند
    - بعضی تردها وظیفه اجرای اصلی را دارند و بقیه فقط بار سیستم را بالا می‌برند
    - نتیجه این طراحی: **سرعت اجرای کد از سرعت واکنش EDR بیشتر می‌شود**
- بعضی از تردها فقط فعالیت کم‌خطر انجام می‌دهند (مثل sleep) تا رفتار مخرب گم شود

---

## 🧾 فایل‌ها

| فایل     | تعداد ترد | توضیحات                           |
|----------|-----------|------------------------------------|
| `ap.py`  | ۳۰٬۰۰۰     | نسخه‌ی کامل با تردهای اضافی برای بارگذاری CPU |
| `app.py` | ۳۰۰        | نسخه‌ی سبک‌تر برای تست‌های کنترل‌شده          |

> نسخه نهایی این دو روش را به شکل بهینه در یک اسکریپت واحد ادغام می‌کند.

---

## 📛 هشدار قانونی و اخلاقی

> این پروژه صرفاً برای **تحقیق و آموزش** است.  
> نویسنده هیچ‌گونه مسئولیتی در قبال **استفاده غیرقانونی** از این پروژه ندارد.

---

## 📬 Contact

For permission requests or collaboration:  
GitHub: [@m-mjd](https://github.com/m-mjd)
