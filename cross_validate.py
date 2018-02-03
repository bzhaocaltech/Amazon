# This file essentially just makes cross validations a lot less messy

# TODO: Probably test or something

class CrossValidation:
    # Takes in a set of data to be split into different partitions as well as
    # the number of partitions that you want to split on.
    # With shuffle on, will randomly shuffle the data
    def __init__(self, data, num_partitions, shuffle = True):
        self.num_partitions = num_partitions
        copy_data = np.copy(data)
        if shuffle:
            np.random.shuffle(copy_data)
        self.data = np.array_split(data, num_partitions)

    # Returns a certain partition of the data
    def get_partition(self, partition_number):
        return self.data[partition_number]

    # Returns everything but a certain partition of the data
    def get_other_partitions(self, partition_number):
        to_return = None
        for i in range(len(self.data)):
            if i != partition_number:
                if to_return is None:
                    to_return = self.data[i]
                else:
                    np.concatenate((to_return, self.data[i]))

        return to_return
