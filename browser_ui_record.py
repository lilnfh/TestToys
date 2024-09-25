import subprocess
import time
import os
import sqlite3


filename = str(int(time.time()*1000))
filename = "1727274686322"
directory_path = f"./records/{filename}"
url = "itch.io"

def record(url, filename, directory_path):
    os.makedirs(directory_path, exist_ok=True)
    process  = subprocess.Popen(['playwright', 'codegen', url, '-o', f"{directory_path}/{filename}.py"], stdout=subprocess.PIPE)
    # wait for command to finish
    stdout, stderr = process.communicate()

    # check response code
    if process.returncode == 0:
        print("Command run successfully")
        print("Output: ")
        print(stdout)
    else:
        print("Command run failed")
        print("Error: ")
        print(stderr)

def save(filename, directory_path):
    conn = sqlite3.connect('./datas/testtoys.db')
    cursor = conn.cursor()
    order = 1
    with open(f"{directory_path}/{filename}.py", 'r') as file:
        for line in file:
            if line.strip().startswith("page."):
                try:
                    cursor.execute('INSERT INTO user_operation ( name, relative_timestamp, "order" ) VALUES (?, ?, ?)', ( line.strip(), filename, order))
                    order += 1
                except Exception as e:
                    print(f"SQL Error: {e}")
    cursor.execute('INSERT INTO timestamp_name ( name, timestamp ) VALUES (?, ?)', ( filename, filename))
    conn.commit()
    conn.close()

def modify(url, filename, directory_path):
    with open(f"{directory_path}/{filename}.py", 'r') as file:
        lines = file.readlines()

    lines.insert(8, f"    page.route_from_har('{directory_path}/html/{filename}.har', url='**/**{url}**/**', update=True)" + '\n')

    """
    window_maxium_no = -1
    for no, line in enumerate(lines):
        if line.strip().startswith("browser = playwright.chromium.launch(headless=False)"):
            window_maxium_no = no
    lines[window_maxium_no] = f"    browser = playwright.chromium.launch(headless=False, args=['--start-maximized'])\n"
    """
    
 
    video_no = -1
    for no, line in enumerate(lines):
        if line.strip().startswith("context = browser.new_context"):
            video_no = no
    lines[video_no] = f"    context = browser.new_context(record_video_dir='{directory_path}/videos/',record_video_size="+"{"+"'width': 1920, 'height': 1080}, viewport="+"{"+"'width': 1920, 'height': 1080})\n"

    
    # get the number of the "page."
    pages_no = []
    for no, line in enumerate(lines):
        if line.strip().startswith("page."):
            pages_no.append(no)
    for no in reversed(pages_no[2:]):
        lines.insert(no, f"    page.screenshot(path='{directory_path}/screenshot/{no}.png')" + '\n')

    

    # write back
    with open(f"{directory_path}/{filename}changed.py", 'w') as file:
        file.writelines(lines)

def replay(filename, directory_path):
    #process  = subprocess.Popen(['playwright', 'open', f"--save-har={directory_path}/{filename}.har", '--save-har-glob', f"{directory_path}/{filename}.py"], stdout=subprocess.PIPE)
    process  = subprocess.Popen(['python', f"{directory_path}/{filename}changed.py"])
    # wait for command to finish
    stdout, stderr = process.communicate()

    # check response code
    if process.returncode == 0:
        print("Command run successfully")
        print("Output: ")
        print(stdout)
    else:
        print("Command run failed")
        print("Error: ")
        print(stderr)

# Record User Operation
#record(url, filename, directory_path)

# Save User Operation to database
#save(filename, directory_path)

# Modify the {timestamp}.py file, let it run with screenshot
#modify(url, filename, directory_path)

# Replay, and save as HAR file
#replay(filename, directory_path)

# Save records, screenshot, video to database
