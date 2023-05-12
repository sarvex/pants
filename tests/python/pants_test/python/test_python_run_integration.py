# coding=utf-8
# Copyright 2014 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from __future__ import (nested_scopes, generators, division, absolute_import, with_statement,
                        print_function, unicode_literals)

import pytest

from pants_test.pants_run_integration_test import PantsRunIntegrationTest


class PythonRunIntegrationTest(PantsRunIntegrationTest):

  def test_run_26(self):
    self._maybe_run_version('2.6')

  def test_run_27(self):
    self._maybe_run_version('2.7')

  def test_die(self):
    command = ['goal', 'run', 'tests/python/pants_test/python:die'
               '--interpreter=CPython>=2.6,<3',
               '--interpreter=CPython>=3.3', '--quiet']
    pants_run = self.run_pants(command=command)
    assert pants_run.returncode == 1

  def _maybe_run_version(self, version):
    if self.has_python_version(version):
      print(f'Found python {version}. Testing running on it.')
      echo = self._run_echo_version(version)
      v = echo.split('.')  # E.g., 2.6.8.
      self.assertTrue(len(v) > 2, f'Not a valid version string: {v}')
      self.assertEquals(version, f'{v[0]}.{v[1]}')
    else:
      print(f'No python {version} found. Skipping.')
      pytest.skip(f'No python {version} on system')

  def _run_echo_version(self, version):
    binary_name = f'echo_interpreter_version_{version}'
    binary_target = f'tests/python/pants_test/python:{binary_name}'
    # Build a pex.
    # Avoid some known-to-choke-on interpreters.
    command = ['goal', 'run', binary_target,
               '--interpreter=CPython>=2.6,<3',
               '--interpreter=CPython>=3.3', '--quiet']
    pants_run = self.run_pants(command=command)
    return pants_run.stdout_data.rstrip().split('\n')[-1]
