from ncclient import manager
import yaml

with open('../yaml_configs/device_config.yaml') as f:
    config = yaml.safe_load(f)

device = config['device']

with manager.connect(
    host=device['180.87.34.52'],
    port=device['port'],
    username=device['gimecuser1'],
    password=device['XXXX'],
    hostkey_verify=False
) as m:
    config_xml = """
    <config>
      <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
          <name>lo0</name>
          <description>Loopback for test</description>
          <enabled>true</enabled>
        </interface>
      </interfaces>
    </config>
    """
    m.edit_config(target="running", config=config_xml)
