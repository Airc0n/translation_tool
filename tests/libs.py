from django.contrib.auth import get_user_model
from django.utils import timezone

passwords = [
    'ohl"ahn8aiSu',
    'la]ePhae1Ies',
    'xareW&ang4sh',
    'haea_d7AiWoo',
    'Eim9Co:e0aev',
    'Ve2eereil>ai',
    'Aengae]t:ie4',
    'ao6Lei+Hip=u',
    'zo!i8aigai{L',
    'Ju8AhGhoo(p?',
    'xieY6fohv>ei',
    'Elu1ie*z5aa3',
    'ooDei1Hoo+Ru',
    'Xohth3ohpu$o',
    'ia)D5AP7sie$',
    'heeb8aeCh-ae'
]


def create_user(username="Aircon", email="aircon@htc.com", raw_password=None,
                date_joined=None, last_login=None, commit=True):
    """ Creates a non-staff user with dynamically generated properties.
    This function dynamically creates an user with following properties:
    - The user is neither an admin nor a staff member.
    - The user is active.
    - The date and his/her last login is generated dynamically.
    """
    if not raw_password:
        import random
        random.shuffle(passwords)
        raw_password = passwords[-1]
    if not date_joined:
        date_joined = timezone.now()
    if not last_login:
        last_login = date_joined
    user = get_user_model()(username=username, email=email, is_active=True, last_login=last_login,
                            date_joined=date_joined)
    user.set_password(raw_password)
    if commit:
        user.save()
    return user



