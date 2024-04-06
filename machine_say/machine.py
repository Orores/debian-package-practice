import argparse

class machine_say:
    def get_arguments(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-w','--word', dest='word', help='The word you want the machine to say')
        options = parser.parse_args()
        if not options.word:
            parser.error('Please enter the word you want the machine to say. Enter -h for help')
        return options

    def say(self, word):
        print(f'machine says {word}')

def main():
    machine = machine_say()
    options = machine.get_arguments()
    machine.say(options.word)

if __name__ == "__main__":
    main()
