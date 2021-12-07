import logging
from ShenheDemo.main import *

class ChannelDetail(RunMain):

    def channel_detail(self,**kwargs):
        response = RunMain().run_main('GET',url,data)
        logging.info(response)
        return response
    #logging.info(response)
