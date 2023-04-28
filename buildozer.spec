[app]

# (str) Title of your application
title = KivyMD Launcher

# (str) Package name
package.name = launcher

# (str) Package domain (needed for android/ios packaging)
package.domain = mx.zino

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,ttf,yaml

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
source.exclude_dirs = tests, bin, art

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 0.1

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma seperated e.g. requirements = sqlite3,kivy
#requirements = kivy, android
#requirements = python3, kivy==master, https://github.com/kivymd/KivyMD/archive/refs/heads/master.zip,Pillow==8.4.0, android, requests, loguru,
requirements = python3, kivy==master, https://github.com/kivymd/KivyMD/archive/refs/heads/master.zip,Pillow==8.4.0, requests==2.28.2,aiohttp==3.8.4,aiosignal==1.3.1,async-timeout==4.0.2,attrs==22.2.0,certifi==2022.12.7,charset-normalizer==2.1.1,frozenlist==1.3.3,idna==3.4,multidict==6.0.4,tqdm==4.65.0,urllib3==1.26.15,yarl==1.8.2,loguru, dirsync



# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source.kivy = ../../kivy

# (list) Garden requirements
#garden_requirements =

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, portrait or all)
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

#
# OSX Specific
#

#
# author = © Copyright Info

# change the major version of python used by the app
osx.python_version = 3

# Kivy version to use
# osx.kivy_version = 1.9.1

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (for new android toolchain)
# Supported formats are: #RRGGBB #AARRGGBB or one of the following names:
# red, blue, green, black, white, gray, cyan, magenta, yellow, lightgray,
# darkgray, grey, lightgrey, darkgrey, aqua, fuchsia, lime, maroon, navy,
# olive, purple, silver, teal.
#android.presplash_color = #FFFFFF

# (int) Android API to use
android.api = 31

# (int) Minimum API required
#android.minapi = 9

# (int) Android SDK version to use
#android.sdk = 20

# (str) Android NDK version to use
# android.ndk = 25

# (bool) Use --private data storage (True) or --dir public storage (False)
#android.private_storage = True

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
#android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
#android.sdk_path =

# (str) ANT directory (if empty, it will be automatically downloaded.)
#android.ant_path =

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess Internet downloads or save time
# when an update is due and you just want to test/build your package
android.skip_update = True

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.renpy.android.PythonActivity

# (list) Pattern to whitelist for the whole project
#android.whitelist =

# (str) Path to a custom whitelist file
#android.whitelist_src =

# (str) Path to a custom blacklist file
#android.blacklist_src =

# (list) List of Java .jar files to add to the libs so that pyjnius can access
# their classes. Don't add jars that you do not need, since extra jars can slow
# down the build process. Allows wildcards matching, for example:
# OUYA-ODK/libs/*.jar
#android.add_jars = foo.jar,bar.jar,path/to/more/*.jar

# (list) List of Java files to add to the android project (can be java or a
# directory containing the files)
#android.add_src =

# (list) Android AAR archives to add (currently works only with sdl2_gradle
# bootstrap)
#android.add_aars =

# (list) Gradle dependencies to add (currently works only with sdl2_gradle
# bootstrap)
#android.gradle_dependencies =

# (str) python-for-android branch to use, defaults to stable
#p4a.branch = master

# (str) XML file to include as an intent filters in <activity> tag
#android.manifest.intent_filters =

# (str) launchMode to set for the main activity
android.manifest.launch_mode = standard

# (list) Android additionnal libraries to copy into libs/armeabi
#android.add_libs_armeabi = libs/android/*.so
#android.add_libs_armeabi_v7a = libs/android-v7/*.so
#android.add_libs_x86 = libs/android-x86/*.so
#android.add_libs_mips = libs/android-mips/*.so

# (bool) Indicate whether the screen should stay on
# Don't forget to add the WAKE_LOCK permission if you set this to True
#android.wakelock = False

# (list) Android application meta-data to set (key=value format)
#android.meta_data =

# (list) Android library project to add (will be added in the
# project.properties automatically.)
#android.library_references =

# (str) Android logcat filters to use
android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86
android.archs = armeabi-v7a
# arm64-v8a

#
# Python for android (p4a) specific
p4a.branch = develop

# (str) python-for-android git clone directory (if empty, it will be automatically cloned from github)
#p4a.source_dir =

# (str) The directory in which python-for-android should look for your own build recipes (if any)
#p4a.local_recipes =
p4a.local_recipes = ./recipes

# (str) Filename to the hook for p4a
#p4a.hook =

# (str) Bootstrap to use for android builds
# p4a.bootstrap = sdl2


#
# iOS specific
#

# (str) Path to a custom kivy-ios folder
#ios.kivy_ios_dir = ../kivy-ios

# (str) Name of the certificate to use for signing the debug version
# Get a list of available identities: buildozer ios list_identities
#ios.codesign.debug = "iPhone Developer: <lastname> <firstname> (<hexstring>)"

# (str) Name of the certificate to use for signing the release version
#ios.codesign.release = %(ios.codesign.debug)s

# (list) Permissions
android.permissions = ACCEPT_HANDOVER, ACCESS_BACKGROUND_LOCATION, ACCESS_CHECKIN_PROPERTIES, ACCESS_COARSE_LOCATION, ACCESS_FINE_LOCATION, ACCESS_LOCATION_EXTRA_COMMANDS, ACCESS_MEDIA_LOCATION, ACCESS_NETWORK_STATE, ACCESS_NOTIFICATION_POLICY, ACCESS_SURFACE_FLINGER, ACCESS_WIFI_STATE, ACCOUNT_MANAGER, ACTIVITY_RECOGNITION, ADD_SYSTEM_SERVICE, ADD_VOICEMAIL, ANSWER_PHONE_CALLS, AUTHENTICATE_ACCOUNTS, BATTERY_STATS, BIND_ACCESSIBILITY_SERVICE, BIND_APPWIDGET, BIND_AUTOFILL_SERVICE, BIND_CALL_REDIRECTION_SERVICE, BIND_CARRIER_MESSAGING_CLIENT_SERVICE, BIND_CARRIER_MESSAGING_SERVICE, BIND_CARRIER_SERVICES, BIND_CHOOSER_TARGET_SERVICE, BIND_CONDITION_PROVIDER_SERVICE, BIND_CONTROLS, BIND_DEVICE_ADMIN, BIND_DREAM_SERVICE, BIND_INCALL_SERVICE, BIND_INPUT_METHOD, BIND_MIDI_DEVICE_SERVICE, BIND_NFC_SERVICE, BIND_NOTIFICATION_LISTENER_SERVICE, BIND_PRINT_SERVICE, BIND_QUICK_ACCESS_WALLET_SERVICE, BIND_QUICK_SETTINGS_TILE, BIND_REMOTEVIEWS, BIND_SCREENING_SERVICE, BIND_TELECOM_CONNECTION_SERVICE, BIND_TEXT_SERVICE, BIND_TV_INPUT, BIND_VISUAL_VOICEMAIL_SERVICE, BIND_VOICE_INTERACTION, BIND_VPN_SERVICE, BIND_VR_LISTENER_SERVICE, BIND_WALLPAPER, BLUETOOTH, BLUETOOTH_ADMIN, BLUETOOTH_PRIVILEGED, BODY_SENSORS, BRICK, BROADCAST_PACKAGE_REMOVED, BROADCAST_SMS, BROADCAST_STICKY, BROADCAST_WAP_PUSH, CALL_COMPANION_APP, CALL_PHONE, CALL_PRIVILEGED, CAMERA, CAPTURE_AUDIO_OUTPUT, CAPTURE_SECURE_VIDEO_OUTPUT, CAPTURE_VIDEO_OUTPUT, CHANGE_COMPONENT_ENABLED_STATE, CHANGE_CONFIGURATION, CHANGE_NETWORK_STATE, CHANGE_WIFI_MULTICAST_STATE, CHANGE_WIFI_STATE, CLEAR_APP_CACHE, CLEAR_APP_USER_DATA, CONTROL_LOCATION_UPDATES, DELETE_CACHE_FILES, DELETE_PACKAGES, DEVICE_POWER, DIAGNOSTIC, DISABLE_KEYGUARD, DUMP, EXPAND_STATUS_BAR, FACTORY_TEST, FLASHLIGHT, FORCE_BACK, FOREGROUND_SERVICE, FOTA_UPDATE, GET_ACCOUNTS, GET_ACCOUNTS_PRIVILEGED, GET_PACKAGE_SIZE, GET_TASKS, GET_TOP_ACTIVITY_INFO, GLOBAL_SEARCH, HARDWARE_TEST, INJECT_EVENTS, INSTALL_LOCATION_PROVIDER, INSTALL_PACKAGES, INSTALL_SHORTCUT, INSTANT_APP_FOREGROUND_SERVICE, INTERNAL_SYSTEM_WINDOW, INTERNET, KILL_BACKGROUND_PROCESSES, LOADER_USAGE_STATS, LOCATION_HARDWARE, MANAGE_ACCOUNTS, MANAGE_APP_TOKENS, MANAGE_DOCUMENTS, MANAGE_OWN_CALLS, MASTER_CLEAR, MEDIA_CONTENT_CONTROL, MODIFY_AUDIO_SETTINGS, MODIFY_PHONE_STATE, MOUNT_FORMAT_FILESYSTEMS, MOUNT_UNMOUNT_FILESYSTEMS, NFC, NFC_PREFERRED_PAYMENT_INFO, NFC_TRANSACTION_EVENT, PACKAGE_USAGE_STATS, PERSISTENT_ACTIVITY, PROCESS_OUTGOING_CALLS, QUERY_ALL_PACKAGES, READ_CALENDAR, READ_CALL_LOG, READ_CONTACTS, READ_EXTERNAL_STORAGE, READ_FRAME_BUFFER, READ_HISTORY_BOOKMARKS, READ_INPUT_STATE, READ_LOGS, READ_OWNER_DATA, READ_PHONE_NUMBERS, READ_PHONE_STATE, READ_PRECISE_PHONE_STATE, READ_PROFILE, READ_SMS, READ_SOCIAL_STREAM, READ_SYNC_SETTINGS, READ_SYNC_STATS, READ_USER_DICTIONARY, READ_VOICEMAIL, REBOOT, RECEIVE_BOOT_COMPLETED, RECEIVE_MMS, RECEIVE_SMS, RECEIVE_WAP_PUSH, RECORD_AUDIO, REORDER_TASKS, REQUEST_COMPANION_RUN_IN_BACKGROUND, REQUEST_COMPANION_USE_DATA_IN_BACKGROUND, REQUEST_DELETE_PACKAGES, REQUEST_IGNORE_BATTERY_OPTIMIZATIONS, REQUEST_INSTALL_PACKAGES, REQUEST_PASSWORD_COMPLEXITY, RESTART_PACKAGES, SEND_RESPOND_VIA_MESSAGE, SEND_SMS, SET_ACTIVITY_WATCHER, SET_ALARM, SET_ALWAYS_FINISH, SET_ANIMATION_SCALE, SET_DEBUG_APP, SET_ORIENTATION, SET_POINTER_SPEED, SET_PREFERRED_APPLICATIONS, SET_PROCESS_FOREGROUND, SET_PROCESS_LIMIT, SET_TIME, SET_TIME_ZONE, SET_WALLPAPER, SET_WALLPAPER_HINTS, SIGNAL_PERSISTENT_PROCESSES, SMS_FINANCIAL_TRANSACTIONS, START_VIEW_PERMISSION_USAGE, STATUS_BAR, SUBSCRIBED_FEEDS_READ, SUBSCRIBED_FEEDS_WRITE, SYSTEM_ALERT_WINDOW, TRANSMIT_IR, UNINSTALL_SHORTCUT, UPDATE_DEVICE_STATS, USE_BIOMETRIC, USE_CREDENTIALS, USE_FINGERPRINT, USE_FULL_SCREEN_INTENT, USE_SIP, VIBRATE, WAKE_LOCK, WRITE_APN_SETTINGS, WRITE_CALENDAR, WRITE_CALL_LOG, WRITE_CONTACTS, WRITE_EXTERNAL_STORAGE, WRITE_GSERVICES, WRITE_HISTORY_BOOKMARKS, WRITE_OWNER_DATA, WRITE_PROFILE, WRITE_SECURE_SETTINGS, WRITE_SETTINGS, WRITE_SMS, WRITE_SOCIAL_STREAM, WRITE_SYNC_SETTINGS, WRITE_USER_DICTIONARY, WRITE_VOICEMAIL



[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .ipa) storage
# bin_dir = ./bin

#    -----------------------------------------------------------------------------
#    List as sections
#
#    You can define all the "list" as [section:key].
#    Each line will be considered as a option to the list.
#    Let's take [app] / source.exclude_patterns.
#    Instead of doing:
#
#[app]
#source.exclude_patterns = license,data/audio/*.wav,data/images/original/*
#
#    This can be translated into:
#
#[app:source.exclude_patterns]
#license
#data/audio/*.wav
#data/images/original/*
#


#    -----------------------------------------------------------------------------
#    Profiles
#
#    You can extend section / key with a profile
#    For example, you want to deploy a demo version of your application without
#    HD content. You could first change the title to add "(demo)" in the name
#    and extend the excluded directories to remove the HD content.
#
#[app@demo]
#title = My Application (demo)
#
#[app:source.exclude_patterns@demo]
#images/hd/*
#
#    Then, invoke the command line with the "demo" profile:
#
#buildozer --profile demo android debug
