#===============================================================================
# EXTRACTION SCRIPT ngx_blank_sample_chamber.py
#===============================================================================
def main():
    # Single airshot, not designed to be part of a run sequence
 


    # write a message to the console (and log it)
    info('this a single manual air shot')

    # Ensure appropriate valves on line are closed
    close('PCVO')
    close('PCVI')
    close('PSV')
    close('CFV')
    close('MSI')

    # open valve CV and IPV valves to pump down line
    open('CV')
    open('CFV')
    open('IPV')

    # wait 3 seconds
    sleep(3)

    # pump down rest of line
    # open PSV
    open('PSV')
    # wait 3 seconds
    sleep(3)
    # open PCVI
    open('PCVI')
    # wait 180 seconds
    sleep(180)
    # close PCVI
    close('PCVI')
    # wait 3 seconds
    sleep(3)
    # close IPV
    close('IPV')
    # wait 3 seconds
    sleep(3)
    # open PCVI to let shot into line
    open('PCVI')
    # wait 60 s to let equilibrate
    sleep(60)
    # close PCVI
    close('PCVI')


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