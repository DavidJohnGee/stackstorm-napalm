from napalm import get_network_driver

from lib.action import NapalmBaseAction

class NapalmGetMACTable(NapalmBaseAction):

    def run(self, hostname, driver, port, credentials):

        try:
            # Look up the driver  and if it's not given from the configuration file
            # Also overides the hostname since we might have a partial host i.e. from
            # syslog such as host1 instead of host1.example.com
            #
            (hostname, driver, credentials) = self.find_device_from_config(hostname, driver, credentials)

            login = self._get_credentials(credentials)
            
            if not port:
                optional_args=None
            else:
                optional_args={'port': str(port)}

            with get_network_driver(driver)(
                hostname=str(hostname),
                username=login['username'],
                password=login['password'],
                optional_args=optional_args
            ) as device:
                result = device.get_mac_address_table()

        except Exception, e:
            self.logger.error(str(e))
            return (False, str(e))

        return (True, result)
