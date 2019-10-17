from gnuradio import gr
import numpy as np
 

 
####################################################
##     clase e_add_ff                             ##
####################################################
#bloque de entradas y salidas reales de tipo flotante
class e_add_ff(gr.sync_block):  

     
    def __init__(self, escala=0.5):
 
        gr.sync_block.__init__(
            self,
            name='e_add_ff', #bloque de entrada y salida real y flotante
            in_sig=[np.float32,np.float32], #input real float signal
            out_sig=[np.float32] # output real float signal
        )
        self.escala=escala #entrada proxima como parametro del bloque

    def work(self, input_items, output_items):
        in0 = input_items[0]
        in1 = input_items[1]
        out0 = output_items[0]
        out0[:]=(in0+in1)*self.escala
        return len(out0)

