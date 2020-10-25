from django import template
import hashlib

register = template.Library()

@register.filter
def get_gravatar(value, size=100):
    default_img ='mp'
    url = 'https://www.gravatar.com/avatar/'
    hash_value = hashlib.md5(value.encode('utf-8').lower()).hexdigest()
    return  f'{url}{hash_value}?d={default_img}&s={size}'
