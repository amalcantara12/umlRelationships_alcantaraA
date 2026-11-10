class Printer:
    def print_page(self, text: str):
        print("Printing: ", text)

class ScoreOutput:
    def __init__(self, content: str):
        self.content = content

    def print_output(self, printer_device: Printer):
        printer_device.print_page(self.content)