#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import with_statement

import plistlib
import os.path


class MobileProvisionReadException(Exception):
    pass


class ApplicationIdentifier(object):
    def __init__(self, identifier):
        self.identifier = identifier
        self.short_identifier = identifier.split('.', 1)[1]

    def __str__(self):
        return self.identifier


class MobileProvision(object):
    def __init__(self, provision_file_path):
        self.name = ''
        self.uuid = ''
        self.application_identifier = None
        self.creation_date = None
        self.expiration_date = None
        self.time_to_live = 0
        self.devices_udids = []

        if provision_file_path:
            self.set_from_provision_file(provision_file_path)

    def set_from_provision_file(self, provision_file_path):
        if not os.path.exists(provision_file_path):
            raise MobileProvisionReadException(
                'Could not find mobile provision file at path %s' %
                provision_file_path
            )

        provision_dict = None
        with open(provision_file_path) as provision_file:
            provision_data = provision_file.read()

            start_tag = '<?xml version="1.0" encoding="UTF-8"?>'
            stop_tag = '</plist>'

            try:
                start_index = provision_data.index(start_tag)
                stop_index = provision_data.index(
                    stop_tag, start_index + len(start_tag)
                ) + len(stop_tag)
            except ValueError:
                raise MobileProvisionReadException(
                    'This is not a valid mobile provision file'
                )

            plist_data = provision_data[start_index:stop_index]
            provision_dict = plistlib.readPlistFromString(plist_data)

        self.name = provision_dict['Name']
        self.uuid = provision_dict['UUID']
        self.application_identifier = ApplicationIdentifier(
            provision_dict['Entitlements']['application-identifier'],
        )
        self.creation_date = provision_dict['CreationDate']
        self.expiration_date = provision_dict['ExpirationDate']
        self.time_to_live = provision_dict['TimeToLive']
        self.devices_udids = provision_dict['ProvisionedDevices']

    def __str__(self):
        return self.name


def main():
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)

    if len(sys.argv) < 2:
        logging.error('Please specify a provisioning profile file')
        logging.error('usage: %s app.mobileprovision', sys.argv[0])
        return 1

    provision_file_path = sys.argv[1]

    logging.info('Scanning file %s', provision_file_path)

    try:
        mobile_provision = MobileProvision(provision_file_path)
    except MobileProvisionReadException, exc:
        logging.error(exc)
        return 2

    logging.debug('Name: %s', mobile_provision)
    logging.debug('UUID: %s', mobile_provision.uuid)
    logging.debug(
        'Application identifier: %s',
        mobile_provision.application_identifier
    )
    logging.debug(
        'Short application identifier: %s',
        mobile_provision.application_identifier.short_identifier
    )
    logging.debug('Creation date: %s', mobile_provision.creation_date)
    logging.debug('Expiration date: %s', mobile_provision.expiration_date)
    logging.debug('Time to live: %s', mobile_provision.time_to_live)
    logging.debug('Devices UDIDs:')

    for udid in mobile_provision.devices_udids:
        logging.debug(' * %s', udid)

    return 0


if __name__ == '__main__':
    import logging
    import sys

    sys.exit(main())
