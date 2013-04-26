
# Convert list of comma-separated strings into a list of integers showing
#  the rank of each argument and a list of sets of tuples.  Each set
#  shows dimensions of arguments that must match by indicating a 2-tuple
#  where the first integer is the argument number (output is argument 0) and
#  the second integer is the dimension
# Example:  If the rank-signature is ['M,L', 'L,K', 'K', '']
#           then the list of integer ranks is [2, 2, 1, 0]
#           while the list of connections is [{(0,1),(1,0)},{(1,1),(2,0)}]

def process_signature(ranksignature):
    ranklist = [0 if not arg else len(arg.split(',')) for arg in ranksignature]

    varmap = {}
    for i, arg in enumerate(ranksignature):
        if not arg: continue
        for k, var in enumerate(arg.split(',')):
            varmap.setdefault(var,[]).append((i,k))

    connections = [set(val) for val in varmap.values() if len(val) > 1]
    return ranklist, connections

# Process type-table dictionary which maps a signature list with
#   (output-type, input-type1, input-type2) to a kernel into a
#   lookup-table dictionary which maps a input-only signature list
#   with a tuple of the output-type plus the signature
def process_typetable(typetable):
    newtable = {}
    for key, value in typetable:
        newtable[key[1:]] = (key[0], value)
        
# Define the Blaze Function
#   * A Blaze Function is a callable that takes Concrete Arrays and returns
#        Deferred Concrete Arrays
#   * At the core of the Blaze Function is a kernel which is a type-resolved
#        element-wise expression graph where elements can be any contiguous
#        primitive type (right-most part of the data-shape)
#   * Kernels have a type signature which we break up into the rank-signature
#       and the primitive type signature because a BlazeFunc will have one
#       rank-signature but possibly multiple primitive type signatures.
#   * Kernels for a particular type might be inline jitted or loaded from
#       a shared-library 
#   * Example BlazeFuncs are sin, svd, eig, fft, sum, prod, inner1d, add, mul
#       etc --- kernels all work on in-memory "elements"
      
class BlazeFunc(object):
    def __init__(self, ranksignature, typetable):
        """
        Construct a Blaze Function from a rank-signature and keyword arguments.

        The keyword arguments are typenames with values as the kernel.  Kernels
        can be written in many ways:  "blir" string, python function (will be
        jitted by numba), ctypes function, cffi functions, etc.

        Arguments
        =========
        ranksignature : ['name1,M', 'M,name3', 'L']
                        a list of comma-separated strings where names indicate
                        unique sizes.  The first argument is the rank-signature
                        of the output.  An empty-string or None means a scalar.

        typetable :  dictionary mapping argument types to an implementation
                     kernel
        """
        self.ranks, self.rankconnect = process_signature(ranksignature)
        self.dispatch = process_types(typetable)

    @property
    def nin(self):
        return len(self.ranks)-1


    def __call__(self, *args):
        # convert inputs to Concrete Arrays
        # 


    
        
        
