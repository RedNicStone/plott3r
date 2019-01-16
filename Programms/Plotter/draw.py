#from plotter import *
try:
    from PyInquirer import style_from_dict, Token, prompt, Separator
    from examples import custom_style_3
    use_PI = True
except:
    use_PI = False

try:
    from plotter import *
    use_printer = True
except:
    use_printer = False

try:
    from pyfiglet import Figlet
    f = Figlet(font='cricket')
    print(f.renderText('Plott3r'))
    print(f.renderText('Gcode Converter'))
except:
    print('Welcome to the Plott3r Gcode and Image Converter!')

from draw_action import *
from pprint import pprint


print_data_raw = None
print_data_converted = None



demo = [[
DrawAction(3, x = 137.77232, y = 218.470245), DrawAction(2),
DrawAction(3, x = -3.337519, y = -16.778845), DrawAction(3, x = -9.504452, y = -14.224418),
DrawAction(3, x = -14.224418, y = -9.504452), DrawAction(3, x = -16.778845, y = -3.33752),
DrawAction(3, x = -16.778845, y = 3.33752), DrawAction(3, x = -14.224418, y = 9.504452),
DrawAction(3, x = -9.504452, y = 14.224418), DrawAction(3, x = -3.337519, y = 16.778845),
DrawAction(3, x = 3.33752, y = 16.778845), DrawAction(3, x = 9.504452, y = 14.224417),
DrawAction(3, x = 14.224417, y = 9.504452), DrawAction(3, x = 16.778845, y = 3.33752),
DrawAction(3, x = 16.778845, y = -3.33752), DrawAction(3, x = 14.224417, y = -9.504452),
DrawAction(3, x = 9.504452, y = -14.224417), DrawAction(3, x = 3.33752, y = -16.778845),
DrawAction(3, x = -137.77232, y = -218.470245)],[DrawAction(3, x = 193.98969, y = 223.999995), DrawAction(2), DrawAction(3, x = 27.71281, y = -15.999989), DrawAction(3, x = -27.71281, y = 16.000016), DrawAction(3, x = -27.71281, y = -16.000016), DrawAction(3, x = 27.71281, y = 15.999989), DrawAction(1), DrawAction(3, x = 13.8564, y = -119.999992), DrawAction(2), DrawAction(3, x = 41.56922, y = 24.000006), DrawAction(3, x = 55.42562, y = -32.000006), DrawAction(1), DrawAction(2), DrawAction(3, x = -41.56921, y = -24.00001), DrawAction(1), DrawAction(3, x = -13.85641, y = 8.0), DrawAction(2), DrawAction(3, x = -55.42562, y = -32.0), DrawAction(3, x = -55.42563, y = 32.0), DrawAction(3, x = 55.42563, y = 31.99998), DrawAction(3, x = 55.42562, y = -31.99998), DrawAction(1), DrawAction(3, x = 55.42562, y = 15.99999), DrawAction(2), DrawAction(3, x = -55.42562, y = -32.0), DrawAction(1), DrawAction(3, x = -55.42562, y = -15.99999), DrawAction(2), DrawAction(1), DrawAction(2), DrawAction(3, x = 55.42562, y = -31.99998), DrawAction(3, x = 55.42562, y = 31.99998), DrawAction(3, x = -55.42562, y = 32.00001), DrawAction(3, x = -55.42562, y = -32.00001), DrawAction(1), DrawAction(2), DrawAction(3, x = -55.42563, y = -31.99998), DrawAction(1), DrawAction(2), DrawAction(3, x = 55.42563, y = 32.0), DrawAction(3, x = -55.42563, y = 32.00001), DrawAction(3, x = -55.425622, y = -32.00001), DrawAction(3, x = 55.425622, y = -31.99998), DrawAction(1), DrawAction(3, x = 55.42563, y = 15.99999), DrawAction(2), DrawAction(3, x = 55.42562, y = -32.0), DrawAction(1), DrawAction(2), DrawAction(1), DrawAction(3, x = 55.42562, y = 47.99999), DrawAction(2), DrawAction(1), DrawAction(3, x = 82.89567, y = -16.14098), DrawAction(2), DrawAction(3, x = 83.13845, y = 47.99999), DrawAction(3, x = 83.13843, y = -47.99999), DrawAction(3, x = -83.13843, y = -48.0), DrawAction(3, x = -83.13845, y = 48.0), DrawAction(1), DrawAction(3, x = 27.71283, y = 16.0), DrawAction(2), DrawAction(3, x = 83.13843, y = -48.0), DrawAction(1), DrawAction(3, x = 27.7128, y = 48.00001), DrawAction(2), DrawAction(3, x = -83.13843, y = -48.00001), DrawAction(1), DrawAction(3, x = 9.99999997475e-06, y = 64.0), DrawAction(2), DrawAction(3, x = 83.13843, y = -48.0), DrawAction(1), DrawAction(3, x = -27.71281, y = 48.0), DrawAction(2), DrawAction(3, x = -83.13843, y = -48.0), DrawAction(1), DrawAction(3, x = 27.71281, y = 143.999995), DrawAction(2), DrawAction(1), DrawAction(3, x = -27.71282, y = 47.999994), DrawAction(2), DrawAction(1), DrawAction(3, x = -27.7128, y = 48.000019), DrawAction(2), DrawAction(3, x = 83.13843, y = -47.999985), DrawAction(1), DrawAction(3, x = 27.71281, y = 16.000015), DrawAction(2), DrawAction(1), DrawAction(3, x = 27.71282, y = 47.999995), DrawAction(2), DrawAction(1), DrawAction(3, x = 27.7128, y = 48.000019), DrawAction(2), DrawAction(3, x = -83.13843, y = -47.999985), DrawAction(1), DrawAction(3, x = 55.42562, y = 95.999981), DrawAction(2), DrawAction(3, x = -83.13843, y = -48.000006), DrawAction(1), DrawAction(3, x = -27.71282, y = 48.000006), DrawAction(2), DrawAction(3, x = 83.13843, y = -47.999996), DrawAction(1), DrawAction(2), DrawAction(3, x = -83.13843, y = -48.000001), DrawAction(1), DrawAction(3, x = -27.71282, y = 16.0), DrawAction(2), DrawAction(3, x = 83.13845, y = 47.999995), DrawAction(3, x = 83.13843, y = -47.999995), DrawAction(3, x = -83.13843, y = -48.0), DrawAction(3, x = -83.13845, y = 48.0), DrawAction(1), DrawAction(3, x = 55.42563, y = 32.000001), DrawAction(2), DrawAction(3, x = 83.13843, y = -48.000001), DrawAction(1), DrawAction(3, x = 55.15933, y = -15.565115), DrawAction(2), DrawAction(3, x = 83.13153, y = -48.277915), DrawAction(1), DrawAction(2), DrawAction(3, x = -82.61696, y = 47.70691), DrawAction(1), DrawAction(3, x = 27.19826, y = 47.9425), DrawAction(2), DrawAction(3, x = 0.1992, y = -95.885), DrawAction(1), DrawAction(3, x = 55.31857, y = -31.81362), DrawAction(2), DrawAction(3, x = 110.85674, y = 63.99683), DrawAction(1), DrawAction(3, x = -27.29589, y = -48.24071), DrawAction(2), DrawAction(3, x = 83.13843, y = -48.0), DrawAction(1), DrawAction(3, x = 9.99999997475e-06, y = 32.0), DrawAction(2), DrawAction(3, x = -83.13843, y = -48.0), DrawAction(1), DrawAction(3, x = 27.97839, y = -15.84666), DrawAction(2), DrawAction(3, x = -0.26559, y = 127.84666), DrawAction(1), DrawAction(3, x = 27.71281, y = -48.0), DrawAction(2), DrawAction(3, x = -83.13843, y = -48.0), DrawAction(1), DrawAction(3, x = -27.44723, y = 16.15333), DrawAction(2), DrawAction(3, x = -0.26559, y = 127.846675), DrawAction(1), DrawAction(3, x = 0.21579, y = -0.12458), DrawAction(2), DrawAction(3, x = -111.26817, y = 64.240705), DrawAction(1), DrawAction(3, x = 0.46123, y = -31.95962), DrawAction(2), DrawAction(3, x = 110.85674, y = 63.996827), DrawAction(1), DrawAction(2), DrawAction(3, x = -0.26559, y = 127.846663), DrawAction(1), DrawAction(2), DrawAction(3, x = 83.13845, y = 48.0), DrawAction(3, x = 83.13843, y = -48.0), DrawAction(3, x = -83.13843, y = -47.999999), DrawAction(3, x = -83.13845, y = 47.999999), DrawAction(1), DrawAction(3, x = 27.71282, y = 16.0), DrawAction(2), DrawAction(3, x = 83.13843, y = -48.0), DrawAction(1), DrawAction(3, x = -27.29714, y = -48.233633), DrawAction(2), DrawAction(3, x = 82.4081, y = -47.942509), DrawAction(3, x = 0.31538, y = -95.884993), DrawAction(3, x = -83.15505, y = -47.942495), DrawAction(3, x = -83.23802, y = 47.942495), DrawAction(3, x = 0.11618, y = 95.884993), DrawAction(3, x = 83.55341, y = 47.942509), DrawAction(1), DrawAction(3, x = 0.00125000000003, y = -0.00707499999999), DrawAction(2), DrawAction(3, x = -111.26817, y = 64.240708), DrawAction(1), DrawAction(3, x = -27.71548, y = -16.00154), DrawAction(2), DrawAction(3, x = 0.41763, y = -96.238037), DrawAction(1), DrawAction(2), DrawAction(3, x = -111.26817, y = 64.240706), DrawAction(1), DrawAction(2), DrawAction(3, x = 83.13737, y = 48.002865), DrawAction(3, x = -82.78685, y = -48.199511), DrawAction(3, x = -0.35052, y = 96.200125), DrawAction(1), DrawAction(3, x = -27.95913, y = -0.136685), DrawAction(2), DrawAction(1), DrawAction(3, x = 138.81233, y = 0.13778), DrawAction(2), DrawAction(3, x = 83.13845, y = 48.0), DrawAction(3, x = 83.13843, y = -48.0), DrawAction(3, x = -83.13843, y = -48.0), DrawAction(3, x = -83.13845, y = 48.0), DrawAction(1), DrawAction(3, x = 27.71282, y = 16.0), DrawAction(2), DrawAction(3, x = 83.13843, y = -48.0), DrawAction(1), DrawAction(3, x = 55.42563, y = 32.0), DrawAction(2), DrawAction(3, x = -0.26559, y = 127.846665), DrawAction(1), DrawAction(3, x = 0.2601, y = 0.15652), DrawAction(2), DrawAction(3, x = 110.85674, y = 63.996815), DrawAction(1), DrawAction(3, x = -0.00692000000004, y = 31.996008), DrawAction(2), DrawAction(3, x = -82.61696, y = 47.706912), DrawAction(1), DrawAction(3, x = -0.51457, y = 32.297081), DrawAction(2), DrawAction(3, x = 83.13153, y = -48.277914), DrawAction(1), DrawAction(3, x = -27.71246, y = 48.274122), DrawAction(2), DrawAction(3, x = 0.1992, y = -95.884999), DrawAction(1), DrawAction(3, x = 27.9371, y = -48.35192), DrawAction(2), DrawAction(3, x = -111.26817, y = 64.240712), DrawAction(1), DrawAction(3, x = -0.0055000000001, y = 0.00317900000005), DrawAction(2), DrawAction(3, x = 110.309, y = 63.680572), DrawAction(1), DrawAction(3, x = -54.87787, y = 31.961667), DrawAction(2), DrawAction(3, x = 0.1992, y = -95.884999), DrawAction(1), DrawAction(3, x = -55.35924, y = 0.392916), DrawAction(2), DrawAction(3, x = -0.26559, y = 127.846663), DrawAction(1), DrawAction(3, x = -27.71281, y = 16.0), DrawAction(2), DrawAction(3, x = -83.13843, y = -48.0), DrawAction(1), DrawAction(3, x = 27.70731, y = -47.996823), DrawAction(2), DrawAction(3, x = 110.85674, y = 63.996823), DrawAction(1), DrawAction(3, x = 0.64735, y = -0.37375), DrawAction(2), DrawAction(3, x = 81.94334, y = -47.942497), DrawAction(3, x = 0.54774, y = -95.683753), DrawAction(3, x = -82.69026, y = 47.741255), DrawAction(3, x = 0.19918, y = 95.884995), DrawAction(1), DrawAction(3, x = -83.78579, y = 48.37375), DrawAction(2), DrawAction(3, x = -83.13843, y = -48.0), DrawAction(1), DrawAction(3, x = 27.71281, y = 48.0), DrawAction(2), DrawAction(3, x = 83.13843, y = -48.0), DrawAction(1), DrawAction(3, x = -27.7176, y = -79.997234), DrawAction(2), DrawAction(3, x = -83.49181, y = -47.795976), DrawAction(1), DrawAction(3, x = 0.35888, y = -0.20083), DrawAction(2), DrawAction(3, x = 0.083, y = -96.04793), DrawAction(1), DrawAction(3, x = -27.7999, y = 48.04556), DrawAction(2), DrawAction(3, x = 82.78437, y = -47.79558), DrawAction(1), DrawAction(3, x = 0.57393, y = 63.67335), DrawAction(2), DrawAction(3, x = -0.22093, y = -95.88499), DrawAction(1), DrawAction(3, x = 27.46898, y = 111.86583), DrawAction(2), DrawAction(3, x = 0.0498, y = -96.02875), DrawAction(1), DrawAction(3, x = 83.33496, y = 16.44334), DrawAction(2), DrawAction(3, x = -111.26817, y = 64.24071), DrawAction(1), DrawAction(3, x = -27.29324, y = 15.48845), DrawAction(2), DrawAction(3, x = 0.0497999999999, y = -96.02875), DrawAction(1), DrawAction(3, x = -83.18894, y = 16.0228), DrawAction(2), DrawAction(3, x = 110.309, y = 63.68057), DrawAction(1), DrawAction(3, x = 55.96273, y = 32.32876), DrawAction(2), DrawAction(3, x = 0.0498, y = -96.02875), DrawAction(1), DrawAction(3, x = 55.37902, y = 0.29621), DrawAction(2), DrawAction(3, x = 83.13737, y = 48.00287), DrawAction(3, x = -82.78685, y = -48.19951), DrawAction(3, x = -0.35052, y = 96.20013), DrawAction(1), DrawAction(3, x = 27.71246, y = 15.999795), DrawAction(2), DrawAction(3, x = 0.41763, y = -96.238045), DrawAction(1), DrawAction(3, x = -28.12814, y = -16.03854), DrawAction(2), DrawAction(3, x = -111.26817, y = 64.24071), DrawAction(1), DrawAction(3, x = 83.73865, y = 79.65982), DrawAction(2), DrawAction(3, x = -83.49181, y = -47.79598), DrawAction(1), DrawAction(3, x = -83.21663, y = 79.75765), DrawAction(2), DrawAction(3, x = 82.78437, y = -47.79558), DrawAction(1), DrawAction(3, x = 83.73528, y = 47.94292), DrawAction(2), DrawAction(3, x = -83.49181, y = -47.79598), DrawAction(1), DrawAction(3, x = -54.71748, y = 95.591137), DrawAction(2), DrawAction(3, x = 82.78437, y = -47.795577), DrawAction(1), DrawAction(3, x = 28.06689, y = 47.795577), DrawAction(2), DrawAction(3, x = -83.49181, y = -47.795977), DrawAction(1), DrawAction(3, x = -55.00657, y = 31.751703), DrawAction(2), DrawAction(3, x = -111.26817, y = 64.240706), DrawAction(1), DrawAction(3, x = 27.71246, y = 15.997539), DrawAction(2), DrawAction(3, x = 0.41763, y = -96.238038), DrawAction(1), DrawAction(3, x = -27.99535, y = -47.8373), DrawAction(2), DrawAction(3, x = 81.94334, y = -47.9425), DrawAction(3, x = 0.54774, y = -95.68375), DrawAction(3, x = -82.69026, y = 47.74125), DrawAction(3, x = 0.19918, y = 95.885), DrawAction(1), DrawAction(3, x = 54.77171, y = -31.630035), DrawAction(2), DrawAction(3, x = 0.1992, y = -95.885005), DrawAction(1), DrawAction(3, x = 28.03172, y = 239.593452), DrawAction(2), DrawAction(3, x = -82.55748, y = -47.942497), DrawAction(1), DrawAction(3, x = -56.25182, y = 79.80296), DrawAction(2), DrawAction(1), DrawAction(3, x = -27.71282, y = 16.00001), DrawAction(2), DrawAction(1), DrawAction(3, x = -27.71281, y = -15.999983), DrawAction(2), DrawAction(1), DrawAction(2), DrawAction(1), DrawAction(3, x = -27.71281, y = 335.99999), DrawAction(2), DrawAction(1), DrawAction(3, x = -27.71282, y = 48.0), DrawAction(2), DrawAction(1), DrawAction(3, x = -27.71281, y = 16.000001), DrawAction(2), DrawAction(1), DrawAction(3, x = -249.17255, y = 64.14098), DrawAction(2), DrawAction(3, x = -55.425622, y = 32.0), DrawAction(3, x = 55.425622, y = 31.999995), DrawAction(3, x = 41.56922, y = -23.999995), DrawAction(1), DrawAction(3, x = -41.56922, y = -23.99999), DrawAction(2), DrawAction(1), DrawAction(3, x = -55.425621, y = 15.99998), DrawAction(2), DrawAction(3, x = 41.569221, y = -23.99998), DrawAction(1), DrawAction(3, x = -41.569222, y = -24.00001), DrawAction(2), DrawAction(1), DrawAction(3, x = -55.425629, y = 32.0), DrawAction(2), DrawAction(3, x = 166.276901, y = 95.999973), DrawAction(3, x = 166.27685, y = -95.999973), DrawAction(3, x = -166.27685, y = -96.0), DrawAction(3, x = -166.276901, y = 96.0), DrawAction(1), DrawAction(3, x = 5.00000000159e-06, y = 399.99999), DrawAction(2), DrawAction(1), DrawAction(3, x = -13.856406, y = 24.0), DrawAction(2), DrawAction(3, x = 13.856406, y = -8.0), DrawAction(1), DrawAction(3, x = 13.856406, y = 8.0), DrawAction(2), DrawAction(3, x = -27.712812, y = 16.0), DrawAction(1), DrawAction(3, x = -9.99999999252e-07, y = 16.00001), DrawAction(2), DrawAction(3, x = 41.569219, y = -24.0), DrawAction(1), DrawAction(3, x = 27.712814, y = 31.99999), DrawAction(2), DrawAction(3, x = 13.856406, y = 8.0), DrawAction(1), DrawAction(3, x = -13.856407, y = -7.99999), DrawAction(2), DrawAction(1), DrawAction(3, x = -13.856407, y = 24.00001), DrawAction(2), DrawAction(1), DrawAction(3, x = -27.712812, y = 32.00001), DrawAction(2), DrawAction(1), DrawAction(3, x = 13.856406, y = 40.00001), DrawAction(2), DrawAction(3, x = 41.569219, y = 24.0), DrawAction(1), DrawAction(3, x = -13.856406, y = 8.0), DrawAction(2), DrawAction(3, x = -27.712813, y = -16.0), DrawAction(1), DrawAction(2), DrawAction(3, x = -27.712812, y = 16.0), DrawAction(1), DrawAction(3, x = 13.856406, y = 8.0), DrawAction(2), DrawAction(3, x = 13.856406, y = -8.0), DrawAction(1), DrawAction(2), DrawAction(3, x = 13.856406, y = 8.0), DrawAction(1), DrawAction(3, x = -13.856406, y = -8.0), DrawAction(2), DrawAction(3, x = -27.712812, y = -16.0), DrawAction(3, x = 27.712812, y = -16.00001), DrawAction(3, x = 27.712813, y = 16.00001), DrawAction(3, x = -27.712813, y = 16.0), DrawAction(1), DrawAction(2), DrawAction(3, x = -41.569219, y = -24.0), DrawAction(3, x = 41.569219, y = -23.99999), DrawAction(3, x = 41.569219, y = 23.99999), DrawAction(3, x = -41.569219, y = 24.0), DrawAction(1), DrawAction(3, x = -13.856406, y = -40.0), DrawAction(2), DrawAction(3, x = -27.712813, y = -16.0), DrawAction(1), DrawAction(3, x = 27.712813, y = 16.0), DrawAction(2), DrawAction(3, x = 13.856406, y = -8.0), DrawAction(3, x = 13.856406, y = 8.0), DrawAction(3, x = -13.856406, y = 8.0), DrawAction(3, x = -13.856406, y = -8.0), DrawAction(1), DrawAction(3, x = 55.425626, y = -9.99999997475e-06), DrawAction(2), DrawAction(3, x = -27.712813, y = -16.0), DrawAction(1), DrawAction(3, x = 318.454557, y = -136.14096), DrawAction(2), DrawAction(3, x = 83.13846, y = 48.0), DrawAction(3, x = 83.13843, y = -48.0), DrawAction(3, x = -83.13843, y = -48.000015), DrawAction(3, x = -83.13846, y = 48.000015), DrawAction(1), DrawAction(2), DrawAction(3, x = 83.13843, y = -47.999998), DrawAction(1), DrawAction(3, x = 55.42562, y = 64.000031), DrawAction(2), DrawAction(3, x = -83.13843, y = -48.00002), DrawAction(1), DrawAction(3, x = -27.71282, y = 48.00002), DrawAction(2), DrawAction(3, x = 83.13843, y = -48.00001), DrawAction(1), DrawAction(3, x = 55.42563, y = 32.00001), DrawAction(2), DrawAction(3, x = -83.13843, y = -47.999998), DrawAction(1), DrawAction(3, x = 27.7128, y = 112.000018), DrawAction(2), DrawAction(3, x = -83.13843, y = -48.000015), DrawAction(1), DrawAction(3, x = 27.71281, y = 48.000015), DrawAction(2), DrawAction(3, x = 83.13843, y = -48.000015), DrawAction(1), DrawAction(3, x = 138.23138, y = -0.197629), DrawAction(2), DrawAction(3, x = -82.55748, y = -47.942499), DrawAction(1), DrawAction(3, x = 82.55748, y = 47.942499), DrawAction(2), DrawAction(3, x = -82.55748, y = -47.942499), DrawAction(1), DrawAction(3, x = 166.6258, y = 0.082819), DrawAction(2), DrawAction(3, x = 82.78437, y = -47.795576), DrawAction(1), DrawAction(3, x = 27.40329, y = 15.814528), DrawAction(2), DrawAction(3, x = -82.82821, y = -47.814938), DrawAction(3, x = -82.81792, y = 47.814938), DrawAction(1), DrawAction(3, x = 55.45847, y = 31.981048), DrawAction(2), DrawAction(3, x = 82.78437, y = -47.795576), DrawAction(1), DrawAction(3, x = 110.85373, y = -63.73295), DrawAction(2), DrawAction(3, x = 0.41763, y = -96.23805), DrawAction(1), DrawAction(3, x = 27.29483, y = 48.24133), DrawAction(2), DrawAction(3, x = -82.55748, y = -47.9425), DrawAction(1), DrawAction(3, x = 81.97954, y = 79.605345), DrawAction(2), DrawAction(3, x = -82.55748, y = -47.942505), DrawAction(1), DrawAction(3, x = 82.55748, y = 47.942505), DrawAction(2), DrawAction(3, x = -82.55748, y = -47.942505), DrawAction(1), DrawAction(3, x = -110.85124, y = 320.0), DrawAction(2), DrawAction(3, x = -0.005, y = -223.99108), DrawAction(1), DrawAction(3, x = -775.95926, y = -256.00573)]]

if use_PI:
    questions = [
        {
            'type': 'checkbox',
            'message': 'Select what you want to do:',
            'name': 'actions',
            'choices': [
                Separator('= Inputs ='),
                {
                    'name': 'File',
                    'disabled': 'not implemented'
                },
                {
                    'name': 'Remote',
                    'disabled': 'not implemented'
                },
                {
                    'name': 'Tests'
                },
                Separator('= Converting ='),
                {
                    'name': 'Gcode'
                },
                {
                    'name': 'Image',
                    'disabled': 'not implemented'
                },
                Separator('= Printing ='),
                {
                    'name': 'To printer',
                    'checked': True
                },
                {
                    'name': 'To file'
                }
            ],
            'validate': lambda answer : 'You must choose at least one action.' if len(answer['actions']) == 0 else True
        }
    ]

    answers = prompt(questions, style=custom_style_3)

else:
    answers = {'actions': []}

    print('Use PyInquirer for better UI')
    usr_input = input('Press (1) to print from file, (2) for remote, (3) to test a example, (0) to skip: ')
    if usr_input == '1':
        answers['actions'].append('File')
    elif usr_input == '2':
        answers['actions'].append('Remote')
    elif usr_input == '3':
        answers['actions'].append('Tests')
        usr_input = input('Press (1) for a circle, (2) for a page tester, (3) to test a advanced example: ')
        if usr_input == '1':
            example = 0
        elif usr_input == '2':
            example = 1
        elif usr_input == '3':
            example = 2

    usr_input = input('Press (1) to convert from Gcode, (2) to convert a Image, (0) to skip: ')
    if usr_input == '1':
        answers['actions'].append('Gcode')
    elif usr_input == '2':
        answers['actions'].append('Image')

    usr_input = input('Press (1) to print, (2) to write to file, (0) to skip: ')
    if usr_input == '1':
        answers['actions'].append('To printer')
    elif usr_input == '2':
        answers['actions'].append('To file')

pprint(answers)

if 'Tests' in answers['actions']:
    print_data_converted = demo[example]

if 'Gcode' in answers['actions']:
    if not 'Tests' in answers['actions']:
        #Convert
        None

#elif 'Gcode' in answers['actions']:
#

if 'To printer' in answers['actions']:
    if use_printer:
        plott3r = Plott3r()

        plott3r.reset_motors()
        plott3r.calibrate()
        plott3r.draw(print_data_converted)

    else:
        print('This program is not running on a plotter')
