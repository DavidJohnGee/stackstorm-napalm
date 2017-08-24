from lib.action import NapalmBaseAction


class NapalmGetBGPneighbors(NapalmBaseAction):
    """Get BGP neighbors from a network device via NAPALM
    """

    def run(self, routing_instance, neighbor, **std_kwargs):

        with self.get_driver(**std_kwargs) as device:
            result = device.get_bgp_neighbors()

            if routing_instance not in result:
                raise ValueError(('Routing instance {} does not exist on '
                                  'this device.').format(routing_instance))

            if not neighbor:
                bgp_neighbors = result[routing_instance]['peers']
            else:
                if neighbor not in result[routing_instance]['peers']:
                    raise ValueError(('BGP neighbor {} does not exist '
                                      'on this device.').format(neighbor))
                else:
                    bgp_neighbors = result[routing_instance]['peers'][neighbor]

            result = {'raw': bgp_neighbors}

            if self.htmlout:
                result['html'] = self.html_out(result['raw'])

        return (True, result)
