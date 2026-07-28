#!/usr/bin/env python3
"""
Custom PPT screenshot capture.
Uses the cached Chromium headless-shell (build 1224) directly via executable_path
to avoid the slow Playwright 1.61 browser download.
"""
import os
import sys
from pathlib import Path

CHROME_PATH = "/Users/hongyangchun/Library/Caches/ms-playwright/chromium_headless_shell-1224/chrome-headless-shell-mac-arm64/chrome-headless-shell"
URL = "http://localhost:5173"
OUTPUT_DIR = "/Users/hongyangchun/Codebase/default/outputs/gmmt-ppt/frontend/public/assets/images/posters/pages"
TOTAL_PAGES = 23

def main():
    from playwright.sync_api import sync_playwright

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    screenshots = []

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            executable_path=CHROME_PATH,
            args=["--no-sandbox", "--disable-dev-shm-usage"],
        )
        context = browser.new_context(
            viewport={"width": 1440, "height": 810},
            device_scale_factor=2,
        )
        page = context.new_page()
        page.on("console", lambda msg: None)  # silence noise

        for i in range(1, TOTAL_PAGES + 1):
            sys.stdout.write(f"  Capturing slide {i}/{TOTAL_PAGES}...\n")
            sys.stdout.flush()
            page.goto(f"{URL}?page={i}", wait_until="load")
            # Wait for the slide content to be injected into #ppt-viewport
            try:
                page.wait_for_selector("#ppt-viewport > *", timeout=8000)
            except Exception:
                pass
            # Give fonts / CSS a moment to settle
            try:
                page.evaluate("() => document.fonts && document.fonts.ready")
            except Exception:
                pass
            page.wait_for_timeout(700)
            out_path = os.path.join(OUTPUT_DIR, f"page-{i}.png")
            try:
                page.locator("#ppt-viewport").screenshot(path=out_path)
            except Exception:
                page.screenshot(
                    path=out_path,
                    clip={"x": 0, "y": 0, "width": 1440, "height": 810},
                )
            screenshots.append(out_path)

        browser.close()

    print(f"\nCaptured {len(screenshots)} slides to {OUTPUT_DIR}")
    for s in screenshots:
        print(f"  {s}  ({os.path.getsize(s)} bytes)")

if __name__ == "__main__":
    main()
