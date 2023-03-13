from pycep_correios import get_address_from_cep, WebService


address = get_address_from_cep('04474-340', webservice=WebService.APICEP)
from pyrastreio import correios, jadlog, sequoia
import pycep_correios , sys , requests 
let =['NA976937556BR']


req = requests.get("https://api.linketrack.com/track/json?user=cinbertolo@gmail.com&token=8aad50835e9d24544e38010d3c50285cc1b37838bcf961818d9ab29a891dfa19&codigo=NA976937556BR")
print(req.text)