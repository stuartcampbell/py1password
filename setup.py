#!/usr/bin/env python

from setuptools import setup

setup(name='py1password',
      version='0.1',
      description='Python library for interfacing with 1password cli',
      author='Stuart B. Wilkins',
      author_email='stuart@stuwilkins.org',
      packages=['py1password'],
      entry_points={
        'console_scripts':
        ['op-askpass=py1password.command_line:askpass',
         'op-unlock=py1password.command_line:add_keys_to_agent',
         'op-getkey=py1password.command_line:download_key'],
        })
