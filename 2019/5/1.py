import time


# Class for CPU
class CPU:
    #instruction set
    data = None

    #instruction pointer
    curr_pos = 0

    #temp registers
    op = None
    modes = [-1, 0, 0, 0]
    params_pos = [-1, 0, 0, 0]
    slow = 0

    #flags
    FINISHED = False
    ERR = 0
    LOG = False

    # stub
    def __init__(self):
        pass

    # Enable / Disable Extra Logging to Console
    def set_logging(self, to_log):
        self.LOG = to_log

    # Enable Slow Mode
    def set_slow(self, slow):
        self.slow = slow

    # Process the op code / modes for the current instruction
    def process_instr(self):
        instr = str( self.data[ self.curr_pos ] )

        self.op = int( instr[ -2: ] )

        self.modes[1], self.modes[2], self.modes[3] = 0, 0, 0

        if len( instr ) == 5:
            self.modes[3] = int( instr[0] )
            instr = instr[1:]
        if len( instr ) == 4:
            self.modes[2] = int( instr[0] ) 
            instr = instr[1:]
        if len( instr ) == 3:
            self.modes[1] = int( instr[0] ) 
    
    # Get the paramters for the current instructions
    def get_params(self):
        l = len(data)
        for parnum in [1, 2, 3]:
            if self.curr_pos + parnum < l:
                if self.modes[parnum] == 0:
                    self.params_pos[parnum] = self.data[self.curr_pos + parnum]
                elif self.modes[parnum == 1]:
                    self.params_pos[parnum] = self.curr_pos + parnum

    # Set Instruction Set
    def set_instructions(self, instructions, copy=False):
        self.data = instructions.copy() if copy else instructions
        self.data_backup = data.copy()

    # Reset the CPU to initial state
    def reset(self):
        self.FINISHED = False
        self.curr_pos = 0
        self.ERR = 0

    # Run all instructions (Program Counter)
    def run(self):
        while not self.FINISHED:
            self.step()
            time.sleep(self.slow)

    #Run Next Instruction
    def step(self):
        self.process_instr()
        self.get_params()

        if self.LOG:
            print(
                'modes:', 
                self.modes, 
                '|| inst:', 
                data[self.curr_pos : min(self.curr_pos + 4, len(data))], 
                '|| ', 
                end='')

        if self.op == 1: # add
            if self.LOG: print('{} = {} + {}'.format(self.params_pos[3], self.params_pos[1], self.params_pos[2]))
            
            self.data[self.params_pos[3]] = self.data[self.params_pos[1]] + self.data[self.params_pos[2]]
            self.curr_pos += 4
        
        elif self.op == 2: # mul
            if self.LOG: print('{} = {} * {}'.format(self.params_pos[3], self.params_pos[1], self.params_pos[2]))

            self.data[self.params_pos[3]] = self.data[self.params_pos[1]] * self.data[self.params_pos[2]]
            self.curr_pos += 4

        elif self.op == 3:
            if self.LOG: print('{} = input'.format(self.params_pos[1]))

            self.data[self.params_pos[1]] = int(input("Enter Input> "))
            self.curr_pos += 2
        
        elif self.op == 4:
            if self.LOG: print('print {}'.format(self.params_pos[1]))

            print(self.data[self.params_pos[1]])
            self.curr_pos += 2

        elif self.op == 99:
            if self.LOG: print('Finished')

            self.FINISHED = True
            self.ERR = 0

        else:
            print('Bad Instruction: ', self.op)
            self.ERR = 1
            self.FINISHED = True


if __name__ == "__main__":
    filename = 'input.txt'
    data = [ int( x ) for x in open( filename, 'r' ).readline().split( ',' ) ]

    cpu = CPU()
    cpu.set_instructions(data)
    # cpu.set_logging(True)
    # cpu.set_slow(0)
    cpu.run()



