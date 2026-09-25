# Installing DroidCam on Linux

- Source: `/home/jadedjade/Documents/copilot-activity-history.csv`
- Source CSV rows: 9532-9541
- Exported messages: 10
- Earliest timestamp: 2025-09-29T15:41:31
- Latest timestamp: 2025-09-29T16:46:14
- Reconstruction: contiguous title run; timestamps ascending; Human before AI for equal timestamps

## Human — 2025-09-29T15:41:31

<!-- source_csv_row: 9541 -->
DROID CAM FOR LINUX CAN YOU WALK ME THROUGH GETITING THE REPO AND INSTALLING IT

## AI — 2025-09-29T15:41:31

<!-- source_csv_row: 9540 -->
Absolutely, Rickey. Here's a step-by-step guide to getting the DroidCam Linux client repo and installing it from source:

---

## 🛠️ Step-by-Step: Install DroidCam on Linux

### 1. 📦 Clone the GitHub Repository
Open a terminal and run:
```bash
git clone https://github.com/dev47apps/droidcam-linux-client.git
cd droidcam-linux-client
```

### 2. 📚 Install Dependencies
Depending on your distro, install the required packages:

**For Debian/Ubuntu:**
```bash
sudo apt update
sudo apt install libavutil-dev libswscale-dev libasound2-dev libspeex-dev libusbmuxd-dev libplist-dev libturbojpeg0-dev \
libgtk-3-dev libayatana-appindicator3-dev linux-headers-$(uname -r) gcc make
```

**For Fedora:**
```bash
sudo dnf install libavutil-free-devel libswscale-free-devel alsa-lib-devel speex-devel libusbmuxd-devel libplist-devel turbojpeg-devel \
gtk3-devel libappindicator-gtk3-devel kernel-devel gcc make
```

### 3. 🧱 Build the Client
To build both GUI and CLI:
```bash
make
```
To build CLI only (no GTK):
```bash
make droidcam-cli
```

### 4. 🚀 Install the Client
Run the install script:
```bash
sudo ./install-client
```

### 5. 🎥 Install the Webcam Driver
Install the v4l2loopback module:
```bash
sudo ./install-dkms
```
To set a custom resolution (e.g., 1920x1080):
```bash
sudo ./install-dkms 1920 1080
```

### 6. 🔊 (Optional) Enable USB Support
If you want to connect via USB:
```bash
sudo apt install usbmuxd
sudo systemctl start usbmuxd
```

---

Once installed, launch DroidCam from your app menu or run `droidcam` from the terminal. Connect your phone and Linux machine to the same network or via USB, and you’re good to go.

Want help configuring OBS or testing the webcam feed next?

## Human — 2025-09-29T16:43:27

<!-- source_csv_row: 9539 -->
┌──(root㉿OiOi)-[~/droidcam-linux-client]
└─# make          

cc   src/droidcam-cli.c src/connection.c src/settings.c src/decoder.c src/decoder_snd.c src/decoder_v4l2.c src/av.c src/usb.c src/queue.c -o droidcam-cli  `pkg-config --libs --cflags libswscale libavutil` `pkg-config --libs --cflags libturbojpeg` `pkg-config --libs --cflags libusbmuxd` -lspeex -lasound -lpthread -lm
Package libusbmuxd was not found in the pkg-config search path.
Perhaps you should add the directory containing `libusbmuxd.pc'
to the PKG_CONFIG_PATH environment variable
Package 'libusbmuxd', required by 'virtual:world', not found
/usr/bin/ld: /tmp/ccl9f5Ig.o: in function `CheckiOSDevices':
usb.c:(.text+0x356): undefined reference to `usbmuxd_get_device_list'
/usr/bin/ld: usb.c:(.text+0x37b): undefined reference to `usbmuxd_device_list_free'
/usr/bin/ld: usb.c:(.text+0x397): undefined reference to `usbmuxd_connect'
/usr/bin/ld: usb.c:(.text+0x3ac): undefined reference to `usbmuxd_device_list_free'
/usr/bin/ld: usb.c:(.text+0x3f9): undefined reference to `usbmuxd_device_list_free'
collect2: error: ld returned 1 exit status
make: *** [Makefile:74: droidcam-cli] Error 1
                                                                                                                                                 
┌──(root㉿OiOi)-[~/droidcam-linux-client]
└─#

## AI — 2025-09-29T16:43:27

<!-- source_csv_row: 9538 -->
You're hitting a linker error because the build process can't find the `libusbmuxd` development files. That library handles USB connections to iOS devices, and DroidCam optionally supports that. Here's how to fix it:

---

## 🧩 Fixing the `libusbmuxd` Build Error

### 🔍 Step 1: Install the Development Package

On **Debian/Ubuntu**, run:
```bash
sudo apt install libusbmuxd-dev
```

On **Fedora**, use:
```bash
sudo dnf install libusbmuxd-devel
```

This installs both the library and the `.pc` file needed by `pkg-config`.

---

### 🧼 Step 2: Clean and Rebuild

After installing the missing package:
```bash
make clean
make
```

If you still get the `pkg-config` error, you might need to manually set the path:

```bash
export PKG_CONFIG_PATH=/usr/lib/pkgconfig:/usr/local/lib/pkgconfig
make
```

You can also skip USB support entirely if you don’t need iOS USB connections. To build without it:

```bash
make droidcam-cli
```

This compiles the CLI without the GTK GUI and skips USB support.

---

Let me know if you want to strip out USB support entirely from the source or patch the Makefile to avoid this dependency. I can walk you through that too.

## Human — 2025-09-29T16:44:33

<!-- source_csv_row: 9537 -->
└─# sudo apt install libusbmuxd-dev

libusbmuxd-dev is already the newest version (2.1.0-1+b1).
The following package was automatically installed and is no longer required:
  libx264-164
Use 'sudo apt autoremove' to remove it.

Summary:
  Upgrading: 0, Installing: 0, Removing: 0, Not Upgrading: 354
                                                                                                                                                 
┌──(root㉿OiOi)-[~/droidcam-linux-client]

## AI — 2025-09-29T16:44:33

<!-- source_csv_row: 9536 -->
Perfect, Rickey — that confirms the dev package is installed. But the linker still can't find `libusbmuxd.pc`, which means `pkg-config` isn’t locating it properly. Let’s fix that manually:

---

## 🧭 Step-by-Step: Fix `pkg-config` for `libusbmuxd`

### 1. 🔍 Locate the `.pc` File
Run:
```bash
find /usr -name 'libusbmuxd.pc'
```

You’ll likely see something like:
```
/usr/lib/x86_64-linux-gnu/pkgconfig/libusbmuxd.pc
```

### 2. 🛠️ Export the Path
Set the environment variable so `pkg-config` can find it:
```bash
export PKG_CONFIG_PATH=/usr/lib/x86_64-linux-gnu/pkgconfig
```

You can verify:
```bash
pkg-config --modversion libusbmuxd
```
If it returns `2.1.0`, you’re good.

### 3. 🔁 Rebuild
Now try:
```bash
make clean
make
```

---

If you want to permanently fix this for your shell, add the export line to your `.bashrc` or `.zshrc`:
```bash
echo 'export PKG_CONFIG_PATH=/usr/lib/x86_64-linux-gnu/pkgconfig' >> ~/.bashrc
source ~/.bashrc
```

Let me know if you want to patch the Makefile to skip USB support entirely — I can walk you through that too.

## Human — 2025-09-29T16:45:50

<!-- source_csv_row: 9535 -->
it just hung didn do anything

## AI — 2025-09-29T16:45:50

<!-- source_csv_row: 9534 -->
Got it — sounds like `pkg-config --modversion libusbmuxd` didn’t return anything, which means it’s still not locating the `.pc` file. Let’s go deeper and fix this cleanly:

---

## 🧪 Diagnose and Patch `pkg-config` for `libusbmuxd`

### 🔍 Step 1: Confirm the `.pc` File Exists
Run this:
```bash
find /usr -name 'libusbmuxd.pc'
```

If it returns nothing, the dev package might be misinstalled or broken. If it returns a path like:
```
/usr/lib/x86_64-linux-gnu/pkgconfig/libusbmuxd.pc
```
then we’re good — move to step 2.

---

### 🧭 Step 2: Temporarily Set the Path
Run:
```bash
export PKG_CONFIG_PATH=/usr/lib/x86_64-linux-gnu/pkgconfig
```

Then test:
```bash
pkg-config --modversion libusbmuxd
```

If it still hangs, try:
```bash
strace pkg-config --modversion libusbmuxd
```

This will show where it’s looking and where it’s failing. If it’s stuck on a missing socket or file, we can bypass it.

---

### 🧼 Step 3: Bypass USB Support (if needed)
If you don’t need iOS USB support, patch the Makefile to skip `libusbmuxd`:

#### 🔧 Edit `Makefile`
Open it in your editor and find the line with:
```make
`pkg-config --libs --cflags libusbmuxd`
```

Delete that part entirely, or comment it out:
```make
# `pkg-config --libs --cflags libusbmuxd`
```

Also remove any `-lusbmuxd` from the linker flags.

Then rebuild:
```bash
make clean
make
```

---

Let me know if you want to keep USB support — I can walk you through manually linking the library without `pkg-config`. Or we can strip it out entirely and simplify the build. Your call.

## Human — 2025-09-29T16:46:14

<!-- source_csv_row: 9533 -->
no find didnt do anythi

## AI — 2025-09-29T16:46:14

<!-- source_csv_row: 9532 -->
Understood. If `find /usr -name 'libusbmuxd.pc'` returns nothing, then the `.pc` file for `libusbmuxd` is missing — even though the dev package claims to be installed. That’s a packaging issue. Let’s bypass it cleanly.

---

## 🧼 Option 1: Strip USB Support from the Build

If you don’t need iOS USB support, here’s how to patch the Makefile:

### 🔧 Edit the Makefile
Open `Makefile` in your editor and find this line (around line 74):
```make
`pkg-config --libs --cflags libusbmuxd`
```

Delete it or comment it out:
```make
# `pkg-config --libs --cflags libusbmuxd`
```

Also remove any `-lusbmuxd` from the linker flags:
```make
-lspeex -lasound -lpthread -lm
```

Save and exit.

### 🔁 Rebuild
```bash
make clean
make
```

This will compile without USB support — which is fine unless you’re connecting an iPhone via USB.

---

## 🧩 Option 2: Manually Link Without `pkg-config`

If you want to keep USB support, we can manually add the include and lib paths. First, find the headers and library:

```bash
dpkg -L libusbmuxd-dev | grep '\.h'
dpkg -L libusbmuxd-dev | grep '\.so'
```

Then modify the Makefile to add:
```make
-I/usr/include/usbmuxd -L/usr/lib/x86_64-linux-gnu -lusbmuxd
```

But unless you’re actively using USB with iOS, stripping it is cleaner.

---

Let me know if you want to patch the source itself to remove USB logic entirely — I can walk you through that too.
