from pdfminer.high_level import extract_text
import re
game_dates = ['2023\n','Oct', 'Sep', 'Nov']
team_names = ['#8-Honey Nut Chelios',
                '#1-Llamas with Hats',
                '#10-Arctic Wolf HC',
                '#2-CnC Sports Cards',
                '#7-Team Ramrod',
                '#3-Unit 91',
                '#11-Indy #3',
                '#9-Tuff Pucks',
                '#12-Indy #4',
                '#13-Cambridge Canadians',
                '#14-KW Hockey Club',
                '#5-Hawks',
                '#4-Floopy Pucks',
                '#6-Lucidaco Lightning',]
rink_names = ['RIM - Ice (2) Optimist\'s',
                'RIM - Ice (1) Piller\'s Ice', 
                'AMCC - Ice West',
                'RIM - Ice (3) Lions Rink']
game_times = ['10:00 PM', '10:30 PM', '11:00 PM', '11:30 PM', '9:30 PM']

class Game:
    def __init__(self, date, time, location, home_away, away_team):
        self._date=date
        self._time=time
        self._location=location
        self._home_away=home_away
        self._away_team=away_team

def extract_text_from_pdf(pdf_filename):
    raw_text = extract_text(pdf_filename)
    
    # Split the text by lines and remove unnecessary newlines
    cleaned_lines = [line.strip() for line in raw_text.split('\n') if line.strip()]
    
    # Join the cleaned lines back together
    cleaned_text = '\n'.join(cleaned_lines)
    
    return cleaned_text

def extract_game_details(text):
    # Split the text into lines
    lines = text.split('\n')
    
    # Initialize empty lists to store extracted details
    dates = []
    times = []
    locations = []
    home_team = []
    away_team = []
    # teams = []
    
    # Iterate over the lines to extract details
    counter = 1
    dateMemory = ''
    pdfCreationDate = ''
    for line in lines:
        for date in game_dates:
            if date in line:
                if pdfCreationDate == '':
                    pdfCreationDate = line
                    break
                else:
                    if line != pdfCreationDate:
                        dates.append(line)
                        dateMemory = line
                        # print(line)
                        break
        for rink in rink_names:
            if rink in line:
                locations.append(rink)
                dates.append(dateMemory)
                break
        for team in team_names:
            if team in line:
                if counter % 2 == 1:
                    home_team.append(team)
                else:
                    away_team.append(team)
                counter += 1
                break
        for time in game_times:
            if time in line:
                times.append(time)
                break
        print(line)
        #   
    # print(dates)  
    print("-" * 80)

    locationLength = len(locations)
    # dates = dates[1:] # skip first date bc date when pdf made
    for date in set(dates):
        if dates.count(date) > 1:
            dates.remove(date)
    games = []
    print(dates)
    print('dates',len(dates))
    print('locations',len(locations))
    print('times',len(times))
    print('home teams',len(home_team))
    print('away teams', len(away_team))

    # # make x number of games based on times or locations
    # for x in range(len(times)):
    #     gameObj = Game(None, times[x], locations[x], None, None)
    # print('='*50)

    # for i in range(len(home_team)): #using locations to get accurate number of games
    #     gameObj = Game(dates[i], times[i], locations[i], home_team[i], away_team[i])
    #     games.append(gameObj)

    # # # Print the extracted details
    # for game in range(len(games)):
    #     print(f"Date:", game.date)
    #     print(f"Time:", game.time)
    #     print(f"Location:", game.location)
    #     print(f"Home Team:", game.home_team)
    #     print(f"Away Team:", game.away_team)
    #     print("-" * 40)
def remove_duplicates(input_list):
    return list(dict.fromkeys(input_list))

if __name__ == "__main__":
    pdf_filename = "schedule.pdf"
    extracted_text = extract_text_from_pdf(pdf_filename)
    extract_game_details(extracted_text)