from simulations.pincell import pincell
from simulations.pincell import plot_spectrum as pincell_plot_spectrum


simulations = {
    'pincell': {
        'model_fn': pincell.pincell_model,
        'analysis_fn': pincell_plot_spectrum.pincell_analysis,
        'options': [
            {
                'args': ["--plot"],
                'kwargs': {
                    'default': False,
                    'help': "Plot the results",
                    'action': 'store_true'
                }
            },
        ]
    }
}
