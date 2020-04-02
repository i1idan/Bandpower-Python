def bandpower(data, fs, freqrange):
    
    """Average Power in input signal x.

    **********
    Parameters
    **********
    
    data :Input signal(Time series).
    fs : Sampling frequency.
    frqrange: Frequency range for band power computation.
    """
    
    import numpy as np
    import os
    print(os.listdir())
    from scipy.signal import welch
    from scipy.integrate import simps
    
    
    freqrange= np.asarray(freqrange)
    low, high = freqrange

    
    freqs, psd = welch(data, fs)

    
    freqrange_idx= np.logical_and(freqs >= low, freqs <= high)

    bp = simps(psd[freqrange_idx])

    return bp

