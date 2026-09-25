# Setting Up Android App Build on Shadow PC

- Source: `/home/jadedjade/Documents/copilot-activity-history.csv`
- Source CSV rows: 4222-4223
- Exported messages: 2
- Earliest timestamp: 2025-12-05T20:04:23
- Latest timestamp: 2025-12-05T20:04:23
- Reconstruction: contiguous title run; timestamps ascending; Human before AI for equal timestamps

## Human — 2025-12-05T20:04:23

<!-- source_csv_row: 4223 -->
ok i finally have my chromebook and so i have access to my shadow pc on a laptop sized interface now lets fix this android app in powershell or teach me how to do it from the ground up inside the android sdk windows app i have all the files i just need to put them in the right place and then make sure i have the right version jdk21 of java and the right android sdk for the app

## AI — 2025-12-05T20:04:23

<!-- source_csv_row: 4222 -->
Perfect — now that you’ve got your Chromebook running Shadow PC with a full Windows interface, you can treat it like a standard dev machine. Let’s walk through this step by step so you can either use **PowerShell** or the **Android SDK tools** directly to get your app building cleanly.

---

## 🛠 Step 1: Verify Java (JDK 21)
Your project requires **Java 21**. Let’s confirm:

```powershell
java -version
```

Expected output should look like:
```
openjdk version "21" ...
```

If it shows an older version:
1. Download [OpenJDK 21](https://jdk.java.net/21/) or install via [Adoptium](https://adoptium.net/).
2. Install it, then set environment variables in PowerShell:

```powershell
setx JAVA_HOME "C:\Program Files\Java\jdk-21"
setx PATH "%JAVA_HOME%\bin;%PATH%"
```

Close and reopen PowerShell, then re-run `java -version`.

---

## 📦 Step 2: Install Android SDK (API 35)
Your compliance docs require **Android SDK 35 (Android 15)**.

1. Install **Android Studio Hedgehog (2023.1.1+)**.
2. Open **SDK Manager** → install:
   - **Android 15 (API Level 35)**
   - **Android SDK Platform-Tools**
   - **Android SDK Build-Tools (35.x)**
3. Verify with PowerShell:

```powershell
sdkmanager --list
```

You should see `platforms;android-35` and `build-tools;35.x.x`.

---

## 📂 Step 3: Place Your Files
From your asset integration doc, the structure should look like:

```
SurvivalMergeKingdom_PlayStore2025/
├── app/
│   └── src/main/
│       ├── res/
│       │   ├── drawable/   (images)
│       │   ├── raw/        (audio)
│       │   ├── mipmap-*/   (icons)
│       └── assets/         (video)
```

Make sure:
- All **31 PNGs** are in `res/drawable/`
- All **5 OGGs** are in `res/raw/`
- `intro.mp4` is in `assets/`
- Launcher icons are in `mipmap-*`
- `play_store_icon_512.png` is at project root

---

## ⚙️ Step 4: Build with Gradle
Navigate to your project root:

```powershell
cd C:\path\to\SurvivalMergeKingdom_PlayStore2025
.\gradlew clean
.\gradlew bundleRelease
```

This will generate:
```
app/build/outputs/bundle/release/app-release.aab
```

---

## 🔍 Step 5: Verify Compliance
Run quick checks in PowerShell:

```powershell
# Target SDK
Select-String -Path "app\build.gradle" -Pattern "targetSdk"

# Billing library
Select-String -Path "app\build.gradle" -Pattern "billing:7"

# Versioning
Select-String -Path "app\build.gradle" -Pattern "versionCode|versionName"
```

---

## 🚀 Step 6: Test on Emulator
1. In Android Studio, create an **Android 15 emulator**.
2. Install debug build:

```powershell
.\gradlew installDebug
```

---

✅ If all of this runs without errors, you’ll have a **Google Play–ready AAB**. From there, you just upload it in Play Console following your submission guide.

---

Would you like me to write you a **PowerShell script** that automates all these steps (checking JDK, SDK, copying assets, building AAB), so you can run it in one go on your Shadow PC?
