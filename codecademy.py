train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

f100_in_celcius = f_to_c(100)
print(f100_in_celcius)
def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp
c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

def get_force(mass, acceleration):
  force = mass * acceleration
  return force

train_force = get_force(train_mass, train_acceleration)
print(train_force)

print("The GE train supplies ", train_force, " Newtons of force.")

def get_energy(mass,c = 3*10**8):
  energy = mass * c
  return energy

print(get_energy(bomb_mass))

def get_work(mass,acceleration,distance):
  work = get_force(mass, acceleration) * distance
  return work