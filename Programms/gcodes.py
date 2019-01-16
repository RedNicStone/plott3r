
#--------------#
# G-code class #
#--------------#

#---tested: approved!---
# adding new features

class gcode():

    def __init__(self, gcode_raw):
        self.gcode_raw = gcode_raw
        self.gcode_codereadable = None
        self.gcode_functions = None
        self.key = None
        self.mode = {'distance': 'cm'}

        self.gcode_table = {
            '00': 'rapidgoto',
            '01': 'goto',
            '21': 'cm',
            '20': 'in'
        }

    def convert_codereadable(self):
        try:
            self.gcode_lines = self.gcode_raw.split('\n')
            self.gcode_codereadable = [None]*len(self.gcode_lines)
            for linenuber in range(0, len(self.gcode_lines)):
                self.gcode_codereadable[linenuber] = self.gcode_lines[linenuber].split()

        except:
            raise ValueError('Must be Gcode')

    def convert_functions(self):
        if self.gcode_codereadable == None:
            self.convert_codereadable()

        self.gcode_functions = []

        for line in range(len(self.gcode_codereadable)):
            if self.gcode_codereadable[line][0] == '(':
            self.gcode_functions.append([0] * len(self.gcode_codereadable[line]))
            for segment in range(len(self.gcode_codereadable[line])):
                if segment == 0:
                    self.key = ''
                    for character in self.gcode_codereadable[line][0]:
                        if not character in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                            pass
                        else:
                            print(character)
                            self.key += character
                            if any(var in self.key  for var in self.gcode_table.keys()):
                                self.gcode_functions[line][0] = self.gcode_table[self.key]
                else:
                    self.gcode_functions[line][segment] = self.gcode_codereadable[line][segment]
