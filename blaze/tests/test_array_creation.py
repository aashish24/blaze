import blaze
from blaze.datadescriptor import dd_as_py
import numpy as np
import unittest
from .common import MayBeUriTest


class TestEphemeral(unittest.TestCase):

    def test_create_from_numpy(self):
        a = blaze.array(np.arange(3))
        self.assert_(isinstance(a, blaze.Array))
        self.assertEqual(dd_as_py(a._data), [0, 1, 2])

    def test_create(self):
        # A default array (backed by NumPy)
        a = blaze.array([1,2,3])
        self.assert_(isinstance(a, blaze.Array))
        self.assertEqual(dd_as_py(a._data), [1, 2, 3])
        # XXX The tests below still do not work
        # self.assertEqual(a[0], 1)
        # self.assertEqual(a[1], 2)
        # self.assertEqual(a[2], 3)

    def test_create_append(self):
        # A default array (backed by NumPy, append not supported yet)
        a = blaze.array([])
        self.assert_(isinstance(a, blaze.Array))
        self.assertRaises(NotImplementedError, a.append, [1,2,3])
        # XXX The tests below still do not work
        # self.assertEqual(a[0], 1)
        # self.assertEqual(a[1], 2)
        # self.assertEqual(a[2], 3)

    def test_create_compress(self):
        # A compressed array (backed by BLZ)
        a = blaze.array(np.arange(1,4), caps={'compress': True})
        self.assert_(isinstance(a, blaze.Array))
        self.assertEqual(dd_as_py(a._data), [1, 2, 3])
        # XXX The tests below still do not work
        # self.assertEqual(a[0], 1)
        # self.assertEqual(a[1], 2)
        # self.assertEqual(a[2], 3)

    def test_create_iter(self):
        # A default array (backed by NumPy)
        a = blaze.array((i for i in range(10)))
        self.assert_(isinstance(a, blaze.Array))
        self.assertEqual(dd_as_py(a._data), range(10))

    def test_create_compress_iter(self):
        # A compressed array (backed by BLZ)
        a = blaze.array((i for i in range(10)), caps={'compress': True})
        self.assert_(isinstance(a, blaze.Array))
        self.assertEqual(dd_as_py(a._data), range(10))

    def test_create_zeros(self):
        # A default array (backed by NumPy)
        a = blaze.zeros('10, int64')
        self.assert_(isinstance(a, blaze.Array))
        self.assertEqual(dd_as_py(a._data), [0]*10)

    def test_create_compress_zeros(self):
        # A compressed array (backed by BLZ)
        a = blaze.zeros('10, int64', caps={'compress': True})
        self.assert_(isinstance(a, blaze.Array))
        self.assertEqual(dd_as_py(a._data), [0]*10)

    def test_create_ones(self):
        # A default array (backed by NumPy)
        a = blaze.ones('10, int64')
        self.assert_(isinstance(a, blaze.Array))
        self.assertEqual(dd_as_py(a._data), [1]*10)

    def test_create_compress_ones(self):
        # A compressed array (backed by BLZ)
        a = blaze.ones('10, int64', caps={'compress': True})
        self.assert_(isinstance(a, blaze.Array))
        self.assertEqual(dd_as_py(a._data), [1]*10)


class TestPersistent(MayBeUriTest, unittest.TestCase):

    uri = True

    def test_create(self):
        a = blaze.create(self.rooturi, 'float64')
        self.assert_(isinstance(a, blaze.Array))
        self.assertEqual(dd_as_py(a._data), [])

    def test_append(self):
        a = blaze.create(self.rooturi, 'float64')
        self.assert_(isinstance(a, blaze.Array))
        a.append(range(10))
        self.assertEqual(dd_as_py(a._data), range(10))


if __name__ == '__main__':
    unittest.main()
