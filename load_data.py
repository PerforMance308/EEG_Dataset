import numpy as np
from six.moves import urllib
import os
import tensorflow as tf
import pickle

DATA_DIRECTORY = "data"
SOURCE_URL = 'http://35.183.27.27/'

def maybe_download(filename):
    """Download the data, unless it's already here."""
    if not tf.io.gfile.exists(DATA_DIRECTORY):
        tf.gfile.MakeDirs(DATA_DIRECTORY)
    filepath = os.path.join(DATA_DIRECTORY, filename)     
    if not tf.io.gfile.exists(filepath):
        print('Start downloading dataset...')
        filepath, _ = urllib.request.urlretrieve(SOURCE_URL + filename, filepath)         
        with tf.gfile.GFile(filepath) as f:
            size = f.size()
        print('Successfully downloaded', filename, size, 'bytes.')
    return filepath

def dense_to_one_hot(labels_dense, num_classes = 3):
    num_labels = labels_dense.shape[0]
    index_offset = np.arange(num_labels) * num_classes
    labels_one_hot = np.zeros((num_labels, num_classes))
    labels_one_hot.flat[index_offset + labels_dense.ravel()] = 1
    return labels_one_hot

def load_data(filename, one_hot=False):
    with open(filename, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
        data = dict['data']
        labels = dict['label']

        if one_hot:
            labels = dense_to_one_hot(labels)
        return data, labels

class DataSet(object):
    def __init__(self, data, labels):
        assert data.shape[0] == labels.shape[0], ("data.shape: %s labels.shape: %s" % (data.shape, labels.shape))
        self._num_examples = data.shape[0]

        self._data = data
        self._lables = labels
        self._epochs_completed = 0
        self._index_in_epoch = 0

    @property
    def data(self):
        return self._data

    @property
    def labels(self):
        return self._lables

    @property
    def num_examples(self):
        return self._num_examples

    @property
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

def read_data_sets(one_hot=False):
    class DataSets(object):
        pass
    train_filename = maybe_download('train')
    test_filename = maybe_download('test')

    train_data, train_labels = load_data(train_filename, one_hot)
    test_data, test_labels = load_data(test_filename, one_hot)
    data_sets = DataSets()
    data_sets.train = DataSet(train_data, train_labels)
    data_sets.test = DataSet(test_data, test_labels)
    return data_sets
