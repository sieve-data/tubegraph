import os

from playwright.sync_api import sync_playwright


def get_storyboard_urls(video_id):
    # Load javascript
    script_path = os.path.join(os.path.dirname(__file__), "storyboard_extractor.js")
    with open(script_path, "r") as f:
        js_code = f.read()

    # Run playwright
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            page.goto(f"https://www.youtube.com/watch?v={video_id}")
            storyboard_urls = page.evaluate(js_code)
            if storyboard_urls is None or storyboard_urls == "":
                raise ValueError(
                    f"Failed to fetch storyboard URL for {video_id}\nValue returned: {storyboard_urls}"
                )
            return storyboard_urls
        except Exception as e:
            print(f"Error fetching storyboard URL: {e}")
            raise e
        finally:
            browser.close()


print(get_storyboard_urls("nr0RPVvKWDI"))
