import csv
from pathlib import Path
class Exporter:
    def export_top8_stats(stats, filename="player_stats.csv"):
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            # Header
            writer.writerow([
                "gamerTag",
                "top8's Achieved",
                "1st",
                "2nd",
                "3rd",
                "4th",
                "5th",
                "7th",
                "8th"
            ])

            sorted_players = sorted(
                stats.items(),
                key=lambda item: item[1]["top8"],
                reverse=True
            )

            for player_id, data in sorted_players:
                placements = data["placements"]

                writer.writerow([
                    data["gamerTag"],
                    data["top8"],
                    placements.get(1, 0),
                    placements.get(2, 0),
                    placements.get(3, 0),
                    placements.get(4, 0),
                    placements.get(5, 0),
                    placements.get(7, 0),
                    placements.get(8, 0),
                ])

        print("CSV exported successfully.")
    
    def export_headcount_stats(stats, filename="player_stats.csv"):
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            # Header
            writer.writerow([
                "gamerTag",
                "Times attended",
            ])

            sorted_players = sorted(
                stats.items(),
                key=lambda item: item[1]["top8"],
                reverse=True
            )

            for player_id, data in sorted_players:
                placements = data["placements"]

                writer.writerow([
                    data["gamerTag"],
                    # TODO: write times attended
                ])

        print("CSV exported successfully.")