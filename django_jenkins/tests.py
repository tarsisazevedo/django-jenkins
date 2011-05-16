# -*- coding: utf-8 -*-
from unittest import TestCase, main
from django_jenkins.functions import relpath, check_output

class FuntionsTest(TestCase):
    def test_relative_path_is_current_dir(self):
        self.assertEquals('.', relpath(path='.'))

    def test_without_path(self):
        self.assertRaises(ValueError, relpath, path='')

    def test_relative_path_to_home(self):
        self.assertEquals('~', relpath(path='~'))

    def test_output_is_stdout(self):
        self.assertRaises(ValueError, check_output, stdout='stdout')

    def test_output_to_ls(self):
        #test example of this gist: https://gist.github.com/839684
        self.assertEquals('/dev/null\n', check_output(["ls","/dev/null"]))

    def test_output_to_ls_inxesistent_file_or_dir(self):
        #test example of this gist: https://gist.github.com/839684
        from subprocess import STDOUT
        self.assertEquals('ls: non_existent_file: No such file or directory\n', check_output(["/bin/sh", "-c", "ls -l non_existent_file ; exit 0"], stderr=STDOUT))

"""
from django.test import TestCase

class SanityCheckTest(TestCase):
    def test_is_ok(self):
        pass
"""

if __name__=='__main__':
    main()
