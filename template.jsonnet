local c = import 'martinis.libsonnet';

{
  'tenant': c['tenant'],
  'dc': c['datacenter'],
  'kafka_cluster': std.join(", ", c['kafka_cluster']),
  'component_name': c['component_name']
}