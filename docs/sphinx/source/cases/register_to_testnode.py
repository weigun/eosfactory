from  eosfactory import *
import testnet_data

testnode = testnet_data.kylin
configure_testnet(testnode.url)
configure_testnet(testnode.url, prefix="registering_to_testnode")
remove_testnet_files()

if not node_is_operative():
    _.ERROR('''
        This test needs the testnode {} running, but it does not answer.
        '''.format(testnode.url))

create_wallet(file=True)
create_master_account("master")

testnode.create_master_account("master")
