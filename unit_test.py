import unittest
import backupFunctions as bckp

class Test_backupFunctions (unittest.TestCase):

    def test_ignoreFile(self):
        main_list = ['first item', 'second item', 'third item', 'fourth item']
        ignore_list = ['second item', 'third item']
        bckp.check_ignore_list (main_list, ignore_list)

        self.assertEqual(main_list[0], 'first item')
        self.assertEqual(main_list[1], 'fourth item')


if __name__ == '__main__':
    unittest.main()