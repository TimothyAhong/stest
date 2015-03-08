__author__ = 'timothyahong'

formatted_filename = 'formatted.csv'

sub_paths = [
    'dry_diaper_jan_10_2015/',
    'displacement_jan_18_2015/',
    'displacement_jan_21_2015/',
    'wet_1_diaper_jan_11_2015/',
    'analysis/jan_22_all_human_tests/'
]

'''
Paths without dry and wet cases
    'wet_2_jan_12_2015/',
    'wet_3_jan_14_2015/',
'''

base_path = '/Users/timothyahong/Google Drive/Sensassure/Venture Related/Product/Prototyping/V4 Prototype/Experiment Reports/Experiments/Data/'

data_paths = [
    base_path + sub_path for sub_path in sub_paths
]

analysis_sub_paths = [
    'jeremy/',
    'sameer/',
    'tim100/',
    'tim50/'
]

analysis_base_path = base_path + 'analysis/'

analysis_paths = [
    analysis_base_path + sub_path for sub_path in analysis_sub_paths
]
