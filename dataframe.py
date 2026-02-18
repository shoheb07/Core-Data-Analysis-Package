class DataFrame:
    def __init__(self, data):
        """
        data: list of dictionaries
        """
        self.data = data
        self.columns = list(data[0].keys()) if data else []

    def head(self, n=5):
        return DataFrame(self.data[:n])

    def select(self, column):
        return [row[column] for row in self.data]

    def filter(self, column, value):
        filtered = [row for row in self.data if row[column] == value]
        return DataFrame(filtered)

    def to_csv(self, filename):
        if not self.data:
            return

        with open(filename, "w") as f:
            f.write(",".join(self.columns) + "\n")
            for row in self.data:
                f.write(",".join(str(row[col]) for col in self.columns) + "\n")

    def __repr__(self):
        output = ""
        for row in self.data[:5]:
            output += str(row) + "\n"
        return output
