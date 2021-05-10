from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path='chromedriver.exe',options=chrome_options)

driver.get('https://www.google.com/')

length_min = 1 # enter how many mins

timer = (length_min * 6)

whitelist = []

tabs = {
    driver.window_handles[0]: 50000
}

while True:
    time.sleep(10)
    
    # Remove any whitelist windows that not open
    try:
        for index in range(len(whitelist)):
            if whitelist[index] not in driver.window_handles:
                whitelist.pop(index)
    except IndexError:
        pass
    
    print(f"Whitelist: {len(whitelist)}")

    for handles in driver.window_handles:
        # Check whitelist size
        if len(whitelist) < 3:
            # Check if tabs in whitelist
            if handles not in whitelist:
                whitelist.append(handles)
                tabs[handles] = timer

        # Check if window is in the tabs
        # if not give it x amount of min 
        if handles not in tabs:
            tabs[handles] = timer
        else:
            # Check if timer is 0
            if tabs[handles] > 0:
                # If the window is not whitelisted decrease the timer
                if handles not in whitelist:
                    tabs[handles] -= 1
                print(f"{handles}:")
                print(tabs[handles])
            else:
                # Remove from tab dictionary and close tab
                tabs.pop(handles)
                driver.switch_to.window(handles)
                driver.close()
