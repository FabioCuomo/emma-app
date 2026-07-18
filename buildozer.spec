[app]
title = Emma
package.name = emma
package.domain = org.esempio
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.3.0
orientation = portrait
fullscreen = 0

android.archs = arm64-v8a
android.api = 34
android.minapi = 24
android.ndk = 25b
android.accept_sdk_license = True

p4a.branch = v2024.01.21

[buildozer]
log_level = 2
warn_on_root = 1
