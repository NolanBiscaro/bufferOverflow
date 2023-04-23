import sqlite3

class LevelManager:
    def __init__(self):
        self.levels = self.load_levels()
        self.connection = sqlite3.connect('progress.db')
        self.cursor = self.connection.cursor()
        self.create_progress_table()
        self.player_progress = self.load_player_progress()

    def load_levels(self):
        # Load level data from the 'levels' directory or another source
        pass

    def create_progress_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS progress
                               (id INTEGER PRIMARY KEY, level INTEGER)''')
        self.connection.commit()

    def load_player_progress(self):
        self.cursor.execute('SELECT level FROM progress WHERE id=1')
        row = self.cursor.fetchone()
        if row:
            return row[0]
        else:
            self.cursor.execute('INSERT INTO progress (id, level) VALUES (1, 1)')
            self.connection.commit()
            return 1

    def get_current_level(self):
        return self.levels[self.player_progress - 1]

    def advance_to_next_level(self):
        if self.player_progress < len(self.levels):
            self.player_progress += 1
            self.cursor.execute('UPDATE progress SET level=? WHERE id=1', (self.player_progress,))
            self.connection.commit()

    def close(self):
        self.connection.close()