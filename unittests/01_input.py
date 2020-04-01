import unittest
import HDF5reader as h5r

class inputDataValidation(unittest.TestCase):
    def empty_filename(self):
        result = h5r.HDF5Reader('')
        self.assertIsNone(result) 
