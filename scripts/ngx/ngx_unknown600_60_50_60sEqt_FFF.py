#!Measurement
'''
default_fits: nominal
'''

def main():
    info('measurement script')

    activate_detectors('H4','H2','Ax','L3','L5')

    position_magnet('Ar40', detector='H4')

    equilibrate(eqtime=60, inlet='MSI', outlet='PIV', delay=3)

    set_time_zero()

    sniff(30)
    set_fits()
    set_baseline_fits()

    sleep(15)
    #multicollect on active detectors
    multicollect(ncounts=12, integration_time=50)

    baselines(ncounts=60, 
                  mass=37.5, 
                  detector='AX',
                  use_dac=True,
                  settling_time=10)
    
    activate_detectors('H4', **{'peak_center':True})

    if analysis_type=='blank':
        info('this is a blank. no center')
    else:
        peak_center(detector='H4',isotope='Ar40', integration_time=1)

    