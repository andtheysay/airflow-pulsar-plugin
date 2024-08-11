import os
import sys
from setuptools import Distribution

def build(setup_kwargs):
    """This function is mandatory in order to build the extensions."""
    # Force the package to be platform-specific
    distribution = Distribution(attrs=setup_kwargs)
    distribution.has_ext_modules = lambda: True
    
    # Set the platform tag
    if sys.platform.startswith('linux'):
        distribution.plat_name = 'linux_x86_64'
    
    setup_kwargs.update({
        'distclass': distribution.__class__,
        'ext_modules': [],  # Add any actual extensions here if you have them
    })