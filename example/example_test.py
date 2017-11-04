#!/usr/bin/env python

import unittest
import example

class ExampleTest(unittest.TestCase):
  def test_id1(self):
    self.assertEqual(1, example.identity(1))

  def test_id2(self):
    self.assertEqual(2, example.identity(2))


if __name__ == '__main__':
    unittest.main()