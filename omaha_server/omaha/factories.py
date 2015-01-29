# coding: utf8

"""
This software is licensed under the Apache 2 license, quoted below.

Copyright 2014 Crystalnix Limited

Licensed under the Apache License, Version 2.0 (the "License"); you may not
use this file except in compliance with the License. You may obtain a copy of
the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
License for the specific language governing permissions and limitations under
the License.
"""

from django.core.files.uploadedfile import SimpleUploadedFile

import factory


class ApplicationFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'omaha.Application'

    id = factory.Sequence(lambda n: '{D0AB2EBC-931B-4013-9FEB-C9C4C2225C%s}' % n)
    name = factory.Sequence(lambda n: 'chrome%s' % n)


class PlatformFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'omaha.Platform'

    name = factory.Sequence(lambda n: 'platform_%s' % n)


class ChannelFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'omaha.Channel'

    name = factory.Sequence(lambda n: 'channel_%s' % n)


class VersionFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'omaha.Version'

    app = factory.lazy_attribute(lambda x: ApplicationFactory())
    platform = factory.lazy_attribute(lambda x: PlatformFactory())
    channel = factory.lazy_attribute(lambda x: ChannelFactory())
    version = '37.0.2062.124'
    file = SimpleUploadedFile('./chrome_installer.exe', b' ' * 123)
    file_size = 123
    file_hash = 'ojan8ermbNHlI5czkED+nc01rxk='