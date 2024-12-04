#程式碼皆為原創，僅使用chatgpt偵錯
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
def get_content(driver, file):
    try:
        title = driver.find_element(By.CLASS_NAME, "page-header")
        sub_title = driver.find_element(By.CLASS_NAME, "content-summary")
        article = driver.find_element(By.XPATH, "//*[@id=\"node-152373\"]/div/div/div/div[3]/div/div")
        paragraphs = article.find_elements(By.TAG_NAME, "p")
            
        # 將標題和段落寫入文件
        file.write(f"title: {title.text}\n")
        file.write(f"subtitle: {sub_title.text}\n\n")
        for i in paragraphs:
            file.write(f"{i.text}\n")
        print("done")
    except Exception as e:
        file.write(f"Error: {str(e)}\n")

def main(): #初始設定
    driver = webdriver.Chrome()
    driver.get("https://www.ithome.com.tw/news/152373")
    time.sleep(3)
    
    with open("output_a.txt", "w", encoding="utf-8") as file:
        get_content(driver, file)

    driver.close()

if __name__ == "__main__":
    main()

