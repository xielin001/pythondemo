# -*- coding: utf-8 -*-
import netsnmp
 
 
class SnmpClass(object):
    """
    SNMP
    """
    def __init__(self, oid="sysDescr", version='2c', destHost="localhost", community="public"):
        self.oid = oid
        self.version = version
        self.destHost = destHost
        self.community = community
 
    @property
    def query(self):
        """
        snmpwalk
        """
        try:
            result = netsnmp.snmpwalk(self.oid,\
                                      Version=self.version,\
                                      DestHost=self.destHost,\
                                      Community=self.community)
        except Exception as err:
            print (err)
            result = None
        return result
 
 
def main():
    test_obj = SnmpClass(oid="sysobjectID", destHost="192.168.137.11")
    print (test_obj.query)
 
if __name__ == '__main__':
    main()