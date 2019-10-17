from gnuradio import gr
import numpy as np
 
####################################################
##     Plantilla: clase e_add_cc                  ##
####################################################

 
class e_add_cc(gr.sync_block):  

    def __init__(self, escala=0.5):

        gr.sync_block.__init__(
            self,
            name='Plantilla_para_crear_bloques_cc', 
            in_sig=[np.complex64,np.complex64], 
            out_sig=[np.complex64]
        )
        self.escala=escala
        self.coef = 1.0
    def work(self, input_items, output_items):
        in0 = input_items[0]
        in1 = input_items[1]
        out0 = output_items[0]
        out0[:]=(in0+in1)*self.escala/self.coef
        return len(out0)

####################################################
##     clase e_add_ff                             ##
####################################################
class e_add_ff(gr.sync_block):  

    def __init__(self, escala=0.5):
 
        gr.sync_block.__init__(
            self,
            name='e_add_ff', 
            in_sig=[np.float32,np.float32], 
            out_sig=[np.float32]
        )
        self.escala=escala
    def work(self, input_items, output_items):
        in0 = input_items[0]
        in1 = input_items[1]
        out0 = output_items[0]
        out0[:]=(in0+in1)*self.escala
        return len(out0)

####################################################
##     clase e_vector_fft_ff                      ##
####################################################
# En color rojo aparece aquello que hace que el bloque sea vectorial
class e_vector_fft_ff(gr.sync_block):
    """calcula la fft en magnitud a una senal vectorial de N muestras y emtrega N muestras del espectro. N deber ser potencia de 2"""
 
    def __init__(self, N=128):  
        gr.sync_block.__init__(
            self,
            name='e_vector_fft_ff',   
            in_sig=[(np.float32,N)],
            out_sig=[(np.float32,N)]
        )
        self.N = N
 
    def work(self, input_items, output_items):
        in0 = input_items[0]
        out0 = output_items[0]
        out0[:]=abs(np.fft.fftshift(np.fft.fft(in0,self.N),1)) 
        return len(output_items[0])	
