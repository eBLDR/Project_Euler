#!/usr/bin/env python3
# -*- coding: utf8 -*-
import os
import subprocess

from time import time


class Supervisor:
    def __init__(self):
        self.interpreter = 'python'
        self.project_url = 'https://projecteuler.net/'
        self.dir_path = os.path.join(os.getcwd(), 'problems')
        self.problem_number = None
        self.problem_number_digits = 3
        self.base_filename = '{}.py'
        self.filename = ''
        self.file_path = ''

    def get_problem_number(self):
        while True:
            number = input('Problem number: ')
            if number.isdigit() and number != '0':
                break

        # Add leading zeroes
        leading_zeroes = ''
        for zero in range(self.problem_number_digits - len(number)):
            leading_zeroes += '0'

        self.problem_number = leading_zeroes + number
        print(self.problem_number)

    def set_filename(self):
        self.filename = self.base_filename.format(self.problem_number)

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
        ext_script = subprocess.Popen(
            [self.interpreter, self.file_path],
            stdout=subprocess.PIPE,
        )
        out, err = ext_script.communicate()
        t_delta = time() - t_0
        print(
            f'Result of problem {self.problem_number} is: \033[1;32m{self.bytes_to_str(out)}'
            f'\033[0mCPU took {t_delta:.4} seconds'
        )


if __name__ == '__main__':
    supervisor = Supervisor()
    supervisor.run()
