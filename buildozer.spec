[app]
title = Jarvis
package.name = jarvis
package.domain = com.echo.light
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,android,jnius
orientation = portrait
osx.kivy_version = 2.3.0
fullscreen = 0
android.permissions = INTERNET, FOREGROUND_SERVICE, RECORD_AUDIO, WAKE_LOCK
android.api = 33
android.minapi = 21
android.ndk_api = 21
android.private_storage = True
android.services = jarvis:jarvis_service.py

[buildozer]
log_level = 2
warn_on_root = 1
