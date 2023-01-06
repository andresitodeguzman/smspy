##
## DYNAMIC
##

## Import the module explicitly (import dynamics.<module_name> as module_name)
import dynamics.root as root
import dynamics.srph as srph

##  Register all modules for checking here. If something interferes, rearrange the order
##  module_name_ = module_name.do(params)
def responseQuery(number, body):
    
    # Available params
    n = number
    b = body

    # Do actions
    root_ = root.do(n,b)
    srph_ = srph.do(n,b)

    if root_:
        return root_
    if srph_:
        return srph_
    else:
        # Returns False if all actions returns False
        return False
