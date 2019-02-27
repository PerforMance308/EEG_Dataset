import os
import numpy as np

class DataSet(object):
    def __init__(self, data, labels):
        assert data.shape[0] == labels.shape[0], ("data.shape: %s labels.shape: %s" % (data.shape, labels.shape))
        self._num_examples = data.shape[0]

        self._data = data
        self._lables = labels
        self._epochs_completed = 0
        self._index_in_epoch = 0

    def data(self):
        return self._data

    def labels(self):
        return self._lables

    def num_examples(self):
        return self._num_examples

    def epochs_completed(self):
        return self._epochs_completed

    def next_batch(self, batch_size):
        start = self._index_in_epoch
        self._index_in_epoch += batch_size
        if self._index_in_epoch > self._num_examples:
            self._epochs_completed += 1
            perm = np.arange(self._num_examples)
            np.random.shuffle(perm)
            self._data = self._data[perm]
            self._lables = self._lables[perm]

            start = 0

            self._index_in_epoch = batch_size

            assert batch_size <= self._num_examples
        end = self._index_in_epoch
        return self._data[start:end], self._lables[start:end]

def read_data_sets(train_dir, one_hot=False):
    class DataSet(object):
        pass
    data_set = DataSets()

