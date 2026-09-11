# CTIS Existing-Tab Bridge Privacy Disclosure

CTIS Existing-Tab Bridge is designed to operate locally in Microsoft Edge.

## Data the extension can access

The extension can access pages on:

- `https://chatgpt.com/*`
- `https://claude.ai/*`
- `https://rickeybennett87-stack.github.io/*`

It uses this access only to locate user-opened ChatGPT and Claude tabs, interact with their existing message composers, and expose bridge controls on the CTIS page.

## Data collection

The extension does not include analytics, advertising, telemetry, tracking pixels, or third-party SDKs. It does not sell personal data. It does not intentionally collect credentials, cookies, authentication tokens, browsing history, or unrelated page content.

## Network behavior

The extension itself does not make independent network requests to ChatGPT or Claude APIs. It operates through the user's already-open browser pages. It does not create tabs, navigate to services, log in, solve challenges, bypass Cloudflare, or manipulate authentication/security pages.

## Message handling

Text entered into the CTIS bridge can be placed into and submitted through an already-open model chat composer selected by the user. That message is then handled by the destination website according to that service's own terms and privacy practices.

## Security-page behavior

If the extension detects common challenge/security-page indicators, it refuses to automate the page.

## Storage

Version 0.2.0 requests browser storage permission for local extension state. No remote synchronization or analytics endpoint is implemented by the extension.

## Contact and source

The extension source is maintained in the public `cross_temporal_data_drop_experiment` GitHub repository. Issues and source review can be handled through the repository.
