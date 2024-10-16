from oxrse_unit_conv.si import *
from oxrse_unit_conv.meta.classes import Unit

# second
minute = Unit(name='minute', abbr='min', si=second, to_si_fun=lambda n: n * 60)
# min shadows the builtin function 'min'

hour = Unit(name='hour', abbr='h', si=second, to_si_fun=lambda n: n * 3600)
h = hour

# meter
kilometer = Unit(name='kilometer', abbr="km", si=meter, to_si_fun=lambda n: n * 1000)
km = kilometer

# mile calculator
mile = Unit(name='mile', abbr='mile', si=meter, to_si_fun=lambda n: n * 1_609.344)
mile = mile

# meter_sq
meter_sq = Unit(name='meter_sq', abbr="km_sq", si=meter, to_si_fun=lambda n: n ** 2)
km_sq = meter_sq

# meter_cu

# kilogram
kilogram = Unit(name='kilogram', abbr="kg", si=gram, to_si_fun=lambda n: n * 1000)
kg = kilogram

pound = Unit(name='pound', abbr='lb', si=kilogram, to_si_fun=lambda n: n * 0.4535924)
lb = pound

# ampere

# kelvin

# mole

# candela
