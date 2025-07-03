from datetime import date
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import psycopg2
# /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir="/Users/johnnymudawar/chrome-debug"
# Configure Chrome options
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=chrome_options)

# Pause to allow manual password input
input("Please enter your password and press Enter to continue...")

# Continue with the rest of the script
print("Resuming script...")

def scrape_data():
    props = []
    board = driver.find_elements(By.ID, 'test-projection-li')
    for p in board:
        player_name = p.find_element(By.ID, 'test-player-name').text
        prop_type = p.find_element(By.CLASS_NAME, 'break-words').text
        proj_value = p.find_element(By.CLASS_NAME, 'duration-300.ease-in').text
        props.append({'player': player_name, 'prop_type': prop_type, 'proj_value': proj_value})
    df = pd.DataFrame(props)
    df['game_date'] = date.today() 
    print(df)
    return df

def insert_into_props_db(data):
    data = data.to_csv('data.csv', index=False)

    conn = psycopg2.connect(
    dbname="player_stats_db",
    user="johnnymudawar",
    password="",
    host="localhost",
    port="5432")

    cur = conn.cursor()

    with open('data.csv') as f:
        next(f)
        cur.copy_from(f, "props", sep=",")
    
    conn.commit()
    cur.close()
    conn.close()

def main():
    new_data = scrape_data()
    insert_into_props_db(new_data)

if __name__ == '__main__':
    main()

while True:
    user_input = input("Type 'x' to stop the program: ")
    if user_input.lower() == "x":
        driver.quit()
        print("Program terminated.")
        break
