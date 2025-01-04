########################
# Unfinished code (dont run)
# Statistical Analysis of Top European Football Leagues From year 2020-2021 version 2
########################
import matplotlib.pyplot as plt
import pandas as pd
from Prompts import Prompts

class FootballAnalysis:
    def __init__(self, base_folder):
        self.base_folder = base_folder
        self.file_names = {
            "league_stats": "leaguestatistics.csv",
            "premier_league": "premierleaguestat.csv",
            "serie_a": "seriastat.csv",
            "la_liga": "laligastat.csv",
            "ligue_1": "ligue1stat.csv",
            "bundesliga": "bundesligastat.csv"
        }
        self.dataframes = {}
        self.load_data()

    def load_data(self):
        for name, file_name in self.file_names.items():
            file_path = f"{self.base_folder}/{file_name}"
            try:
                self.dataframes[name] = pd.read_csv(file_path, encoding='ISO-8859-1')
                print(f"Loaded {file_name} successfully.")
            except FileNotFoundError:
                print(f"File not found: {file_path}")
            except UnicodeDecodeError:
                print(f"Encoding error in file: {file_path}")

    def display_general_details(self):
        
        df = self.dataframes.get('league_stats')
        if df is None or df.empty:  
            print("League statistics data is missing or empty!")
            return
        self.choices_display_leagues(df)
        self.choices_display_general(df)
        
    def choices_for_plot(self):
        print("1. Table\n"
              "2. Line Chart\n"
              "3. Bar Chart\n")
        return int(input("Enter your choice: "))
        
    def display_general_details(self, choice):
        df = self.dataframes.get('league_stats')
        if df is None or df.empty: 
            print("League statistics data is missing or empty!")
            return
        
        try:
            if choice == 1:
                print(df[["Football League", "Country"]])
            elif choice == 2:
                self.plot_goals_per_match(df)
            elif choice == 3:
                Prompts().choices_for_plot()
            elif choice == 4:
                pass
             
            elif choice == 5:
                return
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def plot_goals_per_match(self, df):
        
        choice = self.choices_for_plot()

        if choice == 1:
            print(df[["Football League", "Goals per match"]])
        elif choice == 2:
            plt.plot(df["Football League"], df["Goals per match"])
            plt.title("Goals per Match by League")
            plt.show()
        elif choice == 3:
            df.plot(x="Football League", y="Goals per match", kind='bar', title="Goals per Match by League")
            plt.show()

    def display_league_details(self):
        print("Displaying league-specific details... (to be implemented)")
        

    def display_club_statistics(self):
        print("Displaying club statistics... (to be implemented)")
        

    def run(self):
        menu = Prompts()
        while True:
            choice = menu.main_menu()
            if choice == 3:
                print("Exiting program. Goodbye!")
                break
            elif choice == 0:
                menu.display_glossary()
            elif choice == 1:
                self.display_general_details(menu.display_general_prompt())
            elif choice == 2:
                menu.display_league_specific()
            else:
                print("Invalid choice. Please try again.")



if __name__ == "__main__":
    base_folder = input("Enter the folder path containing the CSV files: ")
    analysis = FootballAnalysis(base_folder)
    analysis.run()
