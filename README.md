# Game Calendar Scraper

## Introduction

This Python script allows you to scrape game schedule data from a specific website and generate an iCalendar (ICS) file for easy integration with calendar applications such as Google Calendar, Outlook, and Apple Calendar. You can customize the script to scrape game schedules for specific teams or leagues by modifying the team names in the code.

## Prerequisites

Before you can use this script, you need to have the following dependencies installed:

- [Python](https://www.python.org/downloads/) (Python 3.6 or higher)
- [Selenium](https://pypi.org/project/selenium/) - To automate web interactions
- [Beautiful Soup](https://pypi.org/project/beautifulsoup4/) - For HTML parsing
- [ics](https://pypi.org/project/ics/) - To work with iCalendar files
- [pytz](https://pypi.org/project/pytz/) - For timezone handling
- [Chrome WebDriver](https://sites.google.com/chromium.org/driver/) - The WebDriver for Google Chrome (or a WebDriver for your preferred browser)

You'll also need to configure the `webdriver.ChromeOptions()` to match your WebDriver setup.

## Installation

1. Clone this GitHub repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/game-calendar-scraper.git
   ```

2. Navigate to the project directory:

   ```bash
   cd game-calendar-scraper
   ```

3. Install the required Python dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Open the `game_calendar_scraper.py` script in your code editor.

2. Modify the script to suit your needs. You can change the target URL, customize team names, or adjust the WebDriver settings.

3. Run the script:

   ```bash
   python game_calendar_scraper.py
   ```

   The script will scrape game schedule data from the specified website and generate an iCalendar file named `games.ics` in the project directory.

4. Import the generated `games.ics` file into your preferred calendar application. The game schedules will be added to your calendar.

## Customization

You can customize the script in the following ways:

- **Target URL**: Change the URL in the `driver.get()` method to scrape game schedules from a different website.

- **Team Filtering**: Modify the team names in the code to filter games for specific teams. For example, you can replace `"Indy #4"` with the name of your favorite team.

- **WebDriver Options**: Customize the `options` object to configure the WebDriver settings. For example, you can enable or disable headless mode or specify the WebDriver executable path.

- **Timezone**: Adjust the `local_tz` variable to set your desired timezone for game schedule times.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This script was created by Jake Hessian as a personal project.
- Special thanks to the open-source community for their contributions to the libraries used in this project.

## Questions and Issues

If you have any questions or encounter issues while using this script, please feel free to [create an issue](https://github.com/yourusername/game-calendar-scraper/issues) on the GitHub repository. We'll do our best to assist you.
