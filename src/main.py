import openmc
import os
import sys
import argparse
from simulation_registry import simulations


openmc.config['cross_sections'] = os.environ['OPENMC_CROSS_SECTIONS']



def run_simulation(sim_name, out_dir, options):

    # Create the 'generated' directory if it doesn't exist
    generated_dir = os.path.join(out_dir, sim_name + "-example", "generated")
    os.makedirs(generated_dir, exist_ok=True)

    # Change working directory to the 'generated' folder
    original_dir = os.getcwd()
    os.chdir(generated_dir)

    try:
        sim = simulations[sim_name]
        # Run the simulation
        model = sim['model_fn'](options)
        model.run()

        # Run the analysis function if it's there
        if 'analysis_fn' in sim:
            sim['analysis_fn'](options)
    finally:
        # Change back to the original directory
        os.chdir(original_dir)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Run a simulation with specified parameters.")

    parser.add_argument("sim_name", help="Name of the simulation")
    parser.add_argument("-o", "--out_dir", default="results", help="Directory to save output files (default: results)")

    args, remaining = parser.parse_known_args()

    out_dir = args.out_dir
    sim_name = args.sim_name
    if sim_name not in simulations:
        raise Exception(f"Simulation '{sim_name}' not found.")

    sim = simulations[sim_name]

    if 'options' in sim:
        for opt in sim['options']:
            parser.add_argument(*opt['args'], **opt['kwargs'])
        args = parser.parse_args()
       
    # Run the simulation
    run_simulation(sim_name, out_dir, args)
