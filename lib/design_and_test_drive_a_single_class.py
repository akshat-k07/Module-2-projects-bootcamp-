import math

class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.front = 0
        pass

    def format(self):
        return f"{self.title}: {self.contents}"

    def count_words(self):
        words_in_content = self.contents.split()
        return len(words_in_content)

    def reading_time(self, wpm):
        return math.ceil(self.count_words()/wpm)

    def reading_chunk(self, wpm, minutes):
        num_of_words = wpm * minutes
        words = self.contents.split()
        to_output = words[self.front: self.front + num_of_words]

        if (self.front+num_of_words) >= len(words):
            self.front = 0
        else:
            self.front += num_of_words
        return " ".join(to_output)
