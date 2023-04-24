import sqlite3
import os
import glob

class LevelManager:
    def __init__(self):
        self.levels = self.load_levels()
        self.connection = sqlite3.connect('progress.db')
        self.cursor = self.connection.cursor()
        self.create_progress_table()
        self.player_progress = self.load_player_progress()

    def load_levels(self):
        levels = []
        level_paths = sorted(glob.glob('levels/level_*'))

        for i, level_path in enumerate(level_paths, start=1):
            level = {
                'number': i,
                'path': f'{level_path}/vulnerable_code.c',
                'instructions': self.load_level_instructions(level_path),
                'hints': self.load_level_hints(level_path)
            }
            levels.append(level)

        return levels

    def save_progress(self):
        with open('progress.txt', 'w') as f:
            f.write(str(self.player_progress))

    def load_level_instructions(self, level_path):
        with open(f'{level_path}/instructions.txt', 'r') as f:
            return f.read()

    def load_level_hints(self, level_path):
        with open(f'{level_path}/hints.txt', 'r') as f:
            return f.read()

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