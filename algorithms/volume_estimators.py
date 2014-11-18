__author__ = 'timothyahong'


class BaseVolumeEstimator():
    pass


class SimpleVolumeEstimator(BaseVolumeEstimator):
    def estimate(self, stabilized_cap_values):
        return [
            self._determine_volume(stabilized_cap_value_set) for stabilized_cap_value_set in stabilized_cap_values
        ]

    def _determine_volume(self, stabilized_cap_value_set):
        volume = 0
        for value in stabilized_cap_value_set:
            #simple linear mat up to 100ml
            if value < 10:
                volume += 100*(value/10)
            else:
                volume += 100