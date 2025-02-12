#!Measurement
'''
default_fits: nominal
'''

def main():
    info('measurement script')


    activate_detectors('H5','H3','H1','L2','L4')

    position_magnet('Ar40', detector='H5')

    
    eqt = 30

    equilibrate(eqtime=eqt, inlet='MSI', outlet='PIV', delay=3)

    set_time_zero()

    sniff(eqt)
    set_fits()
    set_baseline_fits()

    #multicollect on active detectors
    multicollect(ncounts=12, integration_time=50)

    baselines(ncounts=60, 
                  mass=37.5, 
                  detector='AX',
                  use_dac=True,
                  settling_time=10)
    
    
    activate_detectors('H5', **{'peak_center':True})

    peak_center(detector='H5',isotope='Ar40', integration_time=1)

    