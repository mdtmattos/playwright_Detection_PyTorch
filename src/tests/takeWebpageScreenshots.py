from playwright.sync_api import sync_playwright
import os

# Function to capture the screenshot
def capture_screenshot(url, save_path):
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=True)  # True to not show the browser
        page = browser.new_page()

        # Navigate to the URL
        page.goto(url)

        # Take the screenshot
        page.screenshot(path=save_path)
        print(f"Screenshot taken and saved to {save_path}")

        # Close the browser
        browser.close()

# URL of the page you want to capture
url = "https://www.google.com/search?sca_esv=115fbc7a5c2d88aa&sxsrf=ADLYWIKKax1Sll7oN-MxjrxTC-ibaVjJVA:1737579986449&q=fotos+de+pessoas&udm=2&fbs=AEQNm0A_ElqRadfJ052eEZYKSIj__pYFaFHKdnGcO42W-poa4hqiqoSrkT7Gbj0jEa1XXHcpOVXJg6GWUM39QIGoNHiolJF6R_HI7vN-ARaK4Agzx2OFtr8rBZ4dWs9BMuz70G1qAVFA6xk5cCJgFuifVKBmANe5ifBDoDvn4NvufxhzBuNkKEx_JpVLaef-3ibJK_qC3VUhpQG8qyyk_VWfRQevcXn7CA&sa=X&ved=2ahUKEwjCvvHunYqLAxXsIbkGHRMsLkcQtKgLegQIExAB&biw=1536&bih=791&dpr=1.25"

# Define the path to save the screenshot
save_path = "screenshots/webpageImage.png"

# Ensure the screenshots folder exists
os.makedirs(os.path.dirname(save_path), exist_ok=True)

# Capture and save the screenshot
capture_screenshot(url, save_path)

# Check if the file was saved
if os.path.exists(save_path):
    print(f"File successfully saved at {save_path}")
else:
    print(f"Error: File not found at {save_path}")
