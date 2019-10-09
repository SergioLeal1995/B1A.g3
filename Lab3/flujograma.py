#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Lo de arriba es para que los IDE conozcan en que esta escrito este codigo 
###########################################################
# Puedes encontrar este codigo como objeto_ej2.py en:    ##
# https://sites.google.com/saber.uis.edu.co/comdig/sw    ##
###########################################################
###           IMPORTACION DE LIBRERIAS                  ###
###########################################################
 
# Libreria obligatoria
from gnuradio import gr
from gnuradio import audio
 
# Librerias particulares
from gnuradio import analog
from gnuradio import blocks
from gnuradio.filter import firdes
 
# Librerias para poder incluir graficas tipo QT
from gnuradio import qtgui
from PyQt4 import Qt # si no se acepta PyQt4 cambie PyQt4 por PyQt5
import sys, sip
 
###########################################################
###           LA CLASE DEL FLUJOGRAMA                   ###
###########################################################
class flujograma(gr.top_block):
    def __init__(self):
        gr.top_block.__init__(self)
 
        ################################################
        ###   EL FLUJOGRAMA                          ###
        ################################################
 
        # Las variables
        samp_rate = 32000
        fftsize = 2048
	ampl = 8
 
        # Los bloques
        self.src0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 350, ampl)
	self.src1 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 440, ampl)
	self.dst = audio.sink(samp_rate, ""	)
        #self.nse = analog.noise_source_c(analog.GR_GAUSSIAN, 0.1)
        self.add = blocks.add_ff(vlen=1)
        self.thr = blocks.throttle(4, samp_rate,True)
        self.snk = qtgui.sink_f(
            fftsize, #fftsize
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
        )
 
        # Las conexiones
        self.connect(self.src0, (self.dst, 0))
        self.connect(self.src1, (self.dst, 1))
	self.connect(self.src0, (self.add, 0))
	self.connect(self.src1, (self.add, 1))
        self.connect(self.add, self.thr, self.snk)
 
        # La configuracion para graficar
        self.pyobj = sip.wrapinstance(self.snk.pyqwidget(), Qt.QWidget)
        self.pyobj.show()
 
###########################################################
###                LA CLASE PRINCIPAL                   ###
###########################################################
def main():
    # Para que lo nuestro sea considerado una aplicación tipo QT GUI
    qapp = Qt.QApplication(sys.argv)
    tb= flujograma()
    tb.start()
    # Para arranque la parte grafica
    qapp.exec_()
 
# como el main lo hemos puesto como una funcion, ahora hay que llamarla
# podriamos escibir simplemete main(), pero es mas profesional asi:
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
