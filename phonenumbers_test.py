import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import *
from phonenumbers.geocoder import description_for_number
from phonenumbers.util import u

# ph_num = input("Enter phone number (ex:+33615296488) :")
ph_num = '+33615296488'

print(region_codes_for_country_code(33))

numobj = phonenumbers.parse(ph_num)
print(numobj)
print('Valid ?',is_valid_number(numobj))

print(region_code_for_number(numobj))

print(description_for_number(numobj,'en'))
print(carrier.name_for_number(numobj,'en'))

gb_number = phonenumbers.parse("+442083612345", "GB")
de_number = phonenumbers.parse("0891234567", "DE")
ch_number = phonenumbers.parse("0431234567", "CH")

print(description_for_number(gb_number, "en"))
# 'London'
print(description_for_number(gb_number, "fr"))  # fall back to English
# 'London'
print(description_for_number(gb_number, "en", region="GB"))
# 'London'
print(description_for_number(gb_number, "en", region="US"))  # fall back to country
# 'United Kingdom'

print(description_for_number(de_number, "en"))
# 'Munich'
print(u('München') == description_for_number(de_number, "de"))
# True


print(u('Zürich') == description_for_number(ch_number, "de"))
# True
print(description_for_number(ch_number, "en"))
# 'Zurich'
print(description_for_number(ch_number, "fr"))
# 'Zurich'
print(description_for_number(ch_number, "it"))
# 'Zurigo'

'''
for k in range(1,99):
    print(k, region_codes_for_country_code(k))
'''


numobj = phonenumbers.parse("18002530000", "US")
nsn = phonenumbers.national_significant_number(numobj)
print(nsn)
ndc_len = phonenumbers.length_of_national_destination_code(numobj)
print(ndc_len)

if ndc_len > 0:
    national_destination_code = nsn[:ndc_len]
    subscriber_number = nsn[ndc_len:]
    print('case 1',national_destination_code,subscriber_number)
else:
    national_destination_code = ""
    subscriber_number = nsn
    print('case 2',national_destination_code,subscriber_number)
