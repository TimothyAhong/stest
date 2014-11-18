__author__ = 'timothyahong'


class BaseVolumeEstimator():
    pass


class SimpleVolumeEstimator(BaseVolumeEstimator):
    def estimate(self, cap_values):
        return [
            self._determine_volume(stabilized_cap_value_set) for stabilized_cap_value_set in zip(*cap_values)
        ]

    def _determine_volume(self, cap_value_row):
        volume = 0
        for value in cap_value_row:
            #simple linear mat up to 100ml
            if value < 10:
                volume += 100*(value/10)
            else:
                volume += 100
        return int(volume)