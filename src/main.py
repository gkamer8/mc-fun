import openmc

"""

Note: This is placeholder GPT generated code to test installation.

"""

# Create materials
fuel = openmc.Material(name='Fuel')
fuel.add_nuclide('U235', 0.03)
fuel.add_nuclide('U238', 0.97)
fuel.set_density('g/cm3', 10.0)

water = openmc.Material(name='Water')
water.add_nuclide('H1', 2)
water.add_nuclide('O16', 1)
water.set_density('g/cm3', 1.0)

# Create geometry
sphere = openmc.Sphere(r=1.0)
cell = openmc.Cell(fill=fuel, region=-sphere)
outer_cell = openmc.Cell(fill=water, region=+sphere)
geometry = openmc.Geometry([cell, outer_cell])

# Create settings
settings = openmc.Settings()
settings.batches = 100
settings.inactive = 10
settings.particles = 1000

# Create tallies
tallies = openmc.Tallies()
cell_filter = openmc.CellFilter(cell)
tally = openmc.Tally(name='flux')
tally.filters = [cell_filter]
tally.scores = ['flux']
tallies.append(tally)

# Create model and run
model = openmc.model.Model(geometry, materials=[fuel, water], settings=settings, tallies=tallies)
model.run()

# Print results
with openmc.StatePoint('statepoint.100.h5') as sp:
    tally = sp.get_tally(name='flux')
    print(f"Flux in fuel: {tally.mean.flatten()[0]} ± {tally.std_dev.flatten()[0]}")
