import numpy as np

filename = 'input.txt'
width = 25
height = 6

data = [int(c) for c in open( filename ).readline().strip() ]

data_array = np.array(data).reshape(( len( data ) // width , width ) )

min_zero_count = width * height + 1
result = 0

for y_start in range( ( len( data ) // width ) // height ):

    larr = data_array[ y_start * height : ( y_start * height ) + height ]

    num_zeros = larr[ larr == 0 ].shape[ 0 ]

    if num_zeros < min_zero_count:
        min_zero_count = num_zeros

        num_ones  = larr[ larr == 1 ].shape[ 0 ]
        num_twos  = larr[ larr == 2 ].shape[ 0 ]
        
        result = num_ones * num_twos

print(result)
