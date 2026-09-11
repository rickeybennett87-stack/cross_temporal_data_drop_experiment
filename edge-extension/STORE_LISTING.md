# Microsoft Edge Add-ons listing draft

## Name
CTIS Existing-Tab Bridge

## Short description
Connect a CTIS page to ChatGPT and Claude tabs that you already opened yourself, without opening or navigating those services.

## Full description
CTIS Existing-Tab Bridge is a local browser extension for users of the Cross-Temporal Interaction Space (CTIS). It connects the CTIS web interface to ChatGPT and Claude pages that the user has already opened and authenticated in Microsoft Edge.

The extension does not create ChatGPT or Claude tabs, navigate those services, log in, handle authentication, solve challenges, bypass Cloudflare, or interact with security verification pages. If a challenge or security page is detected, the extension refuses to act.

When the user sends a message from the CTIS interface, the extension locates matching tabs that are already open, places the message into the visible chat composer, and uses the normal send control on that already-open page. This allows the user to keep CTIS as the primary workspace while preserving their existing browser sessions.

The extension only requests access to the specific sites it needs: chatgpt.com, claude.ai, and the CTIS GitHub Pages site. It does not collect analytics, sell data, transmit browsing history, or send credentials to a third party.

## Category
Productivity

## Search terms
CTIS, ChatGPT, Claude, multi-model, browser bridge, AI workspace

## Suggested certification notes
1. Open ChatGPT manually in Edge and sign in normally.
2. Open Claude manually in Edge and sign in normally.
3. Open the CTIS GitHub Pages site.
4. The CTIS Existing-Tab Bridge panel reports whether already-open ChatGPT and Claude tabs are present.
5. Enter text in the CTIS bridge and choose a target.
6. The extension fills and submits the message only in already-open tabs.
7. Close the ChatGPT or Claude tab and repeat. The extension does not recreate or navigate to the missing tab.
8. Present a challenge/security page if available in a test environment. The extension should take no action and return a refusal status.

## Availability
Recommended: Public, all markets unless the publisher has a reason to restrict distribution.
