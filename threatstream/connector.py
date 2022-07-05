""" Copyright start
  Copyright (C) 2008 - 2020 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """
# -----------------------------------------
# Anomali ThreatStream
# -----------------------------------------

from .operations import *
from connectors.core.connector import Connector, get_logger, ConnectorError

logger = get_logger('anomali-threatstream')


class ThreatStream(Connector):
    def execute(self, config, operation, params, **kwargs):
        logger.info('execute(): operation is {0}'.format(str(operation)))
        try:
            logger.info('execute [{0}]'.format(operation))
            operation_info = get_curr_oper_info(self._info_json, operation)
            if operation_info['handler_method'] is False:
                return api_request(config, params, operation_info)
            else:
                operation = operation_sym.get(operation)
                return operation(config, params)
        except Exception as err:
            logger.exception(err)
            raise ConnectorError(err)

    def check_health(self, config):
        logger.info('Performing health check')
        check_health(config)
        logger.info('Completed health check with no error')
