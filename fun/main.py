from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time




def find_create_post(driver):
    footer = driver.find_element(By.CLASS_NAME, "border-top")

    driver.execute_script("arguments[0].scrollIntoView();", footer)

    # Navigate to the "Create New Post" page
    create_post = driver.find_element(By.LINK_TEXT, "Create New Post")
    time.sleep(1)
    create_post.click()
    
def populate_data(driver,number):
    title = driver.find_element(By.ID, "title")
    title.send_keys(f"Hello world{number}")

    subtitle = driver.find_element(By.ID, "subtitle")
    subtitle.send_keys("Hello world3")
    
    img_url = driver.find_element(By.ID, "img_url")
    img_url.send_keys("https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Gutenberg_Bible%2C_Lenox_Copy%2C_New_York_Public_Library%2C_2009._Pic_01.jpg/640px-Gutenberg_Bible%2C_Lenox_Copy%2C_New_York_Public_Library%2C_2009._Pic_01.jpg")


    # Wait for CKEditor to be fully loaded
    wait_for_ckeditor(driver)

    # Find the CKEditor textarea element
    ckeditor_textarea = driver.find_element(By.CSS_SELECTOR, "body.cke_editable")

    # Clear any default content (if present)
    ckeditor_textarea.send_keys(Keys.CONTROL + "a")  # Select all existing text
    ckeditor_textarea.send_keys(Keys.DELETE)         # Delete selected text

    # Send your desired text to the CKEditor
    ckeditor_textarea.send_keys(text)
    
    driver.switch_to.default_content()
    
def submit_data(driver):
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "submit"))
    )

    driver.execute_script("arguments[0].scrollIntoView();", submit_button)
    time.sleep(1)
    submit_button.click()
    
def login(driver):
    driver.get("https://angelas-blog2.onrender.com")

    # ... your login code ...
    time.sleep(1)
    driver.get("https://angelas-blog2.onrender.com")
    login = driver.find_element(By.ID, "login")

    login.click()

    email = driver.find_element(By.ID, "email")
    email.send_keys("admin@email.com")
    print("sent email")
    password = driver.find_element(By.ID, "password")
    password.send_keys("samme")
    time.sleep(2)
    driver.implicitly_wait(5)
    login2 = driver.find_element(By.ID, "submit")

    driver.execute_script("arguments[0].scrollIntoView();", login2)
    time.sleep(2)

    login2.click()
    print("Logged in")

    


text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

path = "C:\development\chromedriver.exe"

def wait_for_ckeditor(driver):
    try:
        WebDriverWait(driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe.cke_wysiwyg_frame"))
        )
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "body.cke_editable"))
        )
    except:
        print("CKEditor not fully loaded.")

def main():
    driver = webdriver.Chrome(executable_path=path)
    login(driver)
    # Wait for the new page to load completely
    time.sleep(2)
    for i in range(7,40):
        find_create_post(driver)
        populate_data(driver,i)
        submit_data(driver)
        print(f"the code has run {i} times")
        

    # Now you can interact with elements on the new page without the stale element issue

    # Fill in the title and subtitle

    time.sleep(10)
    driver.quit()
if __name__ == "__main__":
    main()
