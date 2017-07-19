import re
import os


def get_input_to_output_filenames_map(input_filenames, output_filenames):
    input_filenames.sort()
    output_filenames.sort()
    return {input_filename: output_filename
            for input_filename, output_filename in zip(input_filenames, output_filenames)}


def get_challenge_5_own_output_filename(filename):
    main_dir_path = re.search('.+challenge_5', filename).group(0)
    name = re.search('/(\w+?).in', filename).group(1)
    subdir = 'own_out'
    return os.path.join(main_dir_path, subdir, name + '_own.out')
