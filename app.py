import zipfile
import os
import tempfile
import ctypes
import time
import threading


# تابع برای اجرای برنامه به عنوان ادمین
def run_as_admin(exe_path):
    try:
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", exe_path, None, None, 1)
    except Exception as e:
        print(f"Error running as admin: {e}")


# تابع برای استخراج و اجرای فایل EXE
def extract_and_run():
    # مسیر فایل ZIP و اطلاعات فایل exe را مشخص کنید
    zip_file_path = 'Internet.Download.Manager.6.42.27.zip'
    # مسیر فایل exe داخل zip
    exe_file_name = 'Internet.Download.Manager.6.42.27/Patch/Patch.exe'
    zip_password = b'soft98.ir'  # رمز عبور فایل ZIP

    try:
        # باز کردن فایل ZIP و استخراج فایل EXE
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            # بررسی وجود فایل مورد نظر در آرشیو
            if exe_file_name in zip_ref.namelist():
                while True:
                    # ساخت یک فایل موقت برای استخراج
                    with tempfile.TemporaryDirectory() as temp_dir:
                        temp_exe_path = os.path.join(
                            temp_dir, os.path.basename(exe_file_name))

                        # استخراج فایل exe با رمز عبور
                        try:
                            zip_ref.extract(
                                exe_file_name, temp_dir, pwd=zip_password)
                        except RuntimeError as e:
                            print(f"Error extracting ZIP file: {e}")
                            break

                        # مسیر کامل فایل استخراج شده
                        extracted_path = os.path.join(temp_dir, exe_file_name)

                        try:
                            # تغییر نام فایل به مسیر موقت جدید
                            os.rename(extracted_path, temp_exe_path)

                            # اجرای فایل به صورت ادمین
                            run_as_admin(temp_exe_path)

                        except OSError as e:
                            print(f"File operation error: {e}")
                            break
            else:
                print(f"فایل {exe_file_name} در آرشیو یافت نشد.")
    except FileNotFoundError:
        print(f"فایل {zip_file_path} یافت نشد.")
    except zipfile.BadZipFile:
        print(f"{zip_file_path} یک فایل ZIP معتبر نیست.")
    except Exception as e:
        print(f"Unexpected error: {e}")


# تعداد رشته‌ها را مشخص کنید
num_threads = 300  # تعداد رشته‌ها
# __________________________________num_threads بر اساس سیستم تنظیم کن


# ایجاد و راه‌اندازی رشته‌ها
threads = []
try:
    for _ in range(num_threads):
        thread = threading.Thread(target=extract_and_run)
        thread.start()
        threads.append(thread)

    # انتظار برای پایان همه رشته‌ها
    for thread in threads:
        thread.join()

except KeyboardInterrupt:
    print("Execution interrupted by user.")
except Exception as e:
    print(f"Error managing threads: {e}")
