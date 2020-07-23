import os
import subprocess
from time import time

from data import config


class Supervisor:
    def __init__(self):
        self.interpreter = config.INTERPRETER
        self.project_url = config.PROJECT_URL
        self.dir_path = config.PROBLEMS_PATH

        self.problem_number = None
        self.filename = ''
        self.file_path = ''

    def get_problem_number(self):
        while True:
            number = input('Problem number: ')
            if number.isdigit() and number != '0':
                break

        # Add leading zeroes
        leading_zeroes = ''
        for zero in range(config.PROBLEM_NUMBER_DIGITS - len(number)):
            leading_zeroes += '0'

        self.problem_number = leading_zeroes + number
        print(self.problem_number)

    def set_filename(self):
        self.filename = config.BASE_FILENAME.format(self.problem_number)

    def search_file(self):
        return self.filename in os.listdir(self.dir_path)

    def set_file_path(self):
        self.file_path = os.path.join(self.dir_path, self.filename)

    @staticmethod
    def bytes_to_str(b):
        return b.decode('utf-8')

    def run(self):
        print(f'- Project Euler Problems -\n\033[4;1;34m{self.project_url}\033[0m\n')

        self.get_problem_number()
        self.set_filename()
        self.set_file_path()

        print('=' * 25)

        if not self.search_file():
            print('\033[1;31mProblem not found.\033[0m')
            return

        print('Computing...')

        t_0 = time()
        out, err = self.solve_problem()
        t_delta = time() - t_0

        print(
            f'Result of problem {self.problem_number} is: \033[1;32m{self.bytes_to_str(out)}'
            f'\033[0mCPU took {t_delta:.4} seconds.'
        )

    def solve_problem(self):
        ext_script = subprocess.Popen(
            [self.interpreter, self.file_path],
            stdout=subprocess.PIPE,
        )
        return ext_script.communicate()
