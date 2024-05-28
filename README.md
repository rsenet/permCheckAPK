# About permCheckAPK

**permCheckAPK** was written to identify permission used on Android application.

## Usage

Print the help to get all necessary information

```bash
$ python3 permCheckAPK.py -h
usage: permCheckAPK.py [-h] [--device DEVICE] [--list] [--perm PERM]

Android Application Permission Checker

optional arguments:
  -h, --help       show this help message and exit
  --device DEVICE  Specify the device
  --list           List all user installed applications
  --bundle         List all permissions for a specific application using bundle id
  --perm PERM      Return applications with the specified permission
```

Without argument (except the device which is mandatory), all permission from all application will be displayed:

```bash
$ python3 permCheckAPK.py --device emulator-5554

[x] 'com.domobile.applock' has the following permission
 - LEGACY_STORAGE
 - SYSTEM_ALERT_WINDOW
 - TOAST_WINDOW
 - READ_EXTERNAL_STORAGE
 - WRITE_EXTERNAL_STORAGE
 - RUN_IN_BACKGROUND
 - START_FOREGROUND

[x] 'com.scottyab.rootbeer.sample' has the following permission
 - No operations.
```

But, it is also possible to get all application with a specific permission by using **--perm**.

```bash
$ python3 permCheckAPK.py --device emulator-5554 --perm WRITE_EXTERNAL_STORAGE

[x] 'com.domobile.applock' has the following permission
 - LEGACY_STORAGE
 - SYSTEM_ALERT_WINDOW
 - TOAST_WINDOW
 - READ_EXTERNAL_STORAGE
 - WRITE_EXTERNAL_STORAGE
 - RUN_IN_BACKGROUND
 - START_FOREGROUND

[x] 'com.Nubapp.Resawod' has the following permission
 - READ_EXTERNAL_STORAGE
 - WRITE_EXTERNAL_STORAGE
 - LEGACY_STORAGE
 - SYSTEM_ALERT_WINDOW
 - WAKE_LOCK
```

## Enable USB-Debugging

### Via GUI:

Go to **Settings** > **About phone** and press on **build number** 7 times to enable developper mode.

Once enabled, go to **Settings** > **Developer options** and enable **USB debugging**


### Via ADB:

```bash
adb shell settings put global development_settings_enabled 1
adb shell setprop persist.service.adb.enable 1
```


## Author

Régis SENET ([rsenet](https://github.com/rsenet))


## Contributing

Bug reports and pull requests are welcome on [GitHub](https://github.com/rsenet/permCheckAPK).

## License

The project is available as open source under the terms of the [GPLv3](https://www.gnu.org/licenses/quick-guide-gplv3.en.html)
