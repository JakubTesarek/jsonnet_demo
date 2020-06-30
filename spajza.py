import json
import _jsonnet


conf_global = {
  'application': 'matej'
}

conf_dc = {
  'datacenter': 'cprod',
  'kafka_cluster': [
    '127.0.0.1:3000',
    '127.0.0.2:3000',
    '127.0.0.3:3000'
  ] 
}

conf_component = {
  'component_name': 'api'
}

conf_tenant = {
  'tenant': 'alma-iltalehti',
  'kafka_cluster': [ # use different cluster for this instance
    '127.0.0.4:3000',
    '127.0.0.5:3000',
  ]
}



def importer(directory, file):
  conf = {}
  for c in [conf_global, conf_dc, conf_component, conf_tenant]:
    conf.update(c)

  return f'{directory}/{file}', json.dumps(conf)


json_str = _jsonnet.evaluate_file('template.jsonnet', import_callback=importer)
print(json_str)