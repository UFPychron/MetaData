#===============================================================================
# EXTRACTION SCRIPT ngx_co2.py
#===============================================================================
def main():
    # Single airshot, not designed to be part of a run sequence
 
    # write a message to the console (and log it)
    info('this a test co2 shot')

    # Ensure appropriate valves on line are closed
    close('PCVO')
    close('PCVI')
    close('PSV')
    close('CFV')
    close('MSI')

    # open valve CV and IPV valves to pump down line
    open('CV')
    open('IPV')

    # wait 3 seconds
    sleep(3)

    # pump down rest of line

    if analysis_type=='blank':
        info('analysis is a blank. not firing the laser')
        sleep(duration)
    else:
        begin_interval(duration)   # duration is Extract Duration in the experiment editor
    
        # do extraction of gas 
        for pi in position:
            move_to_position(pi)
            #warmup(block=True)
            extract()
        complete_interval()
        

    # wait 3 seconds
    sleep(3)

    # close CV
    close('CV')
    sleep(3)
    # open CFV to let shot into line
    open('CFV')
    # wait 60 s to let equilibrate
    sleep(cleanup)
    # close IPV
    close('IPV')
    # open CV
    open('CV')
    sleep(60)

    # Done!
#===============================================================================
# POST EQUILIBRATION SCRIPT ngx_pump_extractionline.py
#===============================================================================
def main():
    info('post equilibration')
    open('IPV')

    
#===============================================================================
# POST MEASUREMENT SCRIPT ngx_pump_ms.py
#===============================================================================
def main():
    info('post measurement. pumping out mass spec')
    open('PIV')