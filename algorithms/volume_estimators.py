__author__ = 'timothyahong'


class BaseVolumeEstimator():
    pass


class SimpleVolumeEstimator(BaseVolumeEstimator):
    def estimate(self, cap_values):
        return [
            self._determine_volume(cap_value_row) for cap_value_row in zip(*cap_values)
        ]

    def _determine_volume(self, cap_value_row):
        volume = 0
        for value in cap_value_row:
            #simple quadratic map to 10 and above 10 it counts for the full amount
            value = abs(value)
            if value < 6:
                volume += 50*((float(value)/7)**4)
            else:
                volume += 50
        return int(volume)