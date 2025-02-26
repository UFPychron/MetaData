#!Measurement
'''
default_fits: nominal
'''

def main():
    info('measurement script')

    activate_detectors('H5','H3','H1','L2','L4')

    position_magnet('Ar40', detector='H5')

    equilibrate(eqtime=30, inlet='MSI', outlet='PIV', delay=3)

    set_time_zero()

    sniff(25)
    set_fits()
    set_baseline_fits()

    sleep(15)
    #multicollect on active detectors
    multicollect(ncounts=30, integration_time=20)

    baselines(ncounts=60, 
                  mass=37.5, 
                  detector='AX',
                  use_dac=True,
                  settling_time=10)
    
    activate_detectors('H5', **{'peak_center':True})

    if analysis_type=='blank':
        info('this is a blank. no center')
    else:
        peak_center(detector='H5',isotope='Ar40', integration_time=1)

    