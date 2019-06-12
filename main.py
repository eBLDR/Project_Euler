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
        self.problem_number = 0
        self.base_filename = 'p{}.py'
        self.filename = ''
        self.file_path = ''

    def get_problem_number(self):
        while not self.problem_number:
            n = input('Problem number: ')
            if n.isdigit() and n != '0':
                self.problem_number = int(n)

    def set_filename(self):
        self.filename = self.base_filename.format(self.problem_number)

    def search_file(self):
        return True if self.filename in os.listdir(self.dir_path) else False

    def set_file_path(self):
        self.file_path = os.path.join(self.dir_path, self.filename)

    @staticmethod
    def bytes_to_str(b):
        return b.decode('utf-8')

    def run(self):
        print('- Project Euler Problems -\n\033[4;1;34m{}\033[0m\n'.format(
            self.project_url))

        self.get_problem_number()
        self.set_filename()
        self.set_file_path()

        print('=' * 25)

        if self.search_file():
            print('Computing...')
            t_0 = time()
            ext_script = subprocess.Popen(
                [self.interpreter, self.file_path],
                stdout=subprocess.PIPE
            )
            out, err = ext_script.communicate()
            t_delta = time() - t_0
            print(
                'Result of problem {} is: \033[1;32m{}'
                '\033[0mCPU took {:.4} seconds'.format(
                    self.problem_number, self.bytes_to_str(out), t_delta)
            )

        else:
            print('\033[1;31mProblem not found.\033[0m')


if __name__ == '__main__':
    supervisor = Supervisor()
    supervisor.run()
