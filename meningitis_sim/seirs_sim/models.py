# meningitis_sim/seirs_sim/models.py

from django.db import models


class SimulationParameters(models.Model):
    '''defines the parametters the model will accept
    '''
    dur_exp_inf = models.FloatField(default=2.0)  # Duration exposed to infectious
    dur_exp_rec = models.FloatField(default=2.0)  # Duration exposed to recovered
    dur_inf = models.FloatField(default=14.0)     # Duration of infection
    dur_rec = models.FloatField(default=7.0)      # Duration of recovery
    p_death = models.FloatField(default=0.05)     # Probability of death
    p_symptoms = models.FloatField(default=0.4)   # Probability of showing symptoms
    init_prev = models.FloatField(default=0.005)  # Initial prevalence
    beta = models.FloatField(default=0.08)        # Transmission rate
    rel_beta_inf = models.FloatField(default=0.5) # Reduction in transmission for infected vs exposed
    waning = models.FloatField(default=1/1095)    # Immunity waning rate
    imm_boost = models.FloatField(default=0.001)  # Immunity boost

    # vaccine simulation model parameters;
    n_agents = models.IntegerField(default=2000)
    n_timesteps = models.IntegerField(default=20)
    probs = models.CharField(max_length=100, default='0.3, 0.5')
    # imm_boost = models.FloatField(default=0.001)


    # age-based vaccine parameters - stores age range as a comma-separated string
    # for lower bound of age range & upper bound of age range
    age_range = models.CharField(max_length=100, default='0.75, 1.5')

    # used in treatment as an intervention;
    mean_dur_infection = models.FloatField(default=5.0)

    def __str__(self):
        return f'Simulation Parameters {self.id}'
