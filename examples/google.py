#!/usr/bin/env python3

import sys
import os
import asyncio
import time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from playwright.async_api import async_playwright
from weblite.adapters.playwright import PlaywrightPage, PlaywrightElement
from weblite.tree import build_tree, prune_display_tree
from weblite.utils import to_compact_json, to_markdown, to_tree

async def test_google():
    total_start = time.time()
    
    print("Loading Google.com...")
    
    # Step 1: Browser setup
    step_start = time.time()
    playwright_ctx = await async_playwright().start()
    browser = await playwright_ctx.chromium.launch(headless=True)
    
    # Create page with realistic user agent and settings
    page = await browser.new_page(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        viewport={"width": 1920, "height": 1080}
    )
    
    # Set additional headers to appear more like a real browser
    await page.set_extra_http_headers({
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
    })
    print(f"Browser setup: {time.time() - step_start:.2f}s")
    
    # Step 2: Navigate to Google
    step_start = time.time()
    await page.goto("https://google.com")
    await page.wait_for_load_state("networkidle")
    print(f"Page load: {time.time() - step_start:.2f}s")
    
    # Step 3: Wrap in our interface
    step_start = time.time()
    web_page = PlaywrightPage(page)
    root_element = web_page.get_root_element()
    print(f"Interface setup: {time.time() - step_start:.2f}s")
    
    print("Google.com loaded!")
    
    # Step 4: Build tree
    step_start = time.time()
    tree = await build_tree(root_element)
    print(f"Build tree: {time.time() - step_start:.2f}s")
    
    # Step 5: Convert to display tree
    step_start = time.time()
    if tree:
        display = tree.to_display()
    else:
        display = None
    print(f"To display: {time.time() - step_start:.2f}s")
    
    # Step 6: Prune display tree
    step_start = time.time()
    if display:
        pruned_display = prune_display_tree(display)
    else:
        pruned_display = None
    print(f"Prune display: {time.time() - step_start:.2f}s")
    
    # Step 7: Convert to dict
    step_start = time.time()
    if pruned_display:
        result = pruned_display.to_dict()
    else:
        result = {}
    print(f"To dict: {time.time() - step_start:.2f}s")
    
    print("\nParse result:")
    print(to_compact_json(result))
    
    # Cleanup: Close browser
    step_start = time.time()
    await browser.close()
    await playwright_ctx.stop()
    print(f"Browser cleanup: {time.time() - step_start:.2f}s")
    
    print(f"Total time: {time.time() - total_start:.2f}s")
    print("\nBrowser closed!")
    
    return result

if __name__ == "__main__":
    result = asyncio.run(test_google())
    print("Google test completed!")