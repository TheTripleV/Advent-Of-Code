import numpy as np

filename = 'input.txt'
width = 25
height = 6

data = [int(c) for c in open( filename ).readline().strip() ]

data_array = np.array(data).reshape(( len( data ) // width , width ) )

output = np.zeros((height, width), dtype=int) + 2


for y_start in range( (len(data) // width) // height ):
    larr = data_array[ y_start * height : ( y_start * height ) + height ]
    output[ output == 2 ] = larr[ output == 2 ]

print(output)

for y in range(output.shape[0]):
    for x in range(output.shape[1]):
        if output[y,x] == 1:
            print(chr(9608), end='')
        else:
            print(' ', end='')
    print()