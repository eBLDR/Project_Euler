#!/usr/bin/env python3

import os


class Supervisor:
    def __init__(self):
        self.project_url = 'https://projecteuler.net/'
        self.file_path = './problems'
        self.problem_number = 0
        self.base_filename = 'p{}.py'
        self.filename = ''
        self.base_run_command = 'python {}/{}'
        self.run_command = ''

    def get_problem_number(self):
        while not self.problem_number:
            n = input('Problem number: ')
            if n.isdigit() and n != '0':
                self.problem_number = int(n)

    def set_filename(self):
        self.filename = self.base_filename.format(self.problem_number)

    def search_file(self):
        return True if self.filename in os.listdir(self.file_path) else False

    def set_run_command(self):
        self.run_command = self.base_run_command.format(self.file_path, self.filename)

    def run(self):
        print('- Project Euler Problems -\n\033[4;1;34m{}\033[0m\n'.format(self.project_url))
        self.get_problem_number()
        self.set_filename()
        self.set_run_command()
        print('=' * 25)
        if self.search_file():
            print('Result of problem {} is:\033[1;32m'.format(self.problem_number))
            os.system(self.run_command)
        else:
            print('\033[1;31mProblem not found.')


if __name__ == '__main__':
    supervisor = Supervisor()
    supervisor.run()
