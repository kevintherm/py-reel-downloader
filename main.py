from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from requests import get

mobile_emulation = { "deviceName": "iPhone 12 Pro" }
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
chrome_options.add_argument("--headless")
chrome_options.add_argument("--log-level=3")
driver = webdriver.Chrome(options=chrome_options)

# user_agent = "Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16"

# opts = webdriver.FirefoxOptions()
# opts.add_argument("--headless")
# opts.set_preference("general.useragent.override", f"userAgent={user_agent}")
# driver = webdriver.Firefox(options=opts)


url = input("Masukkan URL Reel: ")

while not url:
    print("Reel downloader v1", end='\r')
    url = input("Masukkan URL Reel: ")
    
    

driver.get(
    url)
WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "video"))
    )

vid_url = driver.find_element(By.TAG_NAME, 'video').get_attribute('src')
driver.close()

# print(vid_url)

if (vid_url) and not vid_url.startswith("blob"):
    print("Video URL Obtained, download will start soon...\n")
    r = get(vid_url, stream=True)

    if r.status_code == 200:
        
        
        filename = input("File Name: ") or "video.mp4"

        if not filename.endswith(".mp4"):
            filename=filename+".mp4"

        with open(f".\output\{filename}", 'wb') as f:
            print("Download Start", end='\r')

            # dwnlod chunk 1 mb
            for chunk in r.iter_content(chunk_size=1024*1024):
                if chunk:
                    print("Downloading...", end="\r")
                    f.write(chunk)

            print(f"Download Finished: {filename}")
    else:
        print("Failed to fetch video. Check internet connection")

else:
    print("Failed to Obtain Video URL")