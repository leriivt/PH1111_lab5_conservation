#masses
mass_1 = 0.5003
u_mass_1 = 0.0001
mass_2 = 0.4956
u_mass_2 = 0.0001

#inelastic, cart 1
ie_iVelocity_1 = 0.00002858
ie_u_iVelocity_1 = 0.001116
ie_fVelocity_1 = -0.1385
ie_u_fVelocity_1 = 0.003762

#inelastic, cart 2
ie_iVelocity_2 = -0.3138
ie_u_iVelocity_2 = 0.004971
ie_fVelocity_2 = -0.1395
ie_u_fVelocity_2 = 0.003284

#elastic, cart 1
e_iVelocity_1 = 0.0003702
e_u_iVelocity_1 = 0.001003
e_fVelocity_1 = -0.3201
e_u_fVelocity_1 = 0.01063

#elastic, cart 2
e_iVelocity_2 = -0.3476
e_u_iVelocity_2 = 0.006405
e_fVelocity_2 = -0.02968
e_u_fVelocity_2 = 0.002486


def get_KE(mass, velocity):
    return 0.5 * mass * velocity ** 2

def get_momentum(mass, velocity):
    return mass * velocity

def multiplicative_uncertainty(x, ux, y, uy):
    product = x * y
    return abs(product) * (ux/abs(x) + uy/abs(y))

def momentum_measures(mass, u_mass, velocity_i, u_velocity_i, velocity_f, u_velocity_f):
    momentum_i = get_momentum(mass, velocity_i)
    u_momentum_i = multiplicative_uncertainty(mass, u_mass, velocity_i, u_velocity_i)
    
    momentum_f = get_momentum(mass, velocity_f)
    u_momentum_f = multiplicative_uncertainty(mass, u_mass, velocity_f, u_velocity_f)

    return \
    "initial momentum: " + str(momentum_i) + \
    "\ninitial momentum uncertainty: " + str(u_momentum_i) + \
    "\nfinal momentum: " + str(momentum_f) + \
    "\nfinal momentum uncertainty: " + str(u_momentum_f)

def KE_measures(mass, u_mass, velocity_i, u_velocity_i, velocity_f, u_velocity_f):
    KE_i = get_KE(mass, velocity_i)
    #need to propogate uncertainty twice since multiplying 3 terms with uncertainties (v * v * m)
    u_KE_i = multiplicative_uncertainty(velocity_i, u_velocity_i, velocity_i, u_velocity_i)
    u_KE_i = multiplicative_uncertainty(mass, u_mass, velocity_i ** 2, u_KE_i)
    
    KE_f = get_KE(mass, velocity_f)
    u_KE_f = multiplicative_uncertainty(velocity_f, u_velocity_f, velocity_f, u_velocity_f)
    u_KE_f = multiplicative_uncertainty(mass, u_mass, velocity_f ** 2, u_KE_f)

    return \
    "initial KE: " + str(KE_i) + \
    "\ninitial KE uncertainty: " + str(u_KE_i) + \
    "\nfinal KE: " + str(KE_f) + \
    "\nfinal KE uncertainty: " + str(u_KE_f)


print("Inelastic Collision\n-------------------------------")
print("Cart 1")
print(momentum_measures(mass_1, u_mass_1, ie_iVelocity_1, ie_u_iVelocity_1, ie_fVelocity_1, ie_u_fVelocity_1))
print("|")
print(KE_measures(mass_1, u_mass_1, ie_iVelocity_1, ie_u_iVelocity_1, ie_fVelocity_1, ie_u_fVelocity_1))
print("\nCart 2")
print(momentum_measures(mass_2, u_mass_2, ie_iVelocity_2, ie_u_iVelocity_2, ie_fVelocity_2, ie_u_fVelocity_2))
print("|")
print(KE_measures(mass_2, u_mass_2, ie_iVelocity_2, ie_u_iVelocity_2, ie_fVelocity_2, ie_u_fVelocity_2))

print("\n::::::::::::::::::::::::::::::::::::::\n")

print("Elastic Collision\n-------------------------------")
print("Cart 1")
print(momentum_measures(mass_1, u_mass_1, e_iVelocity_1, e_u_iVelocity_1, e_fVelocity_1, e_u_fVelocity_1))
print("|")
print(KE_measures(mass_1, u_mass_1, e_iVelocity_1, e_u_iVelocity_1, e_fVelocity_1, e_u_fVelocity_1))
print("\nCart 2")
print(momentum_measures(mass_2, u_mass_2, e_iVelocity_2, e_u_iVelocity_2, e_fVelocity_2, e_u_fVelocity_2))
print("|")
print(KE_measures(mass_2, u_mass_2, e_iVelocity_2, e_u_iVelocity_2, e_fVelocity_2, e_u_fVelocity_2))












