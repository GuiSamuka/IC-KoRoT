"""

    This module defines a LightCurve

"""
from . import data_viz
from . import filter_helper


__all__ = ["LightCurve"]


class LightCurve():
    """
    Explicação...

    Parameters
    ----------
    time : numpy ndarray
        Time values

    flux : numpy ndarray
        Flux values, related to every time point.

    """

    # Constructor of the `LightCurve` class
    _required_columns = ["time", "flux"]

    def __init__(self, time=None, flux=None):
        self.time = time
        self.flux = flux

    def plot(self):
        """
        Plot the LightCurve using utils.Data_Viz's `~utils.data_viz.view_lightcurve` method. 
        """
        data_viz.view_lightcurve(self.time, self.flux)

    def ideal_lowpass_filter(self, cutoff_freq, numExpansion=70):
        return filter_helper.apply_filter(self.time, self.flux, filter_technique='ideal', cutoff_freq=cutoff_freq, numExpansion=numExpansion)
        
    def gaussian_lowpass_filter(self, cutoff_freq, numExpansion=70):
        return filter_helper.apply_filter(self.time, self.flux, filter_technique='gaussian', cutoff_freq=cutoff_freq, numExpansion=numExpansion)

    def butterworth_lowpass_filter(self, order, cutoff_freq, numExpansion=70):
        return filter_helper.apply_filter(self.time, self.flux, filter_technique='butterworth', order=order, cutoff_freq=cutoff_freq, numExpansion=numExpansion)

    def bessel_lowpass_filter(self, order, cutoff_freq, numExpansion=70):
        return filter_helper.apply_filter(self.time, self.flux, filter_technique='bessel', order=order, cutoff_freq=cutoff_freq, numExpansion=numExpansion)

    def median_filter(self, numNei, numExpansion=70):
        return filter_helper.apply_filter(self.time, self.flux, filter_technique='median', numNei=numNei, numExpansion=numExpansion)


class FilteredLightCurve():
    """
    Explicação...

    Parameters
    ----------
    time : numpy ndarray
        Time values

    flux : numpy ndarray
        Flux values, related to every time point.

    filtered_flux : numpy ndarray
        Filtered flux values, related to every time point.

    """

    # Constructor of the `LightCurve` class
    _required_columns = ["time", "flux", "filtered_flux", "filter_technique", "cutoff_freq", "order", "numNei"]

    def __init__(self, time=None, flux=None, filtered_flux=None, filter_technique="", cutoff_freq=None, order=None, numNei=None):
        self.time = time
        self.flux = flux
        self.filtered_flux = filtered_flux
        self.filter_technique = filter_technique
        self.cutoff_freq = cutoff_freq
        self.order = order
        self.numNei = numNei
        

    def view_filter_results(self):
        """
        Plot the LightCurve using utils.Data_Viz's `~utils.data_viz.view_filter_results` method. 
        """
        data_viz.view_results(self.time, self.flux, self.filtered_flux, self.filter_technique, self.cutoff_freq, self.order, self.numNei)

    def getFilteredFlux(self):
        return self.filtered_flux

