
import matplotlib.pyplot as mplot
import matplotlib as mplib
import numpy as npy


bdepth = 8
Vref = 3.3
N_markers = 100


settings = npy.loadtxt( "settings.txt", dtype = float )
d_data = npy.loadtxt( "data-22.05.04-15.49.03.txt", dtype = int ) #digital data (0-255)

samplerate = settings[0]
quantization = settings[1]
size = d_data.size
a_data = d_data / ( 2 ** bdepth ) * Vref #analog data (0V - Vref V)
period = 1 / samplerate
maxtime = period * d_data.size
datatime = npy.linspace( 0, maxtime , num = d_data.size )
chargetime = d_data.argmax() * period / 1000
unchargetime = max( datatime )/1000 - chargetime

print('samplerate = {}'.format( samplerate ))
print('quantization = {}'.format( quantization ))
print('d_data = {}'.format( d_data ))
print('a_data = {}'.format( a_data ))
print('period = {}'.format( period ))
print('maxtime = {}'.format( maxtime ))
print('size = {}'.format( d_data.size ))
print('datatime = {}'.format( datatime ))


fig, ax = mplot.subplots( figsize = (16, 10), dpi = 200 ) #layout = "constrained"
ax.set_title( "Процесс зарядки-разрядки конденсатора", wrap = True )
ax.set_xlabel( "Время t, с" )
ax.set_ylabel( "Напряжение U, В" )
ax.set_xlim( 0, maxtime )
ax.set_ylim( 0, max( a_data ) * 1.1 )
ax.text( chargetime + maxtime / 15, 0.8 * max( a_data ), f"Время заряда: {chargetime:.2f} с\n\nВремя разряда: {unchargetime:.2f} с", fontsize = 20, color = "black" )
ax.minorticks_on()
ax.grid( True )
ax.grid( True, "minor", ls = ":" )
#ax.xaxis.set_major_locator( NullLocator )
markrate = int( size / N_markers )
ax.plot( datatime, a_data, marker = 'o', markersize = 5, markeredgecolor = "blue", markevery = 0.2, color = "blue", alpha = 1, linewidth = 0.6, linestyle = "--", label = "V=V(t)" )
ax.legend()
fig.savefig( "graph.png" )
fig.savefig( "graph.svg" )
#mplot.show()