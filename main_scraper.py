from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

from ics import Calendar, Event
from datetime import datetime

from pytz import timezone

local_tz = timezone('America/New_York')  # Adjusted to my local timezone for ics file

# Set up the driver (site is javascript generated)
options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(options=options)

# Navigate to the hockey schedule webpage
url = "https://anc.ca.apm.activecommunities.com/activewaterloo/leagues/info?onlineSiteId=0&league_id=dlpwb0prbWVOTzJXVGVOSGFKUG5Fdz09&display_index=3"
driver.get(url)

# Wait for the content to load 10 seconds
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'league-schedule-card')))

# Get page source
html_content = driver.page_source

# Close the browser window
driver.quit()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all the game segments
games = soup.find_all('div', class_='league-schedule-card')

# Loop through each game and extract information
for game in games:
    home_team = game.find('div', class_='schedule-card__home-wrapper').find('a').text.strip()
    away_team = game.find('div', class_='schedule-card__away-wrapper').find('a').text.strip()
    date = game.find('div', class_='date').text.strip()
    game_time = game.find('div', class_='time-and-status').span.text.strip()
    location = game.find('a', class_='facility-name').text.strip()

# Create a new calendar
cal = Calendar()

# Loop through each game and extract information
for game in games:
    home_team = game.find('div', class_='schedule-card__home-wrapper').find('a').text.strip()
    away_team = game.find('div', class_='schedule-card__away-wrapper').find('a').text.strip()

    # Only add games for my team "INDY #4"

    if home_team == "Indy #4" or away_team == "Indy #4":
        date = game.find('div', class_='date').text.strip()
        game_time = game.find('div', class_='time-and-status').span.text.strip()
        location = game.find('a', class_='facility-name').text.strip()

        # Convert date and time to a datetime object with timezone
        start_time_str = f"{date} {game_time.split(' - ')[0]} 2023"  # Assuming the year is 2023 update later for full sched
        start_time = local_tz.localize(datetime.strptime(start_time_str, '%d %b %I:%M %p %Y'))
        end_time_str = f"{date} {game_time.split(' - ')[1]} 2023"
        end_time = local_tz.localize(datetime.strptime(end_time_str, '%d %b %I:%M %p %Y'))

        # Create an event
        event = Event(name=f"{home_team} vs {away_team}", begin=start_time, end=end_time, location=location)
        cal.events.add(event)

# Save the calendar to an .ics file
with open('games.ics', 'w') as f:
    f.write(str(cal))

print("Calendar file 'games.ics' created!")
