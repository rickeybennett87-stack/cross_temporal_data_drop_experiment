# Accessing PC Projects on Mobile

- Conversation ID: `6ff9bad6-7737-4db7-8086-37841920fbe9`
- User ID: `6e14f714-1808-4d85-b363-3eaf83ed51b7`
- Created: 2025-11-21T12:29:26.834607Z
- Modified: 2025-11-21T12:30:36.858741Z
- Source: d1147757-bd15-428e-a265-6f1310816d48.zip / prod-grok-backend.json
- Message count: 4

---

## Jade (human)

- Message ID: `7b3b3f5c-6999-4a76-adbb-ea96b7c037e6`
- Timestamp: 2025-11-21T12:29:26.853000Z
- Model: grok-4-auto

how do i access a project on Mobile i set it up on pc

---

## Grok (assistant)

- Message ID: `3df20f33-44d6-4d30-a8a2-6d8a6f0c3257`
- Timestamp: 2025-11-21T12:29:40.231000Z
- Model: grok-3
- Parent response ID: `7b3b3f5c-6999-4a76-adbb-ea96b7c037e6`

To access a project you created on PC from your mobile device, it depends on which platform or tool you're using. Here are the most common cases and how to access them on mobile:

### 1. **Groq (groq.com)**
- You need to log in with the **same account** on mobile.
- Mobile access: Use the Groq mobile app (iOS/Android) or go to groq.com in your phone browser.
- Your projects and chats automatically sync if you're logged into the same account.

### 2. **Cursor / VS Code with project sync**
- If you're using Cursor or VS Code with GitHub/Git sync:
  - Make sure your project is pushed to GitHub, GitLab, or Bitbucket.
  - On mobile: Use apps like **GitHub Mobile**, **GitLab Mobile**, or **Working Copy** (iOS) / **Termux + git** (Android) to pull the project.
  - For editing: Use mobile code editors like **Pockets** (iOS), **Acode**, or **Spck Editor** (Android).

### 3. **Replit**
- Log in to replit.com in your mobile browser or use the Replit mobile app.
- All your projects appear automatically if using the same account.

### 4. **CodePen / JSFiddle / Glitch**
- Just go to the website on mobile and log in → your projects are there.

### 5. **Local project (not on cloud)**
- If the project is only on your PC (not uploaded anywhere):
  - Upload it to GitHub/GitLab/Bitbucket/Dropbox/Google Drive first.
  - Or use remote access tools like:
    - **Tailscale** or **ZeroTier** (access your PC remotely)
    - **Chrome Remote Desktop**
    - **Microsoft Remote Desktop** (if on Windows)

### 6. **Notion / FigJam / Figma projects**
- Just open the app or website on mobile and log in → everything syncs.

### Quick checklist:
- Are you logged in with the **same account** on mobile?
- Is the project saved to the cloud (GitHub, Replit, etc.)?
- Did you push/commit your changes on PC?

Tell me which exact tool or platform you used on PC (e.g., Cursor, Groq, Replit, local folder, etc.), and I’ll give you the exact steps for mobile! 😊

---

## Jade (human)

- Message ID: `d631c8be-efdd-4950-ab43-453829817db4`
- Timestamp: 2025-11-21T12:30:26.981000Z
- Model: grok-4-auto
- Parent response ID: `3df20f33-44d6-4d30-a8a2-6d8a6f0c3257`

i see no project listing in my sidebar will i have to open it on mobile browser desktop store or....

---

## Grok (assistant)

- Message ID: `0893c4c2-90bb-4368-81f5-d20761170ddd`
- Timestamp: 2025-11-21T12:30:36.858000Z
- Model: grok-3
- Parent response ID: `d631c8be-efdd-4950-ab43-453829817db4`

It sounds like you’re using **Groq.com** (the Groq chat + Projects feature), because you mentioned a “sidebar” and that you created the project on PC.

Here’s exactly what’s happening and how to fix it:

### On mobile right now, Groq Projects are **only visible in the desktop/browser version**, not in the mobile apps yet.
- Groq iOS/Android apps → You will **not** see your Projects in the sidebar (as of November 2025).  
- Mobile browser (Safari/Chrome) in **Desktop mode** → You **will** see your projects.

### How to access your project on mobile right now:
1. Open **Safari** (iOS) or **Chrome** (Android) on your phone.
2. Go to https://groq.com
3. Log in with the same account you used on PC.
4. **Turn on Desktop mode / Request Desktop Site**  
   - iOS Safari: Tap the “aA” icon → “Request Desktop Website”  
   - Android Chrome: Tap the three dots → “Desktop site”
5. Once the desktop version loads, look at the left sidebar → your Projects folder will now appear exactly like on PC.
6. Tap your project → everything is there (files, instructions, chat history).

That’s the current workaround until Groq adds full Projects support to the mobile apps (they’re working on it, but it’s not there yet).

If you try this and still don’t see the Projects folder in desktop mode on mobile, let me know and I’ll walk you through clearing cache or checking if the project actually saved correctly.

---

