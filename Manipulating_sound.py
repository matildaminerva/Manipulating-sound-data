import sys
import copy
from math import *
import numpy as np
from numpy.linalg import inv, eig
import matplotlib.pyplot as plt
import scipy.fftpack

def read_whole_data_from_file(filename):
    ###########################################################################
    ## With this function the file that contains time in first and amplitude ##
    ## of sound in second column can be read. We parse from the original     ##
    ## data the columns into two numpy arrays.                               ##
    ###########################################################################
    f = file(filename)
    lines = f.readlines()
    f.close()
    
    time = []
    sound = []
    
    for line in lines:
        parts = line.split()
        if len(parts) > 0:
            time.append( float(parts[0]) )
            sound.append( float(parts[1]) )
            

    return np.array( time ), np.array( sound )

def parse_data(time, sound, beginning_time, end_time): 
    ##########################################################################
    ## Here the data (time and sound arrays) are parsed via beginning and   ##
    ## ending time. So for example if we only want to use half minute period##
    ## in the middle of the five minute sound, we can parse it with this    ##
    ## function.                                                            ##
    ##########################################################################
    
    
    new_time= []
    new_sound= []

    i = list(time).index(beginning_time)
    while (time[i] < end_time):
    
        new_time.append(time[i])
        new_sound.append(sound[i])
        i = i+1
    
    return new_time, new_sound
    


def filter_data(sound, level):
    
    filtered_sound =[]
    
    for i in range(len(sound)):
        if sound[i] > level:
            filtered_sound.append(sound[i])
            
        else:
            filtered_sound.append(0)
    
    
    return filtered_sound
 
def fourier_transform(sound):
    #########################################################################
    ## In this function the fourier transform is performed to wanted part  ##
    ## of the sound-data and then it is divided into two parts, because fft##
    ## gives us mirrored fourier transform.                                ##
    #########################################################################
    
    fouriered_sound = scipy.fftpack.fft(sound)
    
    first_half_of_the_fouriered = []
    second_half_of_the_fouriered = []
    
    for i in range(len(sound)):
        if i < len(sound)/2:
            first_half_of_the_fouriered.append(fouriered_sound[i])
        else:
            second_half_of_the_fouriered.append(fouriered_sound[i])
            
    return first_half_of_the_fouriered, second_half_of_the_fouriered
    
    
    
    
def main(args):
    
    name_of_the_file = input("Write here the name of the file of txt-file (has to be in the same place as the code):")
    time, sound = read_whole_data_from_file('maitovalaat.txt')
    Fs=24000
    
    #x, y = fourier_transform(sound)
    
    
    new_time, new_sound = parse_data(time, sound, 96.7, 96.9 )
    
    #plt.plot(time, sound)
    #plt.xlabel('Aika (s)')
    #plt.ylabel('Amplitudi')
    #plt.savefig('whales.pdf',bbox_inches = 'tight')
    #plt.show()
    
    # a=63-64, b=84-85 ja c= 96-97
    
    plt.specgram(new_sound, Fs=24000, cmap='jet')
    plt.xlabel('Aika (s)')
    plt.ylabel('Taajuus (Hz)')
    cbar = plt.colorbar()
    cbar.ax.set_ylabel('Intensiteetti (dB)')
    plt.clim(-175, -55)
    plt.plot([0.041, 0.041], [2000, 11000], 'k-', lw=1)
    plt.plot([0.125, 0.125], [2000, 11000], 'k-', lw=1)
    plt.savefig('spectrogrammiauttakaa.pdf',bbox_inches = 'tight')
    plt.show()
    
  
    

    
if __name__ == "__main__":
    main(sys.argv[1:])
    
 #; Sample Rate 24000
#; Channels 1
         
 #Fourier-muunnos
 #signal to noise-ratio
 #kohinanpoisto
 #np.meanydata tai jotain saa keskiarvot

# erilaiset fourier-muunnokset eri kohdista dataa
# aaltojen aikatiheys

