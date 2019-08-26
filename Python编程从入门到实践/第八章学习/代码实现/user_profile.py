#user_profile.py
"""
def build_profile(first,last,**user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
"""
import build_profile as bp
import build_profile
from build_profile import *
from build_profile import build_profile

user_profile = bp.build_profile("albert",'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)
