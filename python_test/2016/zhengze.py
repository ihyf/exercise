# coding:utf-8

import re

str='1.1.1'
regex = re.compile(
    r'^[0-9]+\.[0-9]+\.[0-9]{1,}$',
    r''

    ,re.IGNORECASE
)
m=regex.match(str)
if m:
    print 'True'
else:
    print 'False'

a = '''
select r.cooperative_company_id from res_partner as r where r.parent_id in
  (select rp.parent_id from res_users as ru,res_partner as rp
    where ru.partner_id=rp.id and ru.id=%s)

'''