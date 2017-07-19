

class Challenge(object):
    def __init__(self, input_to_output_filenames_map):
        self.input_to_output_filenames_map = input_to_output_filenames_map

    def solve_challenge(self, filename):
        pass

    def test_challenge(self):
        for filename in self.input_to_output_filenames_map.keys():
            print filename
            res = self.solve_challenge(filename)
            res = self.res_to_str(res)
            output_filename = self.input_to_output_filenames_map[filename]
            with open(output_filename) as output:
                out = output.read()
            if self.compare_res_with_out(res, out):
                print 'tak'
            else:
                print 'nie'

    @staticmethod
    def compare_res_with_out(res, out):
        return res == out.strip()

    @staticmethod
    def res_to_str(res):
        return str(res)
