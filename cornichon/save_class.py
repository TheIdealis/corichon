# Saving a class using pickle and search for subclasses automatically
#
# TODO: add descriptino
# TODO: Currently there can only be one unique instance for every object
import os
from types import MethodType
import pickle

def save_all(self, filename):
    directory = os.path.dirname(filename)
    if not os.path.exists(directory):
        os.makedirs(directory)
    filename, extension = os.path.splitext(filename)
    if extension is '':
        extension = '.dat'
    self.subclasses = []
    for key, value in self.__dict__.items():
        if hasattr(value, 'save_all'):
            self.subclasses.append([key, value.__class__.__name__])
            sc_filename = f'{filename}_{value.__class__.__name__}{extension}'
            # save obj
            obj = getattr(self, key)
            obj.save_all(sc_filename)
            # delete obj
            obj = None

    with open(f'{filename}{extension}', 'wb') as outfile:
        pickle.dump(self.__dict__, outfile, protocol=pickle.HIGHEST_PROTOCOL)


def load_all(self, filename):
    filename, extension = os.path.splitext(filename)
    if extension is '':
        extension = '.dat'
    # Extracting the relative directory while loading allows one to move the
    # stored date relative to the script creating it
    relative_dir = os.path.dirname(filename)

    with open(f'{filename}{extension}', 'rb') as infile:
        data = pickle.load(infile)
    self.__dict__.update(data)

    # The structure of the subclass might have changed, so we load it again
    for key, value in self.subclasses:
        subclassfilename = f'{filename}_{value}{extension}'
        subclassfilename = os.path.basename(subclassfilename)
        subclassfilename = os.path.join(relative_dir, subclassfilename)
        getattr(self, key).load_all(subclassfilename)

