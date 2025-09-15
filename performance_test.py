#!/usr/bin/env python3

import sys
import os
import asyncio
import time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from playwright.async_api import async_playwright
from weblite import PlaywrightPage

async def test_performance():
    print("Testing to_weblite performance...")

    playwright_ctx = await async_playwright().start()
    browser = await playwright_ctx.chromium.launch(headless=True)
    page = await browser.new_page()

    # Test on Google (complex page)
    await page.goto("https://google.com")
    await page.wait_for_load_state("networkidle")

    web_page = PlaywrightPage(page)

    # Time the conversion
    start_time = time.time()
    element = await web_page.to_weblite()
    end_time = time.time()

    duration = end_time - start_time
    print(f"to_weblite took: {duration:.3f} seconds")

    if element:
        result = element.to_dict(collapse_wrappers=True)
        print(f"Generated {len(str(result))} characters of output")

    await browser.close()
    await playwright_ctx.stop()

    return duration

if __name__ == "__main__":
    duration = asyncio.run(test_performance())
    print(f"Total time: {duration:.3f}s")