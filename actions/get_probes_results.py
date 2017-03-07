from lib.action import NapalmBaseAction


class NapalmGetProbesResults(NapalmBaseAction):
    """Get IP SLA Probe results from a network device via NAPALM
    """

    def run(self, **std_kwargs):

        try:

            if self.driver not in ["iosxr", "junos"]:
                raise ValueError(('Not supported with {} driver, only IOS-XR '
                                  'and JunOS are supported.').format(self.driver))

            with self.get_driver(**std_kwargs) as device:
                result = {'raw': device.get_probes_results()}
                if self.htmlout:
                    result['html'] = self.html_out(result['raw'])

        except Exception, e:
            self.logger.error(str(e))
            return (False, str(e))

        return (True, result)
