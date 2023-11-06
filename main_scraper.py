from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

from ics import Calendar, Event
from datetime import datetime, timedelta

from pytz import timezone

local_tz = timezone('America/New_York') 

options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(options=options)

try:
    driver.get("https://anc.ca.apm.activecommunities.com/activewaterloo/leagues/info?league_id=THZYZUF2SWVQYUY4ZHhPUE5MSi8rdz09&display_index=1")
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'league-schedule-card')))
    html_content = driver.page_source
except Exception as e:
    print("An error occurred:", e)
finally:
    driver.quit()

soup = BeautifulSoup(html_content, 'html.parser')
games = soup.find_all('div', class_='league-schedule-card')

cal = Calendar()

current_date = datetime.now(local_tz)
current_year = current_date.year

for game in games:
    home_team = game.find('div', class_='schedule-card__home-wrapper').find('a').text.strip()
    away_team = game.find('div', class_='schedule-card__away-wrapper').find('a').text.strip()

    if home_team == "Indy #4" or away_team == "Indy #4":
        date = game.find('div', class_='date').text.strip()
        game_time = game.find('div', class_='time-and-status').span.text.strip()
        location = game.find('a', class_='facility-name').text.strip()

        # Parse the date and time into a datetime object
        game_month_day = datetime.strptime(date, '%d %b').replace(year=current_year)
        start_time = datetime.strptime(game_time.split(' - ')[0], '%I:%M %p').time()
        end_time = datetime.strptime(game_time.split(' - ')[1], '%I:%M %p').time()

        # Combine the parsed date and time, localize to the correct timezone
        game_start = local_tz.localize(datetime.combine(game_month_day, start_time))
        game_end = local_tz.localize(datetime.combine(game_month_day, end_time))

        # Check if the game is in the next year
        if game_start < current_date:
            game_start = game_start.replace(year=current_year + 1)
            game_end = game_end.replace(year=current_year + 1)

        # Adjust for games that end after midnight
        if game_end < game_start:
            game_end += timedelta(days=1)

        print('=' * 50)
        print(f"Creating an event with the following details:")
        print(f"Home Team: {home_team}")
        print(f"Away Team: {away_team}")
        print(f"Start Time: {game_start}")
        print(f"End Time: {game_end}")
        print(f"Location: {location}")

        event = Event(name=f"{home_team} vs {away_team}", begin=game_start, end=game_end, location=location)
        cal.events.add(event)

with open('games.ics', 'w') as f:
    f.write(str(cal))

print("Calendar file 'games.ics' created!")
