from os import remove


def flatten_text(text):
    return ' '.join(text.split('\n'))

class DataFile:
    """
    File for saving and loading data into a DQSV file, or Double-Quote Separated Values.
    Compatible with ``with`` statement.
    Does not support multi-line values. Yet.
    """
    def __init__(self, filename, overwrite=False):
        self.filename = filename
        if overwrite:
            try: remove(self.filename + '.txt')
            except: pass
        self.loaded_line = ''
        self.file = open(self.filename + '.txt', 'a+')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

    def write_line(self, string):
        self.file.write(string if '\n' in string else string + '\n')
        self.loaded_line = ''

    def write_lines(self, strings):
        for string in strings:
            self.write_line(string)

    def write_values(self, *values):
        line = ''
        for value in values:
            line += value.strip() + '"'
        self.file.write(line + '\n')
        self.loaded_line = ''

    def load_values(self, *values):
        for value in values:
            self.loaded_line += value.strip() + '"'

    def load_value(self, value):
        self.load_values(value)

    def write_loaded(self):
        self.file.write(self.loaded_line + '\n')
        self.loaded_line = ''


with DataFile('test', overwrite=True) as out:
    out.write_line('2')

print 'done'