import argparse
import sys
import time

class machine_say:
    '''
    class that makes machine say something you want via argument
    '''
    FAIL = '\33[91m'
    OKGREEN = '\33[92m'
    OKCYAN ='\33[96m'
    ORANGE = '\33[93m'
    BOLD = '\33[1m'



    def get_arguments(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-w','--word', dest='word', help='The word you want the machine to say')
        options = parser.parse_args()
        if not options.word:
            parser.error(self.FAIL + self.BOLD + 'Please enter the word you want the machine to say. Enter -h for help')
        return options

    def say(self, word):
        print(self.OKGREEN + '[]' + self. OKCYAN + f'machine says {word}')

    def slowprint(self,s):
        for c in s + '\n':
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0. / 100)

    def script_header(self):
        self.slowprint(
                '''\33[1;31m \33[95m
                                      _     _                                  
                                     | |   (_)                                 
                 _ __ ___   __ _  ___| |__  _ _ __   ___   ___  __ _ _   _ ___ 
                | '_ ` _ \ / _` |/ __| '_ \| | '_ \ / _ \ / __|/ _` | | | / __|
                | | | | | | (_| | (__| | | | | | | |  __/ \__ \ (_| | |_| \__ \\
                |_| |_| |_|\__,_|\___|_| |_|_|_| |_|\___| |___/\__,_|\__, |___/
                                                                      __/ |    
                                                                     |___/     
                \33[92m
                '''
                )

def main():
    machine = machine_say()
    options = machine.get_arguments()
    machine.script_header()
    machine.say(options.word)

if __name__ == "__main__":
    main()
