import time
from collections import defaultdict

# Class for CPU
class CPU:
    #instruction set
    data = None

    #instruction pointer
    curr_pos = 0

    #temp registers
    op = None
    modes = [ -1, 0, 0, 0 ]
    params_pos = [ -1, 0, 0, 0 ]
    slow = 0

    simulated_inputs = []
    simulated_outputs = []

    simulate_outputs_flag = False

    #flags
    FINISHED = False
    ERR = 0
    LOG = False
    JMP = False

    instr_size_d = defaultdict( lambda: 1 )
    instr_size_d[ 1 ] = 4
    instr_size_d[ 2 ] = 4
    instr_size_d[ 3 ] = 2
    instr_size_d[ 4 ] = 2
    instr_size_d[ 5 ] = 3
    instr_size_d[ 6 ] = 3
    instr_size_d[ 7 ] = 4
    instr_size_d[ 8 ] = 4

    # stub
    def __init__( self ):
        pass

    # Enable / Disable Extra Logging to Console
    def set_logging( self, to_log ):
        self.LOG = to_log

    # Enable Slow Mode
    def set_slow( self, slow ):
        self.slow = slow

    # Process the op code / modes for the current instruction
    def process_instr( self ):
        instr = str( self.data[ self.curr_pos ] )

        self.op = int( instr[ -2: ] )

        self.modes[ 1 ], self.modes[ 2 ], self.modes[ 3 ] = 0, 0, 0

        if len( instr ) == 5:
            self.modes[ 3 ] = int( instr[ 0 ] )
            instr = instr[ 1: ]
        if len( instr ) == 4:
            self.modes[ 2 ] = int( instr[ 0 ] ) 
            instr = instr[ 1: ]
        if len( instr ) == 3:
            self.modes[ 1 ] = int( instr[ 0 ] ) 
    
    # Get the paramters for the current instructions
    def get_params( self ):
        l = len( data )
        for parnum in [ 1, 2, 3 ]:
            if self.curr_pos + parnum < l:
                if self.modes[ parnum ] == 0:
                    self.params_pos[ parnum ] = self.data[ self.curr_pos + parnum ]
                elif self.modes[ parnum == 1 ]:
                    self.params_pos[ parnum ] = self.curr_pos + parnum

    # Set Instruction Set
    def set_instructions( self, instructions, copy=False ):
        self.data = instructions.copy( ) if copy else instructions
        self.data_backup = data.copy( )

    def set_simulated_inputs( self, inputs ):
        self.simulated_inputs = inputs.copy( )

    def set_simulated_outputs( self, flag ):
        self.simulate_outputs_flag = flag

    def get_outputs( self ):
        return self.simulated_outputs

    # Reset the CPU to initial state
    def reset( self ):
        self.FINISHED = False
        self.curr_pos = 0
        self.ERR = 0
        self.simulated_inputs = []
        self.simulated_outputs = []

    # Run all instructions ( Program Counter )
    def run( self ):
        while not self.FINISHED:
            self.step( )
            time.sleep( self.slow )

    #Run Next Instruction
    def step( self ):
        self.JMP = False
        self.ERR = False

        self.process_instr( )
        self.get_params( )

        if self.LOG: self.log( )
            
        if self.op == 1: # add
            self.data[ self.params_pos[ 3 ] ] = self.data[ self.params_pos[ 1 ] ] + self.data[ self.params_pos[ 2 ] ]
        
        elif self.op == 2: # mul
            self.data[ self.params_pos[ 3 ] ] = self.data[ self.params_pos[ 1 ] ] * self.data[ self.params_pos[ 2 ] ]

        elif self.op == 3:
            if len(self.simulated_inputs) > 0:
                self.data[ self.params_pos[ 1 ] ] = self.simulated_inputs.pop(0)
            else:
                self.data[ self.params_pos[ 1 ] ] = int( input( "INPUT>> " ) )
        
        elif self.op == 4:
            if self.simulate_outputs_flag:
                self.simulated_outputs.append( self.data[ self.params_pos[ 1 ] ] )
            else:
                print( 'OUTPUT>>', self.data[ self.params_pos[ 1 ] ] )

        elif self.op == 5:
            if self.data[ self.params_pos[ 1 ] ] != 0:
                self.curr_pos = self.data[ self.params_pos[ 2 ] ]
                self.JMP = True

        elif self.op == 6:
            if self.data[ self.params_pos[ 1 ] ] == 0:
                self.curr_pos = self.data[ self.params_pos[ 2 ] ]
                self.JMP = True

        elif self.op == 7:
            if self.data[ self.params_pos[ 1 ] ] < self.data[ self.params_pos[ 2 ] ]:
                self.data[ self.params_pos[ 3 ] ] = 1
            else:
                self.data[ self.params_pos[ 3 ] ] = 0

        elif self.op == 8:
            if self.data[ self.params_pos[ 1 ] ] == self.data[ self.params_pos[ 2 ] ]:
                self.data[ self.params_pos[ 3 ] ] = 1
            else:
                self.data[ self.params_pos[ 3 ] ] = 0

        elif self.op == 99:
            self.FINISHED = True
            self.ERR = 0

        else:
            print( 'BAD INSTRUCTION: ', self.op )
            self.ERR = 1
            self.FINISHED = True

        if not self.JMP: self.curr_pos += self.instr_size_d[ self.op ]

    def log( self ):
        mode_str = '{}'.format( self.modes[ 1: ] )
        instr_str = ''
        asm_str = ''
        c_str = ''
        instr_str = '{}'.format( data[ min( self.curr_pos, len( data ) ): self.curr_pos + min( self.instr_size_d[ self.op ], len( data ) - 1 ) ] )

        if self.op == 1:
            asm_str = 'add $r{}, $r{}, $r{}'.format( self.params_pos[ 3 ], self.params_pos[ 1 ], self.params_pos[ 2 ] )
            c_str = 'r[ {} ] = r[ {} ] + r[ {} ]'.format( self.params_pos[ 3 ], self.params_pos[ 1 ], self.params_pos[ 2 ] )
        elif self.op == 2:
            asm_str = 'mul $r{}, $r{}, $r{}'.format( self.params_pos[ 3 ], self.params_pos[ 1 ], self.params_pos[ 2 ] )
            c_str = 'r[ {} ] = r[ {} ] * r[ {} ]'.format( self.params_pos[ 3 ], self.params_pos[ 1 ], self.params_pos[ 2 ] )
        elif self.op == 3:
            asm_str = 'li $r{}, {}'.format( self.params_pos[ 1 ], 'input' )
            c_str = 'r[ {} ] = {}'.format( self.params_pos[ 1 ], 'input' )
        elif self.op == 4:
            asm_str = 'add $v0, $r{}, $0'.format( self.params_pos[ 1 ] )
            c_str = 'printf( r[ {} ] )'.format( self.params_pos[ 1 ] ) 
        elif self.op == 5:
            asm_str = 'bnez $r{}, $r{}'.format( self.params_pos[ 1 ], self.params_pos[ 2 ] )
            c_str = 'if( r[ {} ] ) goto r[ {} ]'.format( self.params_pos[ 1 ], self.params_pos[ 2 ] )
        elif self.op == 6:
            asm_str = 'bneq $r{}, $r{}'.format( self.params_pos[ 1 ], self.params_pos[ 2 ] )
            c_str = 'if( !r[ {} ] ) goto r[ {} ]'.format( self.params_pos[ 1 ], self.params_pos[ 2 ] )
        elif self.op == 7:
            asm_str = 'slt $r{}, $r{}, $r{}'.format( self.params_pos[ 3 ], self.params_pos[ 1 ], self.params_pos[ 2 ] )
            c_str = 'r[ {} ] = r[ {} ] < r[ {} ]? 1: 0'.format( self.params_pos[ 3 ], self.params_pos[ 1 ], self.params_pos[ 2 ] )
        elif self.op == 8:
            asm_str = 'seq $r{}, $r{}, $r{}'.format( self.params_pos[ 3 ], self.params_pos[ 1 ], self.params_pos[ 2 ] ) #didn't feel like righting out the right stuff
            c_str = 'r[ {} ] = r[ {} ] == r[ {} ]? 1: 0'.format( self.params_pos[ 3 ], self.params_pos[ 1 ], self.params_pos[ 2 ] )
        elif self.op == 99:
            asm_str = 'jr $ra'
            c_str = 'exit( 0 )'
        else:
            asm_str = 'BAD OP'
            c_str = 'exit( 1 )'

        print( 'PC {:>3} || op: {:>3} || mode: {:<9} || instr: {:<25} || asm: {:<25} || C: {:<25}'.format( self.curr_pos, self.op, mode_str, instr_str, asm_str, c_str ) )
        # print( 'modes:', self.modes[ 1: ], '|| inst:', data[ self.curr_pos : min( self.curr_pos + 4, len( data ) ) ], '|| ', end='' )


if __name__ == "__main__":

    from itertools import permutations

    filename = 'input.txt'
    data = [ int( x ) for x in open( filename, 'r' ).readline( ).split( ',' ) ]

    phase_sequence_base = [ 4, 3, 2, 1, 0 ]

    phase_sequences = list( permutations( phase_sequence_base ) )
    
    cpu = CPU()
    cpu.set_simulated_outputs( True )

    max_signal = 0

    for phase_sequence in phase_sequences:

        output = 0
        for i in range( len( phase_sequence ) ):
            cpu.reset()
            cpu.set_instructions( data, copy=True )
            cpu.set_simulated_inputs( [ phase_sequence[ i ], output ] )
            cpu.run()
            output = cpu.get_outputs()[ 0 ]

        max_signal = max( output, max_signal )

    print( max_signal )
