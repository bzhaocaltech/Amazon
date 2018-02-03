# This file essentially just makes cross validations a lot less messy
import numpy as np

# TODO: This isn't working

class CrossValidation:
    # Takes in a set of data to be split into different partitions as well as
    # the number of partitions that you want to split on.
    def __init__(self, x_data, y_data, num_partitions):
        self.num_partitions = num_partitions
        x_copy = np.copy(x_data)
        y_copy = np.copy(y_data)
        if len(x_copy) != len(y_copy):
            raise TypeError("x_data and y_data lengths do not match!")
        self.x_data = np.array_split(x_copy, num_partitions)
        self.y_data = np.array_split(y_copy, num_partitions)

    # Returns a certain partition of the data
    def get_partition(self, partition_number):
        return self.x_data[partition_number], self.y_data[partition_number]

    # Returns everything but a certain partition of the data
    def get_other_partitions(self, partition_number):
        to_return_x = None
        to_return_y = None
        for i in range(self.num_partitions):
            if i != partition_number:
                if to_return_x is None:
                    to_return_x = self.x_data[i]
                    to_return_y = self.y_data[i]
                else:
                    to_return_x = np.concatenate((to_return_x, self.x_data[i]))
                    to_return_y = np.concatenate((to_return_y, self.y_data[i]))

        return to_return_x, to_return_y
