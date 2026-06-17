from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.utils import platform

class JarvisUI(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        self.status_label = Label(text="Jarvis System: Standing By", font_size='20sp', size_hint_y=0.7)
        layout.add_widget(self.status_label)
        
        btn = Button(text="Activate Jarvis Core", size_hint_y=0.3, background_color=(0, 0.7, 1, 1))
        btn.bind(on_press=self.start_jarvis_service)
        layout.add_widget(btn)
        return layout

    def start_jarvis_service(self, instance):
        if platform == 'android':
            from android import jnius
            try:
                activity = jnius.autoclass('org.kivy.android.PythonActivity').mActivity
                service = jnius.autoclass('com.echo.light.jarvis.ServiceJarvis')
                service.start(activity, "")
                self.status_label.text = "Jarvis Core Active\nListening..."
            except Exception as e:
                self.status_label.text = f"Error: {str(e)}"
        else:
            self.status_label.text = "Desktop Simulation Running."

if __name__ == '__main__':
    JarvisUI().run()
  
