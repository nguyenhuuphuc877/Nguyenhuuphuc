[app]
# Tên app hiển thị trên Android
title = DDoSApp

# Tên gói và domain ngược để tạo package name
package.name = ddosapp
package.domain = org.example.ddosapp

# Thư mục chứa source code chính (dấu chấm là thư mục hiện tại)
source.dir = .
source.include_exts = py
source.main = main.py

# Phiên bản app
version = 1.0
requirements = python3,kivy,requests

# Chiều xoay màn hình: portrait hoặc landscape
orientation = portrait

# Kích hoạt touch
fullscreen = 1

# Biểu tượng app (có thể xóa nếu không dùng)
# icon.filename = %(source.dir)s/icon.png

# Android SDK/API
android.api = 33
android.minapi = 21
android.ndk = 25b
android.gradle_dependencies = 
android.gradle_plugin_version = 7.0.0
android.build_tools_version = 34.0.0

# Không yêu cầu storage permission
android.permissions = INTERNET

# App không bị sleep
android.wakelock = 1

# Chạy không có debug log
log_level = 1

# Ngăn buildozer cảnh báo khi chạy bằng root
warn_on_root = 0

# Không dùng app presplash, nếu cần thì thêm ảnh
# presplash.filename = %(source.dir)s/presplash.png

# Thư viện cần bundle sẵn vào APK
android.private_storage = True

# (Tuỳ chọn) sử dụng AndroidX để fix lỗi layout mới
android.enable_androidx = True
