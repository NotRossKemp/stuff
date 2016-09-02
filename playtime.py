ip_address = 8.8.8.8
first_octet = ip_address^\w{1,3}
second_octet =
third_octet =
fourth_octet = 
ip_address_url = 
type_url = ip
domain_url = mypulsant.com
final_url = first_octet + _ + second_octet + _ + third_octet + _ + fourth_octet + type_url + domain_url


print ip_address_url.lower()